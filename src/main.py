from lib.rmdx_funtions import RMDX 
from Interprete.decoder import deco
import os



def send_pos_with_speed(motor_id):
    #incializar clases
    rmdx = RMDX()
    decoi = deco()
    #obtener la trama del angulo
    value_input = input("ingrese angulo Multi turns: ")
    speed_input = input("ingres velocidad: ")
    speed = float(speed_input)
    value = float(value_input)  
    data_send = decoi.getDataDegreeWhitSpeed(value,speed)
    #inicializar motor
    rmdx.setup()
    # motor_id = 0x141
    #envio del angulo
    res = rmdx.setPositionClosedLoopWithSpeed(motor_id,data_send)
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

def send_pos_multi_turns(motor_id):
    #incializar clases
    rmdx = RMDX()
    decoi = deco()
    #obtener la trama del angulo
    value_input = input("ingrese angulo Multi turns: ")
    value = float(value_input)  
    data_send = decoi.getDataDegree(value)
    #inicializar motor
    rmdx.setup()
    # motor_id = 0x141
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
        


def send_pos(motor_id):
    #incializar clases
    rmdx = RMDX()
    decoi = deco()
    #obtener la trama del angulo
    value_input = input("ingrese angulo Single turns: ")
    value = float(value_input)  
    data_send = decoi.getDataDegree(value)
    #inicializar motor
    rmdx.setup()
    # motor_id = 0x141
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
        


def send_speed(motor_id):
    rmdx = RMDX()
    decoi = deco()
    #obtener la trama del angulo
    value_input = input("ingrese valor de velocidad: ")
    value = float(value_input)  
    data_send = decoi.getDataSpeed(value)
    #inicializar motor
    rmdx.setup()
    # motor_id = 0x141
    #envio del angulo
    res = rmdx.setSpeedClosedLoop(motor_id,data_send)
    os.system('sudo /sbin/ip link set can0 down')

def read_encoder(motor_id):
    os.system('sudo /sbin/ip link set can0 down')
    rmdx = RMDX()
    decoi = deco()
    rmdx.setup()
    # motor_id = 0x141
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

def stop_motor(motor_id):
    os.system('sudo /sbin/ip link set can0 down')
    rmdx = RMDX()
    decoi = deco()
    rmdx.setup()
    # motor_id = 0x141
    rmdx.stopMotor(motor_id)
    #rmdx.offMotor(motor_id)

def off_motor(motor_id):
    os.system('sudo /sbin/ip link set can0 down')
    rmdx = RMDX()
    decoi = deco()
    rmdx.setup()
    # motor_id = 0x141
    rmdx.offMotor(motor_id)
    #rmdx.offMotor(motor_id)

def set_zero_motor(motor_id):
    os.system('sudo /sbin/ip link set can0 down')
    rmdx = RMDX()
    decoi = deco()
    rmdx.setup()
    # motor_id = 0x141
    rmdx.setEncoderOffset(motor_id)
    #rmdx.offMotor(motor_id)

def menu():
    print("1. Enviar Posicion Single Turn")
    print("2. Enviar Posicion Multi Turn")
    print("3. Enviar Velocidad")
    print("4. Leer Posicion")
    print("5. Detener motor")
    print("6. Enviar Posicion con velocidad")
    print("7. Apagar motor")
    print("8. Setear cero")
    

options = {
    "1" : send_pos,
    "2" : send_pos_multi_turns,
    "3" : send_speed,
    "4" : read_encoder,
    "5" : stop_motor,
    "6" : send_pos_with_speed,
    "7" : off_motor,
    "8" : set_zero_motor
}


if __name__ == "__main__":
    rmdx = RMDX()
    motor_list = rmdx.getMotorList()
    print("MOTORES DISPONIBLES: ", motor_list)


    
    

    while True:

        index = int(input("seleccione un motor (0 al 4): " ))
        motor_id = motor_list[index]
        print("El motor seleccionado es: ",motor_id)
        print("\n")
        menu()
        option = input("Seleccione una opcion: ")
        if option == "9":
            break
        action = options.get(option)
        if action:
            action(motor_id)
        else:
            print("Opcion no valida, seleccione una opcion del menu")







