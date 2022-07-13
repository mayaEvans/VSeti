from rest_framework import serializers

from v1.apps.v1_certificates.models import Certificate
from v1.apps.v1_courses.serializers import CourseCertificateSerializer


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'user', 'course', 'progress', 'date_added']


class CertificateOutputSerializer(serializers.ModelSerializer):
    course = CourseCertificateSerializer()

    class Meta:
        model = Certificate
        fields = ['id', 'course', 'progress', 'date_added']
