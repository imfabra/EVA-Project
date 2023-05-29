#Aplicación de control para el robot 
import RPi.GPIO as gpio           # Importa libreria de I/O (entradas / salidas)
import tkinter as tk            # Importa la libreria grafica (GUI)  
from tkinter import ttk


#Setear Pines
gpio.setmode(gpio.BCM)
pin = 7
gpio.setup(pin,gpio.IN)

pin_value= gpio.input(pin)
print("Valor del pin: ", pin_value)