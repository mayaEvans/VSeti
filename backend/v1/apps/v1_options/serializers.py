from rest_framework import serializers

from v1.apps.v1_options.models import Option


class TestOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id','option']