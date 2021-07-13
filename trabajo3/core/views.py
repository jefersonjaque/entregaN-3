from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/index.html')

def cajas(request):
    return render(request,'core/cajas.html')
    
def electronica(request):
    return render(request,'core/electronica.html')

def suspension(request):
    return render(request,'core/suspension.html')