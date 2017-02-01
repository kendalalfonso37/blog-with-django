from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Articulo

# Create your views here.
class EntradaListView(ListView):
	model = Articulo
	template_name = 'entrada/index.html'

class EntradaDetailView(DetailView):
	model = Articulo	
	template_name = 'entrada/detalle.html'
	
