from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product, Photo


class ProductList(ListView):
    model = Product

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name']

    def get_success_url(self):
        # return self.object.get_absolute_url()
        return reverse('app_b:product_list')