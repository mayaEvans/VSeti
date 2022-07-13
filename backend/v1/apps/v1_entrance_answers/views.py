import math

from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from djangoTask.helpers import SuccessfulResponse, SuccessfulLevelChanging
from v1.apps.v1_entrance_answers.models import EntranceAnswer
from v1.apps.v1_entrance_answers.serializers import EntranceAnswerSerializer, EntranceAnswerInputSerializer
from v1.apps.v1_entrance_questions.models import EntranceQuestion
from v1.apps.v1_users.models import User


class EntranceAnswerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Записать ответ на вопрос из входного тестирования',
        request=EntranceAnswerInputSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=EntranceAnswerSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Номер вопроса', required=True,
                             type=int)
        ]
    )
    def create(self, request, pk):
        user = User.objects.get(id=request.user.id)
        entrance_question = get_object_or_404(EntranceQuestion, id=pk)
        entrance_answer = EntranceAnswer(
            entrance_question=entrance_question,
            user=user
        )
        entrance_answer.save()

        chosen_options = entrance_question.options.filter(id__in=request.data.get("selected_options"))
        correct_options = entrance_question.options.filter(is_correct=True)
        if set(correct_options) == set(chosen_options):
            entrance_answer.correct = True
        else:
            entrance_answer.correct = False
        entrance_answer.selected_options.set(chosen_options)
        entrance_answer.save()

        all_entrance_questions = EntranceQuestion.objects.all().count()

        if all_entrance_questions == EntranceAnswer.objects.filter(user=user).count():
            correct_user_answers = EntranceAnswer.objects.filter(user=user, correct=True).count()
            print(correct_user_answers)
            num = math.ceil(correct_user_answers / all_entrance_questions * 100)
            if num <= 30:
                user.level = 1
            elif num <= 60:
                user.level = 2
            elif num > 60:
                user.level = 3
            user.save()
            return SuccessfulLevelChanging(user.level)
        else:
            return SuccessfulResponse(entrance_answer.correct)

    @extend_schema(
        summary='Отображение ответа на вопрос во входном тестировании',
        request=EntranceAnswerSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=EntranceAnswerSerializer
            )
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Номер ответа', required=True,
                             type=int)
        ]
    )
    def retrieve(self, request, pk):
        entrance_answer = get_object_or_404(EntranceAnswer, pk=pk)
        serializer = EntranceAnswerSerializer(entrance_answer)
        return SuccessfulResponse(serializer.data)
