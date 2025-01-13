from django.contrib.auth import get_user_model
from django.conf import settings
import jwt, datetime


User = get_user_model()


def jwt_encode(user, secret=None, algorithm="HS256", exp_minutes=60):
    if secret is None:
        secret = settings.SECRET_KEY

    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=exp_minutes)

    payload = {
        "username": user.username,
        "email": user.email,  # Kullanıcının email-ni ekliyoruz
        "exp": exp,
    }

    token = jwt.encode(payload, secret, algorithm=algorithm)
    return token


def jwt_decode(token, secret=None, algorithm="HS256"):
    if secret is None:
        secret = settings.SECRET_KEY

    try:
        payload = jwt.decode(token, secret, algorithms=[algorithm])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token süresi dolmuş")
    except jwt.InvalidTokenError:
        raise ValueError("Geçersiz token")


def create_refresh_token(user, secret=None, exp_days=20):
    if secret is None:
        secret = settings.SECRET_KEY

    exp = datetime.datetime.utcnow() + datetime.timedelta(days=exp_days)

    payload = {
        "email": user.email,
        "user_id": user.id,
        "exp": exp,
    }

    refresh_token = jwt.encode(payload, secret, algorithm="HS256")
    return refresh_token
