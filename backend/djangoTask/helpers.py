from rest_framework import exceptions
from rest_framework.response import Response


def SuccessfulResponse(result=None, status=200, code=0):
    return Response(
        {
            'code': code,
            'message': None,
            'result': result
        },
        status=status)


def SuccessfulLevelChanging(result=None, status=200, code=0):
    return Response(
        {
            'code': code,
            'message': 'Your level was changed',
            'level': result
        },
        status=status)


def SuccessfulEmailSending(result=None, status=200, code=0):
    return Response(
        {
            'code': code,
            'message': 'A confirmation letter was sent to email',
            'result': result
        },
        status=status)


class ERROR:
    USER_ON_COURSE_DOES_NOT_EXIST = Response(
        {
            'code': 4041,
            'message': 'User on course does not exist',
            'result': None
        },
        status=404
    )
    COURSE_DOES_NOT_EXIST = Response(
        {
            'code': 4042,
            'message': 'Course does not exist',
            'result': None
        },
        status=404
    )
    USER_DOES_NOT_EXIST = Response(
        {
            'code': 4043,
            'message': 'User does not exist',
            'result': None
        },
        status=404
    )
    LESSON_DOES_NOT_EXIST = Response(
        {
            'code': 4044,
            'message': 'Lesson does not exist',
            'result': None
        },
        status=404
    )
    ANSWER_DOES_NOT_EXIST = Response(
        {
            'code': 4043,
            'message': 'Answer does not exist',
            'result': None
        },
        status=404
    )
    CERTIFICATE_DOES_NOT_EXIST = Response(
        {
            'code': 4044,
            'message': 'Certificate does not exist',
            'result': None
        },
        status=404
    )
    QUESTION_DOES_NOT_EXIST = Response(
        {
            'code': 4045,
            'message': 'Question does not exist',
            'result': None
        },
        status=404
    )
    NO_QUESTIONS_ON_COURSE = Response(
        {
            'code': 4046,
            'message': 'There are no questions on the course',
            'result': None
        },
        status=404
    )
    INVALID_LINK = Response(
        {
            'code': 4047,
            'message': 'Activation link is invalid',
            'result': None
        },
        status=404
    )
    REVIEW_ALREADY_EXISTS = Response(
        {
            'code': 4221,
            'message': 'A review for the course has already been added by this user',
            'result': None
        },
        status=422
    )
    INSUFFICIENT_PROGRESS_FOR_CERTIFICATE = Response(
        {
            'code': 4222,
            'message': 'Course progress of this user is not enough for creating a certificate',
            'result': None
        },
        status=422
    )
    CERTIFICATE_ALREADY_EXISTS = Response(
        {
            'code': 4223,
            'message': 'The certificate already exists',
            'result': None
        },
        status=422
    )
    SAME_PASSWORD = Response(
        {
            'code': 4224,
            'message': 'The new password is the same as the old one',
            'result': None
        },
        status=422
    )
    NOT_VERIFIED_ACCOUNT = Response(
        {
            'code': 4011,
            'message': 'Verify your account by email',
            'result': None
        },
        status=422
    )


class EXCEPTION:
    MISSING_REQUIRED_FIELDS = exceptions.ValidationError(
        'Must provide all required fields.'
    )
    UNABLE_TO_LOGIN = exceptions.ValidationError(
        'Unable to login with given credentials.'
    )
    DEACTIVATED_USER = exceptions.ValidationError(
        'User is deactivated.'
    )
