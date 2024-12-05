from django.shortcuts import render,redirect
from .models import Cliente
# Create your views here.

def inicio_Clientes(request):
    losclientes=Cliente.objects.all()
    return render(request,"gestionarCliente.html",{"misclientes":losclientes})

def registrarCliente(request):
    id_cliente=request.POST["txtid_cliente"]
    nombre=request.POST["txtnombre"]
    fecha_nac=request.POST["txtfecha_nac"]
    direccion=request.POST["txtdireccion"]
    correo=request.POST["txtcorreo"]
    telefono=request.POST["numtelefono"]


    Cliente.objects.create(
        id_cliente=id_cliente,
        nombre=nombre,
        fecha_nac=fecha_nac,
        direccion=direccion,
        correo=correo,
        telefono=telefono
    ) # GUARDA EL REGISTRO
    return redirect("inicio_Clientes")

def seleccionarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    fecha_nac=cliente.fecha_nac.strftime('%y-%m-%d')
    return render(request,"editarcliente.html",{"misclientes":cliente,"fecha_nac":fecha_nac})

def editarCliente(request):
    id_cliente=request.POST["txtid_cliente"]
    nombre=request.POST["txtnombre"]
    fecha_nac=request.POST["txtfecha_nac"]
    direccion=request.POST["txtdireccion"]
    correo=request.POST["txtcorreo"]
    telefono=request.POST["numtelefono"]
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombre=nombre
    cliente.fecha_nac=fecha_nac
    cliente.direccion=direccion
    cliente.telefono=telefono
    cliente.correo=correo
    cliente.save() #guarda registro actualizado
    return redirect("inicio_Clientes")

def borrarCliente(request,id_cliente):
    cliente=Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete() #borrar el registro

    return redirect("inicio_Clientes")
# Create your views here.
