from django.urls import path

from v1.apps.v1_entrance_questions.views import EntranceQuestionViewSet

urlpatterns = [
    path('', EntranceQuestionViewSet.as_view({
        'get': 'list'
    }))
]
