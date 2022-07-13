from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from djangoTask.helpers import EXCEPTION, ERROR
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', '%d.%m.%Y', 'iso-8601'],required=False)
    photo = serializers.ImageField(use_url=True,required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'first_name',
            'last_name',
            'patronymic',
            'birth_date',
            'social_networks',
            'platform',
            'photo',
            'city'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            "birth_date": {"required": False, "allow_null": True},
            "photo": {"required": False, "allow_null": True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserForgotPasswordSerialiser(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            'email',
            'password'
        ]


class UserForgotPasswordRequestByEmailSerialiser(serializers.Serializer):
    class Meta:
        model = User
        fields = [
            'email'
        ]


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")

        if email and password:
            try:
                user = authenticate(email=email, password=password)
            except User.DoesNotExist:
                return ERROR.USER_DOES_NOT_EXIST
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    raise EXCEPTION.DEACTIVATED_USER
            else:
                raise EXCEPTION.UNABLE_TO_LOGIN
        else:
            raise EXCEPTION.MISSING_REQUIRED_FIELDS
        return data


class UserLoginOutputSerializer(serializers.Serializer):
    key = serializers.CharField()

    def token_output(self, data):
        key = data.get("key","")
        if key:
            return key
