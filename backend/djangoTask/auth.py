from rest_framework.authentication import TokenAuthentication


class CustomTokenAuth(TokenAuthentication):
    keyword = 'Bearer'
