from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from home.models import User
# Create your views here.
def home(request):
    if request.session.get("online") == 1:
        return render_to_response(template_name="home.html")
    else:
        return redirect("/login")


def login(request):
    return render_to_response(template_name="login.html")


def register(request):
    return render_to_response(template_name="register.html")
