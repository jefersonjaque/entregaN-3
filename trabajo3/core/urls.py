from django.urls import path
from .views import home,cajas,electronica,suspension

urlpatterns = [
    path('',home,name="home"),
    path('cajas/',cajas,name="cajas"),
    path('electronica/',electronica,name="electronica"),
    path('suspension/',suspension,name="suspension")
]
