from rest_framework import serializers
from v1.apps.v1_lessons.models import Lesson


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'name', 'theory', 'order', 'date_posted']

