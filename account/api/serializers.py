# serializers.py
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from ..models import CustomUser


class RegisterUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=30, required=True)
    username = serializers.CharField(max_length=30, required=True)
    email = serializers.CharField(max_length=30, required=True)
    phone = serializers.CharField(max_length=15, required=True)
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone",
            "password",
            "password_confirm",
        ]

    def validate(self, data):
        # Şifrelerin eşleşip eşleşmediğini kontrol et
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("The passwords do not match.")

        # Şifre doğrulama işlemi (isteğe bağlı)
        validate_password(data["password"])
        return data

    def create(self, validated_data):
        # `password_confirm` alanını temizle çünkü onu kaydetmeyeceğiz
        validated_data.pop("password_confirm")

        # Kullanıcıyı oluştur
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone=validated_data["phone"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
