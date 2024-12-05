from django.shortcuts import render,redirect
from .models import Productos
# Create your views here.

def inicio_Productos(request):
    losproductos=Productos.objects.all()
    return render(request,"gestionarProductos.html",{"misproductos":losproductos})

def registrarProducto(request):
    id_producto=request.POST["txtid_producto"]
    nombre=request.POST["txtnombre"]
    tipo=request.POST["txttipo"]
    precio=request.POST["numprecio"]
    descripcion=request.POST["txtdescripcion"]
    cantidad=request.POST["numcantidad"]

    Productos.objects.create(
        id_producto=id_producto,
        nombre=nombre,
        tipo=tipo,
        precio=precio,
        descripcion=descripcion,
        cantidad=cantidad
    ) # GUARDA EL REGISTRO

    return redirect("inicio_Productos")

def seleccionarProducto(request,id_producto):
    producto=Productos.objects.get(id_producto=id_producto)
    return render(request,"editarproductos.html",{"misproductos":producto})

def editarProducto(request):
    id_producto=request.POST["txtid_producto"]
    nombre=request.POST["txtnombre"]
    tipo=request.POST["txttipo"]
    precio=request.POST["numprecio"]
    descripcion=request.POST["txtdescripcion"]
    cantidad=request.POST["numcantidad"]
    producto=Productos.objects.get(id_producto=id_producto)
    producto.nombre=nombre
    producto.tipo=tipo
    producto.precio=precio
    producto.descripcion=descripcion
    producto.cantidad=cantidad
    producto.save() #guarda registro actualizado
    return redirect("inicio_Productos")

def borrarProducto(request,id_producto):
    producto=Productos.objects.get(id_producto=id_producto)
    producto.delete() #borrar el registro

    return redirect("inicio_Productos")

# Create your views here.
