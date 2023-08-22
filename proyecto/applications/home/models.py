from django.db import models
from importlib.util import module_from_spec


class Articulo(models.Model):
    nombre=models.CharField('Catalogo',max_length=50)
    def __str__(self):
        return str(self.nombre)
    
class Detalle(models.Model):
    id=models.IntegerField('id',primary_key='True')         
    tipo=models.ForeignKey(Articulo,on_delete=models.CASCADE)
    fecha=models.DateField('fecha',auto_now_add=True)
    cantidad=models.IntegerField('cantidad')
    observacion=models.CharField('observacion',max_length=50)
    def __str__(self):
        return str(self.id)+' - '+str(self.tipo)+' - '+str(self.fecha)+' - '+str(self.cantidad)+' - '+str(self.observacion)
