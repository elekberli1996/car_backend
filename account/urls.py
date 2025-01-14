from django.urls import path
from .views import login_view, register_view, auth_view, logout_view

urlpatterns = [
    path("", auth_view, name="auth_view"),
    #
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]
