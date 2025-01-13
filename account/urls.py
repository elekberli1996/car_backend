from django.urls import path
from .views import login_view, register_view, auth_view

urlpatterns = [
    path("auth/", auth_view, name="auth_view"),
    # path("login/", login_view, name="login_view"),
    # path("register/", register_view, name="register_view"),
]
