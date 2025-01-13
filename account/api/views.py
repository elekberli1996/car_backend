# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterUserSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema
from account.api.auth.services import *
from rest_framework.exceptions import AuthenticationFailed
from drf_yasg import openapi
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from ..models import BlacklistedToken


# @swagger_auto_schema(request_body=RegisterUserSerializer, methods=["post"], security=[])


@api_view(["POST"])
def register_user(request):
    serializer = RegisterUserSerializer(data=request.data)
    if request.method == "POST":
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User created successfully",
                    "user": RegisterUserSerializer(user).data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)

    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email ve şifre gereklidir"}, status=400)

    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            raise AuthenticationFailed("Geçersiz şifre veya email adresi")
    except User.DoesNotExist:
        raise AuthenticationFailed("Geçersiz sifre veya email adresi")

    # JWT access token oluştur
    access_token = jwt_encode(user)

    # Refresh token oluştur
    refresh_token = create_refresh_token(user)

    return Response(
        {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def refresh_token_view(request):
    refresh_token = request.data.get("refresh_token")

    if not refresh_token:
        raise AuthenticationFailed("Refresh token gerekli")

    try:
        # Refresh token'ı çöz
        payload = jwt_decode(refresh_token)
        user = User.objects.get(email=payload["email"])
    except (User.DoesNotExist, ValueError):
        raise AuthenticationFailed("Geçersiz refresh token veya kullanıcı bulunamadı")

    # Yeni access token oluştur
    access_token = jwt_encode(user)

    return Response({"access_token": access_token}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_user(request):
    refresh_token = request.data.get("refresh_token")

    if not refresh_token:
        return Response(
            {"error": "Refresh token gereklidir"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        payload = jwt_decode(refresh_token)
        user = request.user
        BlacklistedToken.objects.create(user=user, token=refresh_token)
    except ValueError:
        return Response({"error": "Geçersiz token"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Başarıyla çıkış yapıldı"}, status=status.HTTP_200_OK)
