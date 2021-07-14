from django.shortcuts import render
from core2.models import Marca, Modelo, Usuario
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from django.core.files.storage import FileSystemStorage
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

    nuevo=Marca()
    nuevo.idMarca = v_idMarca
    nuevo.nombreMarca = v_nombre

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
    

    if request.session.get('nombre'):
        nom=request.session.get('nombre')
        #return HttpResponse('Existe')
        datos={'nombre':nom}
        return render(request, 'core/formMarca.html', datos)
    else:
        #return HttpResponse('No existe')
        return redirect('/formM')

    
def formMO(request):
    if request.session.get('nombre'):
        marca = Marca.objects.all()
        datos = {'marcas': marca}
        return render(request, 'core/formModelo.html', datos)
    else:
        return HttpResponse('No existe la sesion')

def guardarModelo(request):
    v_idModelo=request.POST.get('idModelo')
    v_nombreModelo=request.POST.get('nombreModelo')
    v_patente=request.POST.get('patente')
    v_marca=request.POST.get('marca')

    
    v_imagen=request.FILES.get('imagen')
    fs = FileSystemStorage()
    file = fs.save(v_imagen.name, v_imagen)

    
    
    marca=Marca.objects.get(idMarca=v_marca)


    nuevo=Modelo()
    nuevo.idModelo=v_idModelo
    nuevo.nombreModelo=v_nombreModelo
    nuevo.patente=v_patente
    nuevo.imagen=file
    nuevo.marca=marca

    Modelo.save(nuevo)

    return redirect('/verAutos')
    #return HttpResponse(file)

def verAutos(request):
    if request.session.get('nombre'):
        modelos = Modelo.objects.all()
        datos = {'modelos': modelos}
        return render(request, 'core/verAutos.html', datos)
    else:
        return HttpResponse('No existe la sesion')

def eliminarModelo(request, xxx):
   modelo=Modelo.objects.get(idModelo=xxx)
   Modelo.delete(modelo)
   return redirect('/verAutos')

def modificarModelo(request, xxx):
   modelo=Modelo.objects.get(idModelo=xxx)
   marca=Marca.objects.all()
   contexto={'datos':modelo,'marcas': marca}
   return render(request, 'core/formModificarmodelo.html', contexto)

def guardarModificarModelo(request):
    try:
       v_idModelo=request.POST.get('idModelo')
       v_nombreModelo=request.POST.get('nombreModelo')
       v_patente=request.POST.get('patente')
       v_marca=request.POST.get('marca')
       v_imagen=request.POST.get('imagen')
       #busca la marca por ID
       marca=Marca.objects.get(idMarca=v_marca)

       #buscar el modelo a modificar
       modelo=Modelo.objects.get(idModelo=v_idModelo)

       #rescata el objeto imagen del formulario
       v_imagen=request.FILES.get('imagen')
       fs = FileSystemStorage()
       file = fs.save(v_imagen.name, v_imagen)

       modelo.nombreModelo=v_nombreModelo
       modelo.patente=v_patente
       modelo.imagen=file
       modelo.marca=marca
    
        
       Modelo.save(modelo)
       return redirect('/verAutos')
       #return HttpResponse('Exito')
    except Exception as e:
       return HttpResponse(e)
