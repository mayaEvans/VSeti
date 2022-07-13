from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from djangoTask.helpers import SuccessfulResponse, ERROR
from v1.apps.v1_answer.models import Answer
from v1.apps.v1_answer.serializers import TextTestAnswerSerializer, OptionsTestAnswerSerializer, \
    TestAnswerOutputSerializer, TestAnswerInputSerializer
from v1.apps.v1_courses.models import UserOnCourse
from v1.apps.v1_questions.models import Question
from v1.apps.v1_users.models import User


class AnswerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Записать ответ на задание',
        request=TestAnswerInputSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=TestAnswerInputSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Номер вопроса', required=True,
                             type=int)
        ]
    )
    def create(self, request, pk):
        user = User.objects.get(id=request.user.id)
        question = get_object_or_404(Question, id=pk)
        try:
            user_on_course = UserOnCourse.objects.get(user=user, course=question.lesson.course)
        except UserOnCourse.DoesNotExist:
            return ERROR.USER_ON_COURSE_DOES_NOT_EXIST
        answer = Answer(
            question=question,
            user=user_on_course
        )
        if not question.options.exists():
            answer.text = request.data.get('text')
            answer.save()
        else:
            answer.save()
            chosen_options = question.options.filter(id__in=request.data.get("selected_options"))
            correct_options = question.options.filter(is_correct=True)
            if set(correct_options) == set(chosen_options):
                answer.correct = True
            else:
                answer.correct = False
            answer.selected_options.set(chosen_options)
            answer.save()
        return SuccessfulResponse(answer.correct)

    @extend_schema(
        summary='Отображение ответа на задание',
        request=TestAnswerOutputSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=TestAnswerOutputSerializer
            )
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Номер ответа', required=True,
                             type=int)
        ]
    )
    def retrieve(self, request, pk):
        answer = get_object_or_404(Answer, pk=pk)

        if answer.question.options.exists():
            serializer = OptionsTestAnswerSerializer(answer)
        else:
            serializer = TextTestAnswerSerializer(answer)
        return SuccessfulResponse(serializer.data)
