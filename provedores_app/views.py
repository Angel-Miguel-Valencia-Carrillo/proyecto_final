from django.shortcuts import render,redirect
from .models import Provedor
# Create your views here.

def inicio_Provedores(request):
    losprovedores=Provedor.objects.all()
    return render(request,"gestionarProvedor.html",{"misprovedores":losprovedores})

def registrarProvedor(request):
    id_provedor=request.POST["txtid_provedor"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    tipo_de_producto=request.POST["txttipoproducto"]
    correo=request.POST["txtcorreo"]
    telefono=request.POST["txttelefono"]
    cant_paquetes=request.POST["numcant_paquetes"]

    Provedor.objects.create(
        id_provedor=id_provedor,
        nombre=nombre,
        tipo_de_producto=tipo_de_producto,
        direccion=direccion,
        correo=correo,
        telefono=telefono,
        cant_paquetes=cant_paquetes
    ) # GUARDA EL REGISTRO

    return redirect("inicio_Provedores")

def seleccionarProvedor(request,id_provedor):
    provedor=Provedor.objects.get(id_provedor=id_provedor)
    return render(request,"editarprovedor.html",{"misprovedores":provedor})

def editarProvedor(request):
    id_provedor=request.POST["txtid_provedor"]
    nombre=request.POST["txtnombre"]
    direccion=request.POST["txtdireccion"]
    tipo_de_producto=request.POST["txttipoproducto"]
    correo=request.POST["txtcorreo"]
    telefono=request.POST["txttelefono"]
    cant_paquetes=request.POST["numcant_paquetes"]

    provedor=Provedor.objects.get(id_provedor=id_provedor)
    provedor.nombre=nombre
    provedor.tipo_de_producto=tipo_de_producto
    provedor.direccion=direccion
    provedor.telefono=telefono
    provedor.correo=correo
    provedor.cant_paquetes=cant_paquetes
    provedor.save() #guarda registro actualizado
    return redirect("inicio_Provedores")

def borrarProvedor(request,id_provedor):
    provedor=Provedor.objects.get(id_provedor=id_provedor)
    provedor.delete() #borrar el registro

    return redirect("inicio_Provedores")

# Create your views here.
