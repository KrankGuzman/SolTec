from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.organizacion.forms import AlmacenForm
from apps.organizacion.models import Almacen

# Create your views here.

def index(request):
    return render(request,'organizacion/index.html')

def almacen_view(request):
    if request.method == 'POST':
        form = AlmacenForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form = AlmacenForm()
        return render(request, 'organizacion/almacen_form.html', {'form':form})

def almacen_list(request):
    almacen = Almacen.objects.all().order_by('almacen_id')
    contexto = {'almacen':almacen}
    return render(request, 'organizacion/almacen_list.html', contexto)

def almacen_edit(request, almacen_id):
    almacen = Almacen.objects.get(almacen_id=almacen_id)
    if request.method == 'GET':
        form = AlmacenForm(instance=almacen)
    else:
        form = AlmacenForm(request.POST, instance=almacen)
        if form.is_valid():
            form.save()
        return redirect(almacen_list)
    return render(request, 'organizacion/almacen_form.html',{'form':form})

def almacen_delete(request, almacen_id):
    almacen = Almacen.objects.get(almacen_id=almacen_id)
    if request.method == 'POST':
        almacen.delete()
        return redirect(almacen_list)
    return render(request, 'organizacion/almacen_delete.html',{'almacen':almacen})

class AlmacenList(ListView):
    model = Almacen
    template_name = 'organizacion/almacen_list.html'

class AlmacenCreate(CreateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'organizacion/almacen_form.html'
    success_url = reverse_lazy('almacen_listar')

class AlmacenUpdate(UpdateView):
    model = Almacen
    form_class = AlmacenForm
    template_name = 'organizacion/almacen_form.html'
    success_url = reverse_lazy('almacen_listar')

class AlmacenDelete(DeleteView):
    model = Almacen
    template_name = 'organizacion/almacen_delete.html'
    success_url = reverse_lazy('almacen_listar')