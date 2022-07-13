import json

from django.contrib.auth import login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from drf_spectacular.utils import OpenApiResponse, extend_schema, OpenApiParameter
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from djangoTask.helpers import SuccessfulResponse, SuccessfulEmailSending, ERROR
from .models import User
from .serializers import UserLoginSerializer, UserRegistrationSerializer, UserLoginOutputSerializer, \
    UserForgotPasswordRequestByEmailSerialiser
from .token import account_activation_token


class UserRegistrationView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]

    @extend_schema(
        summary='Регистрация пользователя',
        request=UserRegistrationSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=UserRegistrationSerializer
            ),
        },
        auth=[]
    )
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        # Проверка данных
        if serializer.is_valid():
            serializer.save()
            email = serializer.data.get("email")
            user = User.objects.get(email=email)
            to_email = email
            current_site = get_current_site(request)
            mail_subject = 'Подтвердите свой аккаунт'
            message = render_to_string('email_template.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user),
                'fullname': user.last_name + " " + user.first_name + " " + user.patronymic
            })
            send_mail(mail_subject, message, 'youremail', [to_email])
            return SuccessfulEmailSending(serializer.data)

            # return SuccessfulResponse(serializer.data)
        else:
            data = serializer.errors
            return Response(data)


class UserAuthView(ObtainAuthToken):
    authentication_classes = []
    permission_classes = [AllowAny]

    @extend_schema(
        summary='Авторизация пользователя',
        request=UserLoginSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=UserLoginOutputSerializer
            ),
        },
        auth=[]
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.is_active:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            output_serializer = UserLoginOutputSerializer(token)
            print(output_serializer.data)
            return SuccessfulResponse(output_serializer.data)
        else:
            return ERROR.NOT_VERIFIED_ACCOUNT


class UserLogoutView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Выход из аккаунта',
        request=UserLoginSerializer,
        responses={
            200: OpenApiResponse(description='SuccessfulResponse'),
        }
    )
    def post(self, request):
        logout(request)
        return SuccessfulResponse()


class UserActivateView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary='Активация аккаунта',
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse'
            ),
        },
        parameters=[
            OpenApiParameter(name='uidb64', location=OpenApiParameter.PATH, required=True, type=str),
            OpenApiParameter(name='token', location=OpenApiParameter.PATH, required=True, type=str)
        ],
        auth=[]
    )
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return SuccessfulResponse()
        else:
            return ERROR.INVALID_LINK


class UserChangePasswordByEmailView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        summary='Изменение пароля по почте',
        request=UserLoginOutputSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=UserLoginOutputSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='uidb64', location=OpenApiParameter.PATH, required=True, type=str),
            OpenApiParameter(name='token', location=OpenApiParameter.PATH, required=True, type=str),
            OpenApiParameter(name='password', description="Новый пароль", location=OpenApiParameter.PATH, required=True,
                             type=str),
        ],
        auth=[]
    )
    def post(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            old_password = user.password
            is_active = user.is_active
            # new_password = request.data.get("password")
            new_password = json.loads(request.body)["password"]
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            return ERROR.USER_DOES_NOT_EXIST
        if user is not None \
                and account_activation_token.check_token(user, token) \
                and is_active:

            same_pass = user.check_password(new_password)
            if same_pass:
                return ERROR.SAME_PASSWORD
            else:
                user.set_password(new_password)
                user.save()
                if hasattr(user, 'auth_token'):
                    user.auth_token.delete()
                token, created = Token.objects.get_or_create(user=user)
                output_serializer = UserLoginOutputSerializer(token)
                return SuccessfulResponse(output_serializer.data)
        else:
            return ERROR.INVALID_LINK


class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary='Изменение пароля из аккаунта',
        request=UserLoginOutputSerializer,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse',
                response=UserLoginOutputSerializer
            ),
        },
        parameters=[
            OpenApiParameter(name='password', description="Новый пароль", location=OpenApiParameter.QUERY, required=True,
                             type=str),
        ]
    )
    def post(self, request):
        try:
            user = User.objects.get(pk=request.user.id)
            old_password = user.password
            # new_password = request.data.get("password")
            new_password = json.loads(request.body)["password"]
        except User.DoesNotExist:
            return ERROR.USER_DOES_NOT_EXIST
        same_pass = user.check_password(new_password)
        if same_pass:
            return ERROR.SAME_PASSWORD
        else:
            user.set_password(new_password)
            user.save()
            if hasattr(user, 'auth_token'):
                user.auth_token.delete()
            token, created = Token.objects.get_or_create(user=user)
            output_serializer = UserLoginOutputSerializer(token)
            return SuccessfulResponse(output_serializer.data)


class ForgotPasswordByEmailView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserForgotPasswordRequestByEmailSerialiser
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser]

    @extend_schema(
        summary='Запрос на смену пароля по почте',
        request=UserForgotPasswordRequestByEmailSerialiser,
        responses={
            200: OpenApiResponse(
                description='SuccessfulResponse'
            ),
        },
        parameters=[
            OpenApiParameter(name='email', description="Почта", location=OpenApiParameter.QUERY, required=True,
                             type=str),
        ],
        auth=[]
    )
    def post(self, request, *args, **kwargs):
        # email = request.data.get("email")
        email = json.loads(request.body)["email"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return ERROR.USER_DOES_NOT_EXIST

        to_email = email
        current_site = get_current_site(request)
        mail_subject = 'Запрос на изменение пароля'
        message = render_to_string('email_pass_template.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'token': account_activation_token.make_token(user),
            'fullname': user.last_name + " " + user.first_name + " " + user.patronymic
        })
        send_mail(mail_subject, message, 'youremail', [to_email])
        return SuccessfulEmailSending()
