from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy 
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from album.models import Oficinas, Asociado, Aportes

# Create your views here.
class OficinasListView(ListView):
    model = Oficinas

class OficinasDetailView(DetailView):
    model = Oficinas

class AsociadosListView(ListView):
    model = Asociado

class AsociadosDetailView(DetailView):
    model = Asociado
class AportesListView(ListView):
    model = Aportes

class AportesDetailView(DetailView):
    model = Aportes

class AsociadosUpdate(UpdateView):
    model = Asociado
    fields = '__all__' 

class AsociadosCreate(CreateView):
    model = Asociado
    fields = '__all__'

class AsociadosDelete(DeleteView):
    model = Asociado
    success_url = reverse_lazy('asociados-list')

class OficinasUpdate(UpdateView):
    model = Oficinas
    fields = '__all__' 

class OficinasCreate(CreateView):
    model = Oficinas
    fields = '__all__'

class OficinasDelete(DeleteView):
    model = Oficinas
    success_url = reverse_lazy('oficinas-list')
class AportesUpdate(UpdateView):
    model = Aportes
    fields = '__all__' 

class AportesCreate(CreateView):
    model = Aportes
    fields = '__all__'

class AportesDelete(DeleteView):
    model = Aportes
    success_url = reverse_lazy('aportes-list')