from django.urls import path

from v1.apps.v1_entrance_answers.views import EntranceAnswerViewSet

urlpatterns = [
    path('entrance_question/<int:pk>', EntranceAnswerViewSet.as_view({
        'post': 'create',
    })),
    path('<int:pk>', EntranceAnswerViewSet.as_view({
        'get': 'retrieve',
    })),
]