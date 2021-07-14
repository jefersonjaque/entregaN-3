from django.shortcuts import render
from core2.models import Marca, Modelo, Usuario
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
# Create your views here.

def login(request):
    return render(request, 'core/loginAdmin.html')


def formM(request):
    if request.session.get('nombre'):
        return render(request,'core/formMarca.html')
    else:
        return HttpResponse('No existe la sesion')

def guardarMarca(request):
    v_idMarca = request.POST.get('idMarca')
    v_nombre = request.POST.get('nombreMarca')

    nuevo=Categoria()
    nuevo.idMarca = v_idMarca
    nuevo.nombreMArca = v_nombre

    Marca.save(nuevo)
    
    return HttpResponse('La Marca ah sido registrada correctamente y su nombre es: ' + v_nombre)



def validarusuario(request):
    try:
        v_email=request.POST.get('email')
        v_password=request.POST.get('password')


        usuario=Usuario.objects.get(password=v_password, email=v_email)

        #crear la sesion y redireccionar
        request.session['nombre']=usuario.nombre
        #return HttpResponse(v_password + ' ' + v_email)
        return redirect('/formM')


    except Exception as e:
        return HttpResponse(e)
        #return redirect('/')

def principal(request):
    #nombre='Diego Rivera'

    if request.session.get('nombre'):
        nom=request.session.get('nombre')
        #return HttpResponse('Existe')
        datos={'nombre':nom}
        return render(request, 'core/formMarca.html', datos)
    else:
        #return HttpResponse('No existe')
        return redirect('/formM')