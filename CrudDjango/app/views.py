from django.shortcuts import render, redirect
from app.forms import CarrosForm
from app.models import Carros

#Create your views here.
#Pagina inicial
def home(request):
    data = {}
    data['db'] = Carros.objects.all()
    return  render(request,'index.html', data)

#Formulario
def form(request):
    data = {}
    data['form'] = CarrosForm()
    return render(request,'form.html', data)

#Insert
def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():#verifica se o formulario é valido
        form.save() #salva no banco de dados
        return redirect('home')# redireciona para home

#Read
def view(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

#Edit
def edit(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data)

#Update
def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')
#python manage.py runserver = para rodar o servidor