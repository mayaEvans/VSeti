from rest_framework import serializers

from v1.apps.v1_reviews.models import Review


class ReviewRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'text', 'date', 'rating']
