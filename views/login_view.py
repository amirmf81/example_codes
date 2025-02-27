from django.shortcuts import render
from api.login_api.login import login_handler


def login_view_func(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    return login_handler(username=username, password=password)
