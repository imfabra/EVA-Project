#Prueba paralelismo
import concurrent.futures
from lib.rmdx_funtions import RMDX 
from Interprete.decoder import deco
import os


# ------- Tareas Principales ----------------------------------------------------

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



def stop_motor(motor_id):
    # os.system('sudo /sbin/ip link set can0 down')
    rmdx = RMDX()
    rmdx.setup()
    rmdx.stopMotor(motor_id)
 

def off_motor(motor_id):
    # os.system('sudo /sbin/ip link set can0 down')
    rmdx = RMDX()
    rmdx.setup()
    rmdx.offMotor(motor_id)
  


# ------------------ Tareas Concurrentes -------------------------------

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

def send_action_off_motor(motores):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        action = [] 
        for motor in motores:
            task = executor.submit(off_motor,motor)
            action.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(action)


def send_action_stop_motor(motores):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        action = [] 
        for motor in motores:
            task = executor.submit(stop_motor,motor)
            action.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(action)



# ------------------------ Aplicacion --------------------------------------------- 

def menu():
    print("1. Enviar Posicion Robot")
    print("2. Apagar motores")
    print("3. Detener/Encender motores")

options = {
    "1" : send_motion,
    "2" : send_action_off_motor,
    "3" : send_action_stop_motor
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
        if option == "4":
            break
        action = options.get(option)
        if action:
            action(motores)
        else:
            print("Opcion no valida, seleccione una opcion del menu")


