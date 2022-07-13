from django.urls import path

from v1.apps.v1_answer.views import AnswerViewSet

urlpatterns = [
    path('question/<int:pk>', AnswerViewSet.as_view({
        'post': 'create',
    })),
    path('<int:pk>', AnswerViewSet.as_view({
        'get': 'retrieve',
    })),
]