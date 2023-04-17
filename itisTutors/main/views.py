from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


def index(request):
    return render(request, "main/index.html")


def forum(request):
    return render(request, "main/forum.html")


def storage(request):
    return render(request, "main/storage.html")

def tutorsAbout(request):
    return render(request, "main/tutorsAbout.html")

def MyProfile(request):
    return render(request, "main/MyProfile.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"