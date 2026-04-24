from urllib import request

from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "Account created successfully")
            return redirect("/login")
        else:
            messages.error(response, form.errors)

    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


def login(response):
    if response.method == "POST":
        form = LoginForm(response.POST)
        if form.is_valid():
            messages.success(response, "Account logged in")
            return redirect("/dashboard")
        else:
            messages.error(response, form.errors)
    else:
        form = LoginForm()

    return render(response, "registration/login.html", {"form": form})
