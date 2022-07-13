from django.urls import include, re_path
from v1.apps.v1_reviews import urls as reviews_urls
from v1.apps.v1_courses import urls as courses_urls
from v1.apps.v1_users import urls as users_urls
from v1.apps.v1_lessons import urls as lessons_urls
from v1.apps.v1_certificates import urls as certificates_urls
from v1.apps.v1_questions import urls as questions_urls
from v1.apps.v1_answer import urls as answers_urls
from v1.apps.v1_entrance_answers import urls as entrance_answers_urls
from v1.apps.v1_entrance_questions import urls as entrance_questions_urls

urlpatterns = [
    re_path(r"^reviews/", include(reviews_urls)),
    re_path(r'^courses/', include(courses_urls)),
    re_path(r"^users/", include(users_urls)),
    re_path(r"^lessons/", include(lessons_urls)),
    re_path(r"^entrance_answers/", include(entrance_answers_urls)),
    re_path(r"^entrance_questions/", include(entrance_questions_urls)),
    re_path(r"^certificates/", include(certificates_urls)),
    re_path(r"^questions/", include(questions_urls)),
    re_path(r"^answers/", include(answers_urls)),
]
