from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from panel.models import Oficina, Asociado, Aporte

# Create your views here.
class OficinaListView(ListView):
    model = Oficina

class OficinaDetailView(DetailView):
    model = Oficina

class AsociadosListView(ListView):
    model = Asociado

class AsociadosDetailView(DetailView):
    model = Asociado
class AporteListView(ListView):
    model = Aporte

class AporteDetailView(DetailView):
    model = Aporte

class AsociadosUpdate(UpdateView):
    model = Asociado
    fields = '__all__' 

class AsociadosCreate(CreateView):
    model = Asociado
    fields = '__all__'

class AsociadosDelete(DeleteView):
    model = Asociado
    success_url = reverse_lazy('asociados-list')

class OficinaUpdate(UpdateView):
    model = Oficina
    fields = '__all__' 

class OficinaCreate(CreateView):
    model = Oficina
    fields = '__all__'

class OficinaDelete(DeleteView):
    model = Oficina
    success_url = reverse_lazy('oficina-list')
class AporteUpdate(UpdateView):
    model = Aporte
    fields = '__all__' 

class AporteCreate(CreateView):
    model = Aporte
    fields = '__all__'

class AporteDelete(DeleteView):
    model = Aporte
    success_url = reverse_lazy('aporte-list')