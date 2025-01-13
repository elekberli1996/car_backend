from django.shortcuts import render


# Create your views here.
def login_view(request):
    pass


def register_view(request):
    pass


def auth_view(request):
    return render(request, "login_register_page.html")
