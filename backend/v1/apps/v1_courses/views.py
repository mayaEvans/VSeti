from drf_spectacular.utils import OpenApiParameter, OpenApiResponse, extend_schema
from rest_framework import permissions, viewsets
from rest_framework.decorators import action, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny

from djangoTask.helpers import ERROR, SuccessfulResponse
from v1.apps.v1_courses.models import Course, UserOnCourse
from v1.apps.v1_courses.serializers import CourseListSerializer, CourseRetrieveSerializer, UserOnCourseListSerializer, \
    CourseCreateSerializer
from v1.apps.v1_users.models import User


class CourseViewSet(viewsets.ViewSet):
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [AllowAny]

    # parser_classes = [MultiPartParser]

    @extend_schema(
        summary='Список курсов (общий и личный)',
        request=CourseListSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=CourseListSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='my', description='Список курсов авторизированного пользователя', required=False,
                             type=str)
        ]
    )
    def list(self, request):
        my = request.query_params.get('my', None)
        if my:
            queryset = [i.course for i in UserOnCourse.objects.filter(user=request.user)]
        else:
            queryset = Course.objects.all()
        serializer = CourseListSerializer(queryset, many=True)
        return SuccessfulResponse(serializer.data)

    @extend_schema(
        summary='Создать курс',
        request=CourseCreateSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=CourseCreateSerializer
            ),
        }
    )
    @parser_classes(MultiPartParser)
    def create(self, request):
        serializer = CourseCreateSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessfulResponse(serializer.data)

    @extend_schema(
        summary='Вывод информации о курсе и статуса юзера на нем (если авторизован)',
        request=CourseRetrieveSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=CourseRetrieveSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='id', location=OpenApiParameter.PATH, description='Курс', required=True, type=int)
        ]
    )
    def retrieve(self, request, pk):
        try:
            queryset = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return ERROR.COURSE_DOES_NOT_EXIST
        serializer = CourseRetrieveSerializer(
            queryset,
            context={"user_id": request.user.id}
        )
        return SuccessfulResponse(serializer.data)

    @extend_schema(
        summary='Удаление курса',
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
            ),
        },
    )
    def destroy(self, request, pk):
        try:
            queryset = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return ERROR.COURSE_DOES_NOT_EXIST
        queryset.delete()
        return SuccessfulResponse()

    @extend_schema(
        summary='Изменение информации о курсе',
        request=CourseListSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=CourseListSerializer
            ),
        },
    )
    @parser_classes(MultiPartParser)
    def update(self, request, pk):
        try:
            queryset = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return ERROR.COURSE_DOES_NOT_EXIST
        serializer = CourseListSerializer(
            queryset,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessfulResponse(serializer.data)

    @extend_schema(
        summary='Удаление юзера с курса',
        responses={
            200: OpenApiResponse(description='SuccessfulResponse'),
        }
    )
    @action(detail=True, methods=['delete'], permission_classes=[permissions.IsAuthenticatedOrReadOnly])
    def unsubscribe_from_course(self, request, pk):
        try:
            queryset = UserOnCourse.objects.get(user=request.user, course=pk)
        except UserOnCourse.DoesNotExist:
            return ERROR.USER_ON_COURSE_DOES_NOT_EXIST
        queryset.delete()
        return SuccessfulResponse()

    @extend_schema(
        summary='Запись юзера на курс',
        request=UserOnCourseListSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=UserOnCourseListSerializer
            ),
        }
    )
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def subscribe_to_course(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return ERROR.COURSE_DOES_NOT_EXIST

        user = User.objects.get(id=request.user.id)
        serializer = UserOnCourseListSerializer(data={'user': user.id, 'course': course.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessfulResponse(serializer.data)

    # if not UserOnCourse.objects.filter(course=course_pk, user=request.user).exists():
    #     serializer = UserOnCourseListSerializer(data=request.data)
    # else:
    #     queryset = UserOnCourse.objects.get(course=course_pk, user=request.user)
    #     serializer = UserOnCourseListSerializer(
    #         queryset,
    #         data=request.data,
    #     )
    # print(request.data)
    # serializer.save(course=course_pk, user=request.user)
