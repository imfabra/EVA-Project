from lib.rmdx_funtions import RMDX 
from Interprete.decoder import deco
import os

def send_pos_multi_turns():
    #incializar clases
    rmdx = RMDX()
    decoi = deco()
    #obtener la trama del angulo
    value_input = input("ingrese angulo: ")
    value = float(value_input)  
    data_send = decoi.getDataDegree(value)
    #inicializar motor
    rmdx.setup()
    motor_id = 0x142
    #envio del angulo
    res = rmdx.setPositionClosedLoopM(motor_id,data_send)
    os.system('sudo /sbin/ip link set can0 down')
    #Leer respuesta de encoder
    res_list = list()
    res_list = decoi.readResponseDataPos(res.data)

    print("******************************")
    print("temp: "+str(res_list[1]))
    print("current: "+str(res_list[2]))
    print("speed: "+str(res_list[3]))
    print("encoder_pos: "+str(res_list[4]))
    print("******************************")
        


def send_pos():
    #incializar clases
    rmdx = RMDX()
    decoi = deco()
    #obtener la trama del angulo
    value_input = input("ingrese angulo: ")
    value = float(value_input)  
    data_send = decoi.getDataDegree(value)
    #inicializar motor
    rmdx.setup()
    motor_id = 0x142
    #envio del angulo
    res = rmdx.setPositionClosedLoop(motor_id,data_send)
    os.system('sudo /sbin/ip link set can0 down')
    #Leer respuesta de encoder
    res_list = list()
    res_list = decoi.readResponseDataPos(res.data)

    print("******************************")
    print("temp: "+str(res_list[1]))
    print("current: "+str(res_list[2]))
    print("speed: "+str(res_list[3]))
    print("encoder_pos: "+str(res_list[4]))
    print("******************************")
        


def send_speed():
    rmdx = RMDX()
    decoi = deco()
    #obtener la trama del angulo
    value_input = input("ingrese valor de velocidad: ")
    value = float(value_input)  
    data_send = decoi.getDataSpeed(value)
    #inicializar motor
    rmdx.setup()
    motor_id = 0x142
    #envio del angulo
    res = rmdx.setSpeedClosedLoop(motor_id,data_send)
    os.system('sudo /sbin/ip link set can0 down')

def read_encoder():
    os.system('sudo /sbin/ip link set can0 down')
    rmdx = RMDX()
    decoi = deco()
    rmdx.setup()
    motor_id = 0x142
    encoder = rmdx.getEncoder(motor_id)
    res_encoder = decoi.readEncoderData(encoder.data)

    print("******************************")
    print("Command ",res_encoder[0])
    print("Encoder Position ",res_encoder[1])
    print("Encoder Original Position ",res_encoder[2])
    print("Encoder offset ",res_encoder[3])
    print("Angulo_m1",res_encoder[4])
    print("Angulo_m2",res_encoder[5])

    print("******************************")

def stop_motor():
    os.system('sudo /sbin/ip link set can0 down')
    rmdx = RMDX()
    decoi = deco()
    rmdx.setup()
    motor_id = 0x142
    rmdx.stopMotor(motor_id)
    rmdx.offMotor(motor_id)

def menu():
    print("1. Enviar Posicion Single Turn")
    print("2. Enviar Posicion Multi Turn")
    print("3. Enviar Velocidad")
    print("4. Leer Posicion")
    print("5. Detener motor")
    

options = {
    "1" : send_pos,
    "2" : send_pos_multi_turns,
    "3" : send_speed,
    "4" : read_encoder,
    "5" : stop_motor
}


if __name__ == "__main__":
    while True:
        menu()
        option = input("Seleccione una opcion: ")
        if option == "6":
            break
        action = options.get(option)
        if action:
            action()
        else:
            print("Opcion no valida, seleccione una opcion del menu")







