from django.urls import path

from v1.apps.v1_reviews.views import ReviewViewSet

urlpatterns = [
    path('course/<int:pk>', ReviewViewSet.as_view({
        'post': 'create',
        'get': 'list',
    })),
]
