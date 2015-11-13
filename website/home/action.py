__author__ = 'WeiDun'
from django.shortcuts import *
from django.http import HttpResponse
from home.models import User


def login_action(request):
    if "name" and "password" in request.GET:
        request_name = request.GET["name"]
        request_password = request.GET["password"]
        database_user = User.objects.filter(name=request_name)
        if database_user.count() > 0:
            if database_user.first().password == request_password:
                request.session["online"] = 1
                # return HttpResponse("login success")
                return redirect("/")
            else:
                return HttpResponse("error password")
        else:
            return HttpResponse("error user name")


def register_action(request):
    if "name" and "password" and "confirm_password" in request.GET:
        if request.GET["password"] == request.GET["confirm_password"]:
            request_name = request.GET["name"]
            request_password = request.GET["password"]
            if User.objects.filter(name=request_name).count() > 0:
                return HttpResponse("already has this name, please try another one")
            else:
                user = User()
                user.name = request_name
                user.password = request_password
                user.save()
                return HttpResponse("register success<br><a href='/login'>login now</a>")
        else:
            return HttpResponse("the passwords you entered do not match")
    else:
        return HttpResponse("incomplete field")
