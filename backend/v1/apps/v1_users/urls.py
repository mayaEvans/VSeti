from django.urls import path

from v1.apps.v1_users.views import UserRegistrationView, UserAuthView, UserLogoutView, UserActivateView, \
    ForgotPasswordByEmailView, UserChangePasswordByEmailView, UserChangePasswordView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view()),
    path('login/', UserAuthView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('activate/<uidb64>/<token>/', UserActivateView.as_view(), name="activate"),
    path('reset/<uidb64>/<token>/', UserChangePasswordByEmailView.as_view(), name="reset"),
    path('change_password/', UserChangePasswordView.as_view()),
    path('forget_password/', ForgotPasswordByEmailView.as_view())
]
