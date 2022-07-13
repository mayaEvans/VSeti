from rest_framework import serializers

from v1.apps.v1_answer.models import Answer
from v1.apps.v1_options.serializers import TestOptionsSerializer


class TestAnswerOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'user', 'text', 'selected_options', 'correct']


class TestAnswerInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'user', 'text', 'selected_options']


class TextTestAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'user', 'text', 'correct']


class OptionsTestAnswerSerializer(serializers.ModelSerializer):
    selected_options = TestOptionsSerializer(many=True)

    class Meta:
        model = Answer
        fields = ['id', 'question', 'user', 'selected_options', 'correct']
