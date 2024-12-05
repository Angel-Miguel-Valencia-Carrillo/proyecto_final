from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    fecha_nac=models.DateField(null=False,blank=False)
    direccion=models.CharField(max_length=100)
    telefono=models.PositiveSmallIntegerField()
    horario=models.CharField(max_length=100)
    numsegurosocial=models.CharField(max_length=9)


    def __str__(self):
        return self.nombre