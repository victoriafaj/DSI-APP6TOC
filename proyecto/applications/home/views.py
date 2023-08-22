from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Detalle

class Detalle(ListView):
    template_name ="stock.html"
    model=Detalle
    context_object_name="stock"

class formulario(CreateView):
    template_name='formulario.html'
    model=Detalle
    fields=['tipo','cantidad','observacion']
    context_object_name="formulario"
    success_url="."

    


