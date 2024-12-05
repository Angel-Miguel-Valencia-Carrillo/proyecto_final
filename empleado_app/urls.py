from django.urls import path
from empleado_app import views
urlpatterns = [
    path("inicio_Empleados",views.inicio_Empleados, name="inicio_Empleados"),
    path("registrarEmpleado/",views.registrarEmpleado,name="registrarEmpleado"),
    path("seleccionarEmpleado/<id_empleado>",views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path("editarEmpleado/",views.editarEmpleado,name="editarEmpleado"),
    path("borrarEmpleado/<id_empleado>",views.borrarEmpleado,name="borrarEmpleado")
]
