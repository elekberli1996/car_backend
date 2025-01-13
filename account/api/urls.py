from django.urls import path
from .views import register_user, login_view, create_refresh_token, logout_user

# api/auth/login
# api/auth/logout
# api/auth/register
# api/auth/refresh-token

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("refresh-token/", create_refresh_token, name="refresh-token"),
]
