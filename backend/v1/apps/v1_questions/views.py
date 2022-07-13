from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from djangoTask.helpers import ERROR, SuccessfulResponse
from v1.apps.v1_lessons.models import Lesson
from v1.apps.v1_questions.models import Question
from v1.apps.v1_questions.serializers import QuestionSerializer, QuestionSerializerName


class QuestionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Список вопросов к уроку',
        request=QuestionSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=QuestionSerializer
            ),
        }
    )
    def list(self, request, pk):
        try:
            lesson = Lesson.objects.get(id=pk)
        except Lesson.DoesNotExist:
            return ERROR.LESSON_DOES_NOT_EXIST

        queryset = Question.objects.filter(lesson=lesson.id)
        serializer = QuestionSerializer(queryset, many=True)
        return SuccessfulResponse(serializer.data)

    def retrieve(self, request, pk):
        try:
            queryset = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return ERROR.QUESTION_DOES_NOT_EXIST
        serializer = QuestionSerializerName(
            queryset
        )
        return SuccessfulResponse(serializer.data)