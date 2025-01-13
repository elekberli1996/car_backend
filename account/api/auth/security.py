import jwt, datetime
from django.conf import settings
from .services import jwt_encode, jwt_decode
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


User = get_user_model()


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):

            # Eğer token yoksa veya Bearer ile başlamıyorsa doğrulama yapılmaz
            return None

        token = auth_header.split(" ")[1]

        try:
            payload = jwt_decode(token)
            user = User.objects.get(email=payload["email"])
        except (User.DoesNotExist, ValueError):
            raise AuthenticationFailed("Kimlik doğrulama başarısız")

        return (user, None)  # Django için authenticate metodu bir tuple döndürmelidir
