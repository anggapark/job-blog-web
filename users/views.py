from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.urls import reverse

# from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def register(request):
    # redirect a user to the home page if he is already logged in
    # if request.user.is_authenticated:
    #     return redirect("jobblog:home")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # display a nice message when a new user is registered
            messages.success(request, "Congratulations, you are now a registered user!")
            return redirect("jobblog:home")
    else:
        form = SignUpForm()
    return render(request, "users/register.html", {"form": form})


def log_in(request):
    # if request.user.is_authenticated:
    #     return redirect("core:home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # We check if the data is correct
            user = authenticate(username=username, password=password)
            if user:  # If the returned object is not None
                login(request, user)  # we connect the user
                return redirect("jobblog:home")
            else:  # otherwise an error will be displayed
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("users:login"))
