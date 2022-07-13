import math
from io import BytesIO

from django.http import HttpResponse
from django.template.loader import get_template
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from transliterate import translit
from xhtml2pdf import pisa

from djangoTask.helpers import ERROR, SuccessfulResponse
from v1.apps.v1_certificates.models import Certificate
from v1.apps.v1_certificates.serializers import CertificateSerializer, CertificateOutputSerializer
from v1.apps.v1_courses.models import Course, UserOnCourse
from v1.apps.v1_lessons.models import Lesson
from v1.apps.v1_questions.models import Question
from v1.apps.v1_answer.models import Answer
from v1.apps.v1_users.models import User


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result, encoding='utf-8')
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def get_data(user, num, course, cert_num, cert_date):
    user_fullname = translit(user.first_name, "ru", reversed=True) + ' ' \
                    + translit(user.last_name, "ru", reversed=True) + ' ' \
                    + translit(user.patronymic, "ru", reversed=True)
    course_name = course.english_name
    cert_num = 1000 + cert_num

    data = {
        "user_on_course": user_fullname,
        "course": course_name,
        "kurator": "Korovin D. V.",
        "num": num,
        "date": cert_date.strftime('%d %b %Y'),
        "cert_num": cert_num
    }
    return data


def get_data_by_id(certificate_pk):
    try:
        user_on_course = Certificate.objects.get(id=certificate_pk).user
        user = User.objects.get(id=user_on_course.user.id)
        course = Certificate.objects.get(id=certificate_pk).course
    except Course.DoesNotExist:
        return ERROR.COURSE_DOES_NOT_EXIST
    except UserOnCourse.DoesNotExist:
        return ERROR.USER_ON_COURSE_DOES_NOT_EXIST
    except User.DoesNotExist:
        return ERROR.USER_DOES_NOT_EXIST

    date = Certificate.objects.get(id=certificate_pk).date_added
    user_fullname = translit(user.first_name, "ru", reversed=True) + ' ' \
                    + translit(user.last_name, "ru", reversed=True) + ' ' \
                    + translit(user.patronymic, "ru", reversed=True)
    course_name = course.english_name
    lessons = Lesson.objects.filter(course=course.id)
    all_questions = Question.objects.filter(lesson__in=lessons).count()
    correct_answers = Answer.objects.filter(
        user=user_on_course.id,
        is_correct=True,
        question__in=Question.objects.filter(lesson__in=lessons)
    ).count()
    num = math.ceil(correct_answers / all_questions * 100)

    cert_num = 1000 + certificate_pk

    data = {
        "user_on_course": user_fullname,
        "course": course_name,
        "kurator": "Korovin D. V.",
        "num": num,
        "date": date.strftime('%d %b %Y'),
        "cert_num": cert_num
    }
    return data


class CertificateViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Создать сертификат',
        request=CertificateSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=CertificateSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Номер курса', required=True,
                             type=int)
        ]
    )
    def create(self, request, pk):
        global num
        num = -1000
        user = User.objects.get(id=request.user.id)
        try:
            course = Course.objects.get(id=pk)
            user_on_course = UserOnCourse.objects.get(user=user, course=course)
            lessons = Lesson.objects.filter(course=course.id)
            all_questions = Question.objects.filter(lesson__in=lessons).count()
            correct_answers = Answer.objects.filter(
                user=user_on_course.id,
                correct=True,
                question__in=Question.objects.filter(lesson__in=lessons)
            ).count()
        except Course.DoesNotExist:
            return ERROR.COURSE_DOES_NOT_EXIST
        except UserOnCourse.DoesNotExist:
            return ERROR.USER_ON_COURSE_DOES_NOT_EXIST
        except Answer.DoesNotExist:
            return ERROR.INSUFFICIENT_PROGRESS_FOR_CERTIFICATE
        except Question.DoesNotExist:
            return ERROR.NO_QUESTIONS_ON_COURSE

        try:
            num = math.ceil(correct_answers / all_questions * 100)
            if num < 60:
                return ERROR.INSUFFICIENT_PROGRESS_FOR_CERTIFICATE
        except ZeroDivisionError:
            return ERROR.INSUFFICIENT_PROGRESS_FOR_CERTIFICATE

        try:
            # existing_certificate_progress = Certificate.objects.filter(user=user_on_course, course=course)
            queryset = [i.progress for i in Certificate.objects.filter(user=user_on_course, course=course)]
            for i in queryset:
                if i == num:
                    return ERROR.CERTIFICATE_ALREADY_EXISTS
        except Certificate.DoesNotExist:
            print("certificate does not exists")

        serializer = CertificateSerializer(
            data={'user': user_on_course.id, 'course': course.id, 'progress': num}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        cert_num = Certificate.objects.filter(
            course=course.id,
            user=user_on_course.id) \
            .latest('date_added').id
        cert_date = Certificate.objects.filter(
            course=course.id,
            user=user_on_course.id) \
            .latest('date_added').date_added

        data = get_data(user, num, course, cert_num, cert_date)
        pdf = render_to_pdf('../templates/cert.html', data)

        cert_num += 1000
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Certificate_%s.pdf" % cert_num
        content = "attachment; filename=%s" % filename
        response['Content-Disposition'] = content
        return response

    @extend_schema(
        summary='Просмотр сертификата',
        request=CertificateSerializer,
        responses={
            # (200, 'application/pdf'): OpenApiTypes.BINARY
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=CertificateSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Номер сертификата', required=True,
                             type=int)
        ]
    )
    def retrieve(self, request, pk):
        try:
            queryset = Certificate.objects.get(pk=pk)
        except Certificate.DoesNotExist:
            return ERROR.CERTIFICATE_DOES_NOT_EXIST
        print(queryset.pk)
        data1 = get_data_by_id(queryset.pk)

        pdf = render_to_pdf('../templates/cert.html', data1)
        cert_num = queryset.id + 1000
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Certificate_%s.pdf" % cert_num
        content = "attachment; filename=%s" % filename
        response['Content-Disposition'] = content
        return response

    @extend_schema(
        summary='Список сертификатов юзера',
        request=CertificateOutputSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=CertificateOutputSerializer
            ),
        }
    )
    def list(self, request):
        user = User.objects.get(id=request.user.id)
        try:
            user_on_course = UserOnCourse.objects.filter(user=user)
        except UserOnCourse.DoesNotExist:
            return ERROR.USER_ON_COURSE_DOES_NOT_EXIST

        queryset = Certificate.objects.filter(user__in=user_on_course)
        serializer = CertificateOutputSerializer(queryset, many=True)
        return SuccessfulResponse(serializer.data)
