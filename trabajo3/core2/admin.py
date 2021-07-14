from django.contrib import admin
from core2.models import Marca
from core2.models import Modelo
from core2.models import Usuario

# Register your models here.
class MarcaAdmin(admin.ModelAdmin):
    list_display=("nombreMarca",)
    search_fields=("nombreMarca",)

class ModeloAdmin(admin.ModelAdmin):
    list_display=("nombreModelo", "patente")
    search_fields=("nombreModelo",)

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("email",)
    search_fields=("email",)


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(Usuario, UsuarioAdmin )