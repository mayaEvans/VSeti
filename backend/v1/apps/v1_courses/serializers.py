from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.parsers import MultiPartParser

from v1.apps.v1_courses.models import Course, UserOnCourse
from v1.apps.v1_reviews.models import Review


class CourseListSerializer(serializers.ModelSerializer):
    listeners_number = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.INT)
    def get_listeners_number(self, queryset):
        try:
            listeners = UserOnCourse.objects.filter(course=queryset.id).count()
            return listeners
        except UserOnCourse.DoesNotExist:
            return 0

    @extend_schema_field(OpenApiTypes.DOUBLE)
    def get_rating(self, queryset):
        try:
            review_number = Review.objects.filter(course=queryset.id).count()
            if review_number == 0:
                return 5
            review_sum = 0
            for i in Review.objects.filter(course=queryset.id):
                review_sum += i.rating
            rating = review_sum / review_number
            return round(rating, 1)
        except Review.DoesNotExist:
            return 5

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'photo', 'short_description', 'status', 'rating', 'listeners_number',
                  'rating']


class CourseCreateSerializer(serializers.ModelSerializer):
    parser_classes = [MultiPartParser]
    photo = serializers.ImageField()

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'photo', 'short_description', 'status', 'rating']


class CourseRetrieveSerializer(serializers.ModelSerializer):
    user_status = serializers.SerializerMethodField()
    listeners_number = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    @extend_schema_field(OpenApiTypes.STR)
    def get_user_status(self, queryset):
        try:
            user = UserOnCourse.objects.get(course=queryset.id, user=self.context.get("user_id"))
            return user.user_status
        except UserOnCourse.DoesNotExist:
            return None

    @extend_schema_field(OpenApiTypes.INT)
    def get_listeners_number(self, queryset):
        try:
            listeners = UserOnCourse.objects.filter(course=queryset.id).count()
            return listeners
        except UserOnCourse.DoesNotExist:
            return 0

    @extend_schema_field(OpenApiTypes.DOUBLE)
    def get_rating(self, queryset):
        try:
            review_number = Review.objects.filter(course=queryset.id).count()
            if review_number == 0:
                return 5
            review_sum = 0
            for i in Review.objects.filter(course=queryset.id):
                review_sum += i.rating
            rating = review_sum / review_number
            return round(rating, 1)
        except Review.DoesNotExist:
            return 5

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'photo', 'short_description', 'status', 'rating', 'listeners_number',
                  'user_status', 'rating')


class CourseCertificateSerializer(serializers.ModelSerializer):
    parser_classes = [MultiPartParser]
    photo = serializers.ImageField()

    class Meta:
        model = Course
        fields = ['name', 'photo']


class UserOnCourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOnCourse
        fields = ['id', 'user', 'course', 'user_status', 'date_updated']
