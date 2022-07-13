from django.urls import path

from .views import CertificateViewSet

urlpatterns = [
    path('', CertificateViewSet.as_view({
        'get': 'list',
    })),
    path('course/<int:pk>', CertificateViewSet.as_view({
        'post': 'create',
    })),
    path('<int:pk>', CertificateViewSet.as_view({
        'get': 'retrieve',
    })),
]
