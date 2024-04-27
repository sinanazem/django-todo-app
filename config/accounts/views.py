from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd["username"], cd["email"], cd["password"])
            user.first_name = cd["first_name"]
            user.last_name = cd["last_name"]
            user.save()
            messages.success(request, "You Registered Successfully", "success")
            
            return redirect("todo")


    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd["username"], password=cd["password"])

            if user is not None:
                login(request=request, user=user)
                messages.success(request, "You Login Successfully ")

                return redirect("todo")
            
            else:
                messages.success(request, "Username or Password is Wrong", "danger")
                
            
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "You Logged Successfully", "danger")
    return redirect("introduction")
    



# Create your views here.
