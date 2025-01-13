from rest_framework import filters
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import PartImageSerializer, PartImage, PartSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from account.api.auth.security import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from ..models import PartImage, Parts


@api_view(["GET"])
@authentication_classes([JWTAuthentication])
@permission_classes([AllowAny])
def parts_home_view(request):
    cars = Parts.objects.all()
    serializer = PartImageSerializer(cars, many=True)
    return Response(serializer.data)


class PartCreateView(generics.CreateAPIView):
    serializer_class = PartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            part_instance = serializer.save()
            part_data = PartSerializer(part_instance).data
            return Response(
                {"message": "part added", "part_data": part_data},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartDetailView(generics.RetrieveAPIView):
    queryset = Parts.objects.all()
    serializer_class = PartSerializer
    lookup_field = "pk"
