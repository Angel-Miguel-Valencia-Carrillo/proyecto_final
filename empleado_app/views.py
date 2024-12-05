from django.shortcuts import render,redirect
from .models import Empleado
# Create your views here.

def inicio_Empleados(request):
    losempleados=Empleado.objects.all()
    return render(request,"gestionarEmpleado.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre=request.POST["txtnombre"]
    fecha_nac=request.POST["txtfecha_nac"]
    direccion=request.POST["txtdireccion"]
    horario=request.POST["txthorario"]
    telefono=request.POST["numtelefono"]
    numsegurosocial=request.POST["txtsegurosocial"]

    Empleado.objects.create(
        id_empleado=id_empleado,
        nombre=nombre,
        fecha_nac=fecha_nac,
        direccion=direccion,
        horario=horario,
        telefono=telefono,
        numsegurosocial=numsegurosocial
    ) # GUARDA EL REGISTRO

    return redirect("inicio_Empleados")

def seleccionarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    fecha_nac=empleado.fecha_nac.strftime('%y-%m-%d')
    return render(request,"editarempleado.html",{"misempleados":empleado,"fecha_nac":fecha_nac})

def editarEmpleado(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre=request.POST["txtnombre"]
    fecha_nac=request.POST["txtfecha_nac"]
    direccion=request.POST["txtdireccion"]
    horario=request.POST["txthorario"]
    telefono=request.POST["numtelefono"]
    numsegurosocial=request.POST["txtsegurosocial"]
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre=nombre
    empleado.fecha_nac=fecha_nac
    empleado.direccion=direccion
    empleado.telefono=telefono
    empleado.horario=horario
    empleado.numsegurosocial=numsegurosocial
    empleado.save() #guarda registro actualizado
    return redirect("inicio_Empleados")

def borrarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete() #borrar el registro

    return redirect("inicio_Empleados")

# Create your views here.
