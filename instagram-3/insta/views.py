from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    all_images = PostImage.objects.all()
    all_users = Profile.objects.all()
    return render(request, 'home.html', locals())


# def profile_acc(request, pk):
#     profile = get_object_or_404(Profile, pk=pk)
#     return render(request, 'profile.html')


class ProfileAccountView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'


