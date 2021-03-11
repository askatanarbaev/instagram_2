from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from .models import *
from .forms import CreateProfileForm

model1 = Car.objects.all()
model2 = Notebook.objects.all()
model3 = Smartphone.objects.all()
all_model = [model1, model2, model3]


def post_list(request):
    all_models = all_model
    model4 = Category.objects.all()
    return render(request, "base.html", locals())

class NotebookDetailView(DetailView):
    model = Notebook
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class CarDetailView(DetailView):
    model = Car
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class SmartphoneDetailView(DetailView):
    model = Smartphone
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class NewProfileView(CreateView, LoginRequiredMixin):
    model = Profile
    template_name = 'create_profile.html'
    form_class = CreateProfileForm
    context_object_name = 'new_profile'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user = self.request.user
        user.save()
        return redirect('home')


@login_required
def my_profile(request):
    p = request.user.profile
    all_models = all_model
    return render(request, "profile.html", locals())


@login_required
def edit_profile(request):
    if request.method == 'POST':
        p_form = CreateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            return redirect('my_profile')
    else:
        p_form = CreateProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': p_form})



class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'


def my_profile(request):
    p = request.user.profile
    all_models = all_model
    return render(request, "profile.html", locals())
