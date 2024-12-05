from django.db import models

# Create your models here.
class Provedor(models.Model):
    id_provedor=models.PositiveIntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    tipo_de_producto=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.PositiveSmallIntegerField()
    correo=models.EmailField(max_length=100)
    cant_paquetes=models.PositiveIntegerField()


    def __str__(self):
        return self.id_provedor