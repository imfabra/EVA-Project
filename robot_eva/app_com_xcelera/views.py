from django.shortcuts import render, get_object_or_404, redirect
from robot_eva.app_crud.models import *
from robot_eva.app_crud.forms import *

# Create your views here.
# def motion_robot_details(request):
#     if request.method == 'POST':
# la idea aqui es hacer la siguiente sentencia:
# SELECT  Movimientos.idEtiqueta, Etiquetas.nombre,Movimientos.idMovimiento,
# Submovimientos.join1, Submovimientos.join2, Submovimientos.join3, Submovimientos.join4, Submovimientos.join5, Submovimientos.velocidad,
# Submovimientos.tiempo, Submovimientos.orden, Movimientos.descripcion
# FROM Movimientos
# INNER JOIN Etiquetas ON Movimientos.idEtiqueta = Etiquetas.idEtiqueta
# INNER JOIN Submovimientos ON Movimientos.idMovimiento = Submovimientos.idMovimiento;

