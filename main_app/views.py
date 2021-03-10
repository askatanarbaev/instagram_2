from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, DetailView
from .models import *

model1 = Car.objects.all()
model2 = Notebook.objects.all()
model3 = Smartphone.objects.all()
all_model = [model1, model2, model3]


def post_list(request):
    all_models = all_model
    model4 = Category.objects.all()
    return render(request, "base.html", locals())


# def post_detail(request, slug):
#     car = get_object_or_404(Car, slug=slug)
#     notebook = get_object_or_404(Notebook, slug=slug)
#     smartphone = get_object_or_404(Smartphone, slug=slug)
#     return render(request, 'product_detail.html', locals())


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


