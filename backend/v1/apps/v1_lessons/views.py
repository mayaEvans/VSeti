from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny

from djangoTask.helpers import ERROR, SuccessfulResponse
from v1.apps.v1_courses.models import Course
from v1.apps.v1_lessons.models import Lesson
from v1.apps.v1_lessons.serializers import LessonListSerializer


class LessonViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]

    @extend_schema(
        summary='Список уроков курса',
        request=LessonListSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=LessonListSerializer
            ),
        }
    )
    def list(self, request, pk):
        try:
            course = Course.objects.get(id=pk)
        except Course.DoesNotExist:
            return ERROR.COURSE_DOES_NOT_EXIST
        queryset = Lesson.objects.filter(course=course)
        serializer = LessonListSerializer(queryset, many=True)
        return SuccessfulResponse(serializer.data)

    @extend_schema(
        summary='Отображение урока',
        request=LessonListSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=LessonListSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Номер урока и задания',
                             required=True, type=int)
        ]
    )
    def retrieve(self, request, pk):
        try:
            queryset = Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            return ERROR.LESSON_DOES_NOT_EXIST
        serializer = LessonListSerializer(queryset)
        return SuccessfulResponse(serializer.data)
