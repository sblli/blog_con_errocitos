from django.http import request, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactoForm
from .forms import Publiform, CustomUserCreationForm
from .forms import Otraform, RegisForm, LoginForm
from .forms import comentarioform, uwuform, postisform
from .models import publicacionn, otrapubli, Registro, uwu, postis, comment
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView

@login_required
def index2(request):
    data = {
        'form':postisform(),
        'posts':postis.objects.all()
    }
    if request.method =='POST':
        formulario = postisform(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save(commit=False)
            return redirect(to="index2")
            data["mensaje"]="Publicación Guardado"
        else:
            data["form"]=formulario
    return render (request, 'app/index2.html', data)


def uwus(request):
    publicacion = uwu.objects.all()
    data = {
        'publicacion': publicacion
    }
    return render (request,'app/uwu.html', data)

def index(request):
    return render (request, 'app/index.html')

def service(request):
    return render (request, 'app/service.html')

def team(request):
    data = {
        'form': comentarioform()
    }

    if request.method == 'POST':
        formulario = comentarioform(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]="guardado correctamente"

        else:
            data["form"]=formulario
    return render (request, 'app/team.html', data)

def about(request):
    return render (request, 'app/about.html')

def com(request):
      
    return render (request, 'app/publis/com.html')


def contact(request):
    data = {
        'form': ContactoForm()
    }
      
    if request.method =='POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="contact")
            data["mensaje"]="Contacto Guardado"
        else:
            data["form"]=formulario
    return render (request, 'app/contact.html', data)

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data ["username"], password=formulario.cleaned_data["password1"])
            messages.success(request, "Te has registrado correctamente")
            return redirect (to="index2")
        data["form"]=formulario
    return render (request, 'registration/registro.html', data)


@login_required
def escribir(request):
    data = {
        'form': postisform()
    }
      
    if request.method =='POST':
        formulario = postisform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="escribir")
            data["mensaje"]="Publicación Guardado"
        else:
            data["form"]=formulario
    return render (request, 'app/escribir.html',data)

@login_required
def agregar_producto(request):
    data = {
        'form': Publiform()
    }

    if request.method == 'POST':
        formulario = Publiform(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"agregado correctamente")
            return redirect(to="agregar")
        else:
            data["form"]=formulario

    return render(request,'app/publis/agregar.html',data)

@login_required
def mypubli(request):
    data = {
        'posts':postis.objects.all()
    }
    return render (request, 'app/mypubli.html',data)

def listar(request):
    publicacion = publicacionn.objects.all()
    data = {
        'publicacion':publicacion
    }
    return render (request, 'app/publis/listar.html',data)

@permission_required('app.change_postis')
def modificar(request, id):
    publicacion = get_object_or_404(postis, id=id)
    data = {
        'form': postisform(instance=publicacion)
    }

    if request.method == 'POST':
        formulario = postisform(data=request.POST, instance=publicacion, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"modificado correctamente")
            return redirect(to="mypubli")
        data["form"] = formulario
    return render (request, 'app/publis/modificar.html', data)

def eliminar (request,id):
    publicacion = get_object_or_404(publicacionn, id=id)
    publicacion.delete()
    messages.success(request,"eliminado correctamente")
    return redirect(to="mypubli")

def otrapubli(request):
    return render (request, 'app/otrapubli.html')


def regislis(request):
    registro = Registro.objects.all()
    data = {
        'registro':registro
    }
    return render (request, 'app/regislis.html', data)

@login_required
def modificaar(request, id):
    registro = get_object_or_404(Registro, id=id)
    data = {
        'form': RegisForm(instance=registro)
    }

    if request.method == 'POST':
        formulario = RegisForm(data=request.POST, instance=registro, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="regislis")
        data["form"] = formulario
    return render (request, 'app/usua/modificaar.html', data)

def eliminaar (request,id):
    registro = get_object_or_404(Registro, id=id)
    registro.delete()
    return redirect(to="regislis")

def login(request):
    data = {
        'form': LoginForm()
    }
    return render (request, 'registration/login.html', data)

def perfi(request):
    return render (request, 'app/perfi.html')

def info(request):
    return render (request, 'app/info.html')