from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from djangoTask.helpers import ERROR, SuccessfulResponse
from v1.apps.v1_courses.models import UserOnCourse, Course
from v1.apps.v1_reviews.models import Review
from v1.apps.v1_reviews.serializers import ReviewRetrieveSerializer
from v1.apps.v1_users.models import User


class ReviewViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @extend_schema(
        summary='Список отзывов у курса',
        request=ReviewRetrieveSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=ReviewRetrieveSerializer
            ),
        }
    )
    def list(self, request, pk):
        try:
            course = Course.objects.get(id=pk)
        except Course.DoesNotExist:
            return ERROR.COURSE_DOES_NOT_EXIST

        queryset = Review.objects.filter(course=course.id)
        serializer = ReviewRetrieveSerializer(queryset, many=True)
        return SuccessfulResponse(serializer.data)

    @extend_schema(
        summary='Добавить отзыв на курс',
        request=ReviewRetrieveSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=ReviewRetrieveSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Номер курса', required=True,
                             type=int)
        ]
    )
    def create(self, request, pk):
        user = User.objects.get(id=request.user.id)
        try:
            course = Course.objects.get(id=pk)
            user_on_course = UserOnCourse.objects.get(user=user, course=course)
        except Course.DoesNotExist:
            return ERROR.COURSE_DOES_NOT_EXIST
        except UserOnCourse.DoesNotExist:
            return ERROR.USER_ON_COURSE_DOES_NOT_EXIST

        try:
            Review.objects.get(user=user_on_course, course=course)
            return ERROR.REVIEW_ALREADY_EXISTS
        except Review.DoesNotExist:
            serializer = ReviewRetrieveSerializer(
                data={
                    'user': user_on_course.id,
                    'course': course.id,
                    'text': request.data.get("text"),
                    'rating': request.data.get("rating")
                }
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return SuccessfulResponse(serializer.data)
