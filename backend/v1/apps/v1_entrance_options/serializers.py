from rest_framework import serializers
from v1.apps.v1_entrance_options.models import EntranceOption


class EntranceOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntranceOption
        fields = ['option']