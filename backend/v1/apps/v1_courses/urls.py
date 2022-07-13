from django.urls import path
from v1.apps.v1_courses.views import CourseViewSet

urlpatterns = [
    path('', CourseViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>', CourseViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'post': 'update'
    })),
    path('<int:pk>/status', CourseViewSet.as_view({
        'delete': 'unsubscribe_from_course',
        'post': 'subscribe_to_course',
    })),
]
