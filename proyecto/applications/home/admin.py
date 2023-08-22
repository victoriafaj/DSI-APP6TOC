from django.contrib import admin

# Register your models here.
from .models import Articulo
admin.site.register(Articulo)
from .models import Detalle
admin.site.register(Detalle)

