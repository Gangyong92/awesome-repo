import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions
from users.models import User


class JWTAuthentication(authentication.BaseAuthentication):

    """ JWT Decoding """

    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")
            if token is None:
                return None
            # split는 그냥 문자열 분리임. Token을 제대로 보내지 않은 경우 를 대비해서 try 넣음
            xjwt, jwt_token = token.split(" ")
            decoded = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
            pk = decoded.get("pk")
            user = User.objects.get(pk=pk)
            return (user, None)
        except (ValueError, User.DoesNotExist):
            return None
        except jwt.exceptions.DecodeError:
            # decode에서 비정상 token이 입력 된 경우. Not enough segments 에러 띄움
            # None 해도 되고 이런 식으로 메시지를 띄워도 되고
            raise exceptions.AuthenticationFailed(detail="JWT Format Invalid")