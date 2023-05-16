from lib.rmdx_funtions import RMDX 
from Interprete.decoder import deco
import os


def send_pos():
    value_input = input("ingrese angulo: ")

def send_speed():
    value_input = input("ingrese velcidad: ")

def read_encoder():
    os.system('sudo /sbin/ip link set can0 down')

def menu():
    print("1. Enviar Posicion")
    print("2. Enviar Velocidad")
    print("3. Leer Posicion")

options = {
    "1" : send_pos,
    "2" : send_speed,
    "3" : read_encoder
}

if __name__ == "__main__":
    while True:
        menu()
        option = input("Seleccione una opcion: ")
        if option == "4":
            break
        action = options.get(option)
        if action:
            action()
        else:
            print("Opcion no valida, seleccione una opcion del menu")







