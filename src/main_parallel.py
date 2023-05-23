#Prueba paralelismo
import concurrent.futures
from lib.rmdx_funtions import RMDX 
from Interprete.decoder import deco
import os

def send_pos_with_speed(motor_id,value,speed):
    print(f"Enviando movimiento a {motor_id}: Ángulo {value}, Velocidad {speed}")
    #incializar clases
    rmdx = RMDX()
    decoi = deco()
    data_send = decoi.getDataDegreeWhitSpeed(value,speed)
    #inicializar motor
    rmdx.setup()
    #envio del angulo
    res = rmdx.setPositionClosedLoopWithSpeed(motor_id,data_send)
    os.system('sudo /sbin/ip link set can0 down')
    #Leer respuesta de encoder
    res_list = list()
    res_list = decoi.readResponseDataPos(res.data)

def send_motion(motores):
    #listas
    angulos = list()
    speeds = list()
    #ingresar data
    for motor in motores:
        angulo = int(input("angulo deseado " + str(motor) + ": "))
        angulos.append(angulo)
        speed = int(input("velocidad deseada " + str(motor) + ": "))
        speeds.append(speed)
    
    #Tareas en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        movimiento = [] 
        for motor, angulo,speed in zip(motores,angulos,speeds):
            task = executor.submit(send_pos_with_speed,motor,angulo,speed)
            movimiento.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(movimiento)

def menu():
    print("1. Enviar Posicion Robot")

options = {
    "1" : send_motion,
}


if __name__ == "__main__":
    rmdx = RMDX()
    motor_list = rmdx.getMotorList()
    print("MOTORES DISPONIBLES: ", motor_list)

    while True:
        motores= list()
        index = int(input("seleccione cantidad de motores: " ))
        for motor_id in motor_list[:index]:
            motores.append(motor_id)

        menu()
        option = input("Seleccione una opcion: ")
        if option == "2":
            break
        action = options.get(option)
        if action:
            action(motores)
        else:
            print("Opcion no valida, seleccione una opcion del menu")


