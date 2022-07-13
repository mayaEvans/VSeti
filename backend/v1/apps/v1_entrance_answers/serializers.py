from v1.apps.v1_entrance_answers.models import EntranceAnswer
from v1.apps.v1_entrance_options.serializers import EntranceOptionsSerializer
from rest_framework import serializers


class EntranceAnswerSerializer(serializers.ModelSerializer):
    selected_options = EntranceOptionsSerializer(many=True)

    class Meta:
        model = EntranceAnswer
        fields = ['id', 'entrance_question', 'user', 'selected_options', 'correct']


class EntranceAnswerInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceAnswer
        fields = ['id', 'entrance_question', 'user', 'selected_options']