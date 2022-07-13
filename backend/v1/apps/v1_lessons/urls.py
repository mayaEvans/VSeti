from django.urls import path
from v1.apps.v1_lessons.views import LessonViewSet

urlpatterns = [
    path('course/<int:pk>', LessonViewSet.as_view({
        'get': 'list',
        # 'post': 'create'
    })),
    path('<int:pk>', LessonViewSet.as_view({
        'get': 'retrieve',
#         'delete': 'destroy',
#         'post': 'update'
    })),
]
