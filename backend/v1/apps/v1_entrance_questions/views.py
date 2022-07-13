from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from djangoTask.helpers import SuccessfulResponse
from v1.apps.v1_entrance_questions.models import EntranceQuestion
from v1.apps.v1_entrance_questions.serializers import EntranceQuestionSerializer


class EntranceQuestionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Список вопросов входного тестирования',
        request=EntranceQuestionSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=EntranceQuestionSerializer
            ),
        }
    )
    def list(self, request):
        queryset = EntranceQuestion.objects.all()
        serializer = EntranceQuestionSerializer(queryset, many=True)
        return SuccessfulResponse(serializer.data)
