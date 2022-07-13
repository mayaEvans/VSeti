from rest_framework import serializers

from v1.apps.v1_entrance_questions.models import EntranceQuestion


class EntranceQuestionSerializer(serializers.ModelSerializer):
    options = serializers.StringRelatedField(many=True)

    class Meta:
        model = EntranceQuestion
        fields = ['id', 'text', 'options']


class EntranceQuestionSerializerName(serializers.ModelSerializer):
    class Meta:
        model = EntranceQuestion
        fields = ['text']
