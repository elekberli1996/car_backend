# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterUserSerializer
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(request_body=RegisterUserSerializer, methods=["post"], security=[])
@api_view(["POST"])
def register_user(request):
    """
    Kullanıcı kaydı için POST isteği.
    """
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


# class LoginUserView(CreateAPIView):
#     serializer_class = RegisterUserSerializer

#     pass
