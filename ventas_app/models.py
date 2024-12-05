from django.db import models

# Create your models here.
class Venta(models.Model):
    id_venta=models.PositiveIntegerField(primary_key=True)
    id_cliente=models.PositiveIntegerField()
    id_empleado=models.PositiveIntegerField()
    id_producto=models.PositiveIntegerField()
    fecha_venta=models.DateField(null=False,blank=False)
    cant=models.PositiveIntegerField()
    importe_pagar=models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.id_venta