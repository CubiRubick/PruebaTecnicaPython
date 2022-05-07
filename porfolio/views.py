from django import views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import cliente

# Create your views here.
class porfolioDash(TemplateView):
    template_name = 'cliente_dash.html'

        

class porfolioList(ListView):
    model = cliente

class porfolioDetail(DetailView):
    model = cliente

class porfolioCreated(CreateView):
    model = cliente
    success_url = reverse_lazy('porfolio:dash')
    fields = ['nombre', 'email', 'numeroT', 'descripcion']

class porfolioUpdate(UpdateView):
    model = cliente
    success_url = reverse_lazy('porfolio:list')
    fields = ['nombre', 'email', 'numeroT', 'descripcion']

class porfolioDetele(DeleteView):
    model = cliente
    success_url = reverse_lazy('porfolio:list')