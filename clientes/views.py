from django.shortcuts import render
from .models import *
from .forms import ClientesForm
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy, reverse

# Create your views here.
class Inicio(TemplateView):
    template_name = 'paginas_base/inicio.html'
    
class Nosotros(TemplateView):
    template_name = 'paginas_base/nosotros.html'
    
class Lista(ListView):
    template_name = 'crud/lista.html'
    model = Cliente
    ordering = 'nom'
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'
    
class Crear(CreateView):
    template_name = 'crud/crear.html'
    model = Cliente
    form_class = ClientesForm
    
    def get_success_url(self, **kwargs):
        return reverse("clientes_app:lista")
    
class Editar(UpdateView):
    template_name = 'crud/editar.html'
    model = Cliente
    form_class = ClientesForm
    pk_url_kwarg = 'pk'
    
    def get_success_url(self, **kwargs):
        return reverse("clientes_app:lista")
    
class Eliminar(DeleteView):
    template_name = 'crud/eliminar.html'
    model = Cliente
    pk_url_kwarg = 'pk'
    
    def get_success_url(self, **kwargs):
        return reverse("clientes_app:lista")