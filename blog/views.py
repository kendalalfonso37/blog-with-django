from django.shortcuts import render
from django.views.generic import TemplateView

## Vista Basada en clases
class Index(TemplateView):
	template_name = 'inicio/index.html'

#Vista basada en funciones
def index(request):
	return render(request, 'inicio/index.html')
