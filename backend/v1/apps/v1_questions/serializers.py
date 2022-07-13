from rest_framework import serializers

from v1.apps.v1_options.serializers import TestOptionsSerializer
from v1.apps.v1_questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    # options = serializers.StringRelatedField(many=True)
    options =TestOptionsSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'options']


class QuestionSerializerName(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['text']
