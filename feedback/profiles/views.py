from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import UserProfile


def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "/profiles"


class ProfileViews(ListView):
    template_name = "profiles/user_profiles.html"
    model = UserProfile
    context_object_name = "profiles"