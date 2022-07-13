from django.urls import path

from v1.apps.v1_questions.views import QuestionViewSet

urlpatterns = [
    path('lesson/<int:pk>', QuestionViewSet.as_view({
        'get': 'list'
    }))
]

