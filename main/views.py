from http.client import responses

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



from .models import Tolist,User
# from .forms import CreateForm, LoginForm


def index(response):
    # ls = Tolist.objects.get(name="Users")
    # user=ls.user_set.get(id=id)
    return render(response, "main/registration.html")

def dashboard(response):
    return render(response, "main/dashboard.html")


def logout(response):
        return redirect("/login")
#
# def login_user(response):
#     if response.method == "POST":
#         form = LoginForm()
#
#         if form.is_valid():
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]
#
#             # if user is not None:
#             #     registration(request,user)
#             #     print("ddddd")
#             #     messages.success(request,'Hellow, Successfully Logged In')
#             #
#             #     next_url = request.GET.get('next')
#             #     if next_url:
#             #         return redirect(next_url)
#             #     return redirect('dashboard')
#             # else:
#             #  messages.error(request,'username or password is incorrect')
#         else:
#             messages.error(response,'invalid credentials')
#     else:
#         form = LoginForm()
#
#     return render(response, 'main/registration.html',{"form":form})
#
# @login_required
# def dashboard(request):
#     context = {
#         'username':request.user.username,
#         'email':request.user.email,
#         'gender':request.user.gender,
#     }
#     return render(request, 'main/dashboard.html',context)
#
#
