import RPi.GPIO as GPIO 
from time import sleep 
import concurrent.futures
from rmdx_funtions import RMDX 
from decoder import deco as Deco
import os
from kine import Kine 


# esqueleto base para tercera capa del framework del robot
# ----------------- kinematics funtions ----------
def path_plannig(degrees,speed):
    rmdx = RMDX()
    motors = rmdx.getMotorList()
    kn = Kine()
    start = list()
    pos_final= list()
    steps = 2
    start = [0.0,0.0,0.0,0.0,0.0]
    for degree in degrees:
        angulo_final = degree
        pos_final.append(angulo_final)
    print("objetivo",pos_final)
    pos_aux = pos_final.copy()

    sub_motion = kn.path_plannig(start,pos_final,steps)
    for array in sub_motion:
        send_motion(motors,array,speed)
        # sleep(0.5)
    start=pos_aux
    print("posicion inicial: ", start)




# ------------------ control functions -----------


def control_stop_motor(sensors, motors,states):

    zero_speed = [80.0,-20.0,32.0,-40.0,0.0]
    # send_rotational_motion(motor_list,zero_speed)
    
    

    if (sensors[0] == 1 or sensors[1]  == 1) and states[0] == False:  
        stop_motor(motors[0])
        states[0] = True
    elif (states[0] == True) and (sensors[0] != 1 and sensors[1]  != 1):
        states[0] = False
        send_speed(motors[0],zero_speed[0])


    if (sensors[2] == 1 or sensors[3] == 1) and states[1] == False: 
        stop_motor(motors[1])
        states[1] = True
    elif (states[1] == True) and (sensors[2] != 1 and sensors[1]  != 1):
        states[1] = False
        send_speed(motors[1],zero_speed[1])


    if (sensors[4] == 1 or sensors[5] == 1) and states[2] == False: 
        stop_motor(motors[2])
        states[2] = True
    elif (states[2] == True) and (sensors[4] != 1 and sensors[5]  != 1):
        states[2] = False
        send_speed(motors[2],zero_speed[2])


    if sensors[6] == 1 and states[3] == False: 
        stop_motor(motors[3])
        states[3] = True
    
    
   

def control_set_zero_mode(motor_list):
    send_action_set_zero_motors(motor_list)
    sleep(0.5)
    send_action_reset_motors(motor_list)
    sleep(2)
    send_action_set_zero_motors(motor_list)
    sleep(0.5)
    send_action_reset_motors(motor_list)
            



# -------------------- motor functions ---------- -------------------
def send_speed(motor_id,speed):
    rmdx = RMDX()
    decoi = Deco()
    #obtener la trama del angulo
    # value_input = input("ingrese valor de velocidad: ")
    value = float(speed)  
    data_send = decoi.getDataSpeed(value)
    #inicializar motor
    rmdx.setup()
    # motor_id = 0x141
    res = rmdx.setSpeedClosedLoop(motor_id,data_send)
    os.system('sudo /sbin/ip link set can0 down')

def send_pos_with_speed(motor_id, value, speed):
    # print(f"sending {value} degrees to motor {motor_id} with {speed} rad/s")
    rmdx = RMDX()
    decoi = Deco()
    data_send = decoi.getDataDegreeWhitSpeed(value,speed)
    #inicializar motor
    rmdx.setup()
    #envio del angulo
    res = rmdx.setPositionClosedLoopWithSpeed(motor_id,data_send)
    os.system('sudo /sbin/ip link set can0 down')
    #Leer respuesta de encoder
    res_list = list()
    res_list = decoi.readResponseDataPos(res.data)


def reset_motor(motor_id):
    # print(f"applying reset to motor: {motor_id}")
    rmdx = RMDX()
    rmdx.setup()
    rmdx.resetSystemMotor(motor_id)


def stop_motor(motor_id):
    rmdx = RMDX()
    rmdx.setup()
    rmdx.stopMotor(motor_id)


def off_motor(motor_id):
    print(f"turning motor {motor_id} off")


def get_multi_turn_angle_value(motors):
    rmdx = RMDX()
    decoi = Deco()
    rmdx.setup()
    #motor_id = 0x142
    index = int(input("seleccione un motor (0 al 4): " ))
    motor_id = motors[index]
    encoder = rmdx.getMultiTurnAngle(motor_id)
    res_encoder = decoi.readMultiTurnAngle(encoder.data)
    print("*********************************")
    print("angle_value",res_encoder)

def get_single_turn_angle_value(motors):
    rmdx = RMDX()
    decoi = Deco()
    rmdx.setup()
    #motor_id = 0x142
    index = int(input("seleccione un motor (0 al 4): " ))
    motor_id = motors[index]
    encoder = rmdx.getSingleTurnAngle(motor_id)
    res_encoder = decoi.readSingleTurnAngle(encoder.data)
    print("*********************************")
    print("angle_value",res_encoder)


def set_zero_motor(motor_id):
    # print(f"setting zero to motor: {motor_id}")
    rmdx = RMDX()
    rmdx.setup()    
    res = rmdx.setCurrentEncoderOffset(motor_id)


# ---------------------------- parallel or concurrent functions -------------------

def send_rotational_motion(motors,speeds):
    # print("sending rotational motion ..")
    #listas
    #Tareas en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        movimiento = [] 
        for motor,speed in zip(motors,speeds):
            task = executor.submit(send_speed,motor,speed)
            movimiento.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(movimiento)

def send_motion_to_zero_kine(motors,angulos,speeds):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        movimiento = [] 
        for motor, angulo,speed in zip(motors,angulos,speeds):
            task = executor.submit(send_pos_with_speed,motor,angulo,speed)
            movimiento.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(movimiento)
        
        


def send_motion(motors,angulos,speeds):
    #Tareas en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        movimiento = [] 
        for motor, angulo,speed in zip(motors,angulos,speeds):
            task = executor.submit(send_pos_with_speed,motor,angulo,speed)
            movimiento.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(movimiento)


def send_action_reset_motors(motors):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        action = [] 
        for motor in motors:
            task = executor.submit(reset_motor,motor)
            action.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(action)



def send_action_stop_motors(motors):
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        action = [] 
        for motor in motors:
            task = executor.submit(stop_motor,motor)
            action.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(action)


def send_action_set_zero_motors(motors):
    # print("sending command set zero")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        action = [] 
        for motor in motors:
            task = executor.submit(set_zero_motor,motor)
            action.append(task)
        
        #esperar a quee todas las tareas se completen
        concurrent.futures.wait(action)


# ------------------------------------ Interface --------------------------------
def menu():
    print("********* MENU ***********")
    print("\n")



options = {

}

# --------------------------------------- MAIN ----------------------------------
def going_zero():#if __name__ == '__main__':
      print("APP RUNNING")
      

    # --------------- Raspberry configs --------------------
    # define pines here
      GPIO.setwarnings(False) 
      GPIO.setmode(GPIO.BCM) 
      #Definicion sensores Numero de GPIO
      button_on_of = 15
      f_1 = 17
      f_2 = 7
      f_3 = 21
      f_4 = 20
      f_5 = 19
      f_6 = 13
      f_7 = 12

      #Seteo de pines
      GPIO.setup(button_on_of, GPIO.IN)
      GPIO.setup(f_1, GPIO.IN)
      GPIO.setup(f_2, GPIO.IN) 
      GPIO.setup(f_3, GPIO.IN) 
      GPIO.setup(f_4, GPIO.IN)    
      GPIO.setup(f_5, GPIO.IN)
      GPIO.setup(f_6, GPIO.IN)
      GPIO.setup(f_7, GPIO.IN) 
      # enable set zero rutine
      enable = True

      #Motors id
      rmdx = RMDX()
      motor_list = rmdx.getMotorList()
    #   motor_list = [0x144]
      #speed for set zero rutine
      zero_speed = [80.0,-20.0,32.0,-20.0,0.0] #velocidad minima motor 3 = 30
    #   zero_speed = [0.0,0.0,0.0,0.0,0.0] #velocidad minima motor 3 = 30
      angulos_zero_kine =[-118.0,110.0,-159.0,22.5,0]
      speed_kine=[80.0,120.0,40.0,40.0,40.0]

    #   zero_speed = [15.0]
      
      send_rotational_motion(motor_list,zero_speed)

      #estados iniciales de stop
      state_m0 = False
      state_m1 = False
      state_m2 = False
      state_m3 = False

      states = [state_m0,state_m1,state_m2,state_m3]
      sensor_trama_true=[0,0,0,0,0,0,0]
      sensor_trama_anterior=[0,0,0,0,0,0,0]
      sensor_trama_anterior_anterior=[0,0,0,0,0,0,0]

      while enable:
            # step 1: if sensors equal 1 them set zero motors and reset motors
            # sensor trama
            sensor_trama = [GPIO.input(f_1),GPIO.input(f_2),GPIO.input(f_3),
                            GPIO.input(f_4),GPIO.input(f_5),GPIO.input(f_6),GPIO.input(f_7)]
            

            if sensor_trama == [0,1,0,1,1,0,1]:
                enable = False
                break
            else:
                # print("********SEARCHING ZERO MODE*****")
                print("lectura: ",sensor_trama)
                 # sensor_trama_anterior=sensor_trama

                control_stop_motor(sensor_trama,motor_list,states)
                enable = True
            # step 3: stop motor when associated sensor A equal 1 or sensor B equal 1
            sleep(0.1)
    

      control_set_zero_mode(motor_list)
      sleep(2)
      send_motion_to_zero_kine(motor_list,angulos_zero_kine,speed_kine)
      sleep(5)
      control_set_zero_mode(motor_list)
      sleep(1)
      angulos_zero = [0.1,0.1,0.0,0.0,0.0]
      send_motion(motor_list,angulos_zero,speed_kine) 
      print("Finish set zero")
      
