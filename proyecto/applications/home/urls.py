
from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('stock/', views.Detalle.as_view(), name='Detalle'),
    path('formulario/', views.formulario.as_view(), name='formulario'),
]
