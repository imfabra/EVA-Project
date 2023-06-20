# Aplicación de control para el robot
import RPi.GPIO as GPIO
from time import sleep
import concurrent.futures
from .rmdx_funtions import RMDX
from .decoder import Deco
import os
from .kine import Kine


# ----------------- kinematics functions ----------
class Robot:

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        # Definicion sensores Numero de GPIO
        self.button_on_of = 15
        self.f_1 = 17
        self.f_2 = 7
        self.f_3 = 21
        self.f_4 = 20
        self.f_5 = 19
        self.f_6 = 13
        self.f_7 = 12
        # Seteo de pines
        GPIO.setup(self.button_on_of, GPIO.IN)
        GPIO.setup(self.f_1, GPIO.IN)
        GPIO.setup(self.f_2, GPIO.IN)
        GPIO.setup(self.f_3, GPIO.IN)
        GPIO.setup(self.f_4, GPIO.IN)
        GPIO.setup(self.f_5, GPIO.IN)
        GPIO.setup(self.f_6, GPIO.IN)
        GPIO.setup(self.f_7, GPIO.IN)

        # Motors id
        self.rmdx = RMDX()
        self.decoi = Deco()
        self.motor_list = self.rmdx.getMotorList()
        # estados iniciales de stop
        state_m0 = False
        state_m1 = False
        state_m2 = False
        state_m3 = False
        self.states = [state_m0, state_m1, state_m2, state_m3]

    def path_plannig(self, motors, speed):
        kn = Kine()
        pos_final = list()
        steps = 2
        start = [0.0, 0.0, 0.0, 0.0, 0.0]
        for motor in motors:
            angulo_final = float(input(f"angulo final {motor} : "))
            pos_final.append(angulo_final)
        print("objetivo", pos_final)
        pos_aux = pos_final.copy()

        sub_motion = kn.path_plannig(start, pos_final, steps)
        for array in sub_motion:
            self.send_motion(motors, array, speed)
            # sleep(0.5)
        start = pos_aux
        print("posicion inicial: ", start)

    # ------------------ control functions -----------

    def control_stop_motor(self, sensors):

        motors = self.motor_list
        states = self.states
        zero_speed = [80.0, -20.0, 32.0, -40.0, 0.0]
        # send_rotational_motion(motor_list,zero_speed)
        if (sensors[0] == 1 or sensors[1] == 1) and states[0] == False:
            self.stop_motor(motors[0])
            states[0] = True
        elif (states[0] == True) and (sensors[0] != 1 and sensors[1] != 1):
            states[0] = False
            self.send_speed(motors[0], zero_speed[0])
        if (sensors[2] == 1 or sensors[3] == 1) and states[1] == False:
            self.stop_motor(motors[1])
            states[1] = True
        elif (states[1] == True) and (sensors[2] != 1 and sensors[1] != 1):
            states[1] = False
            self.send_speed(motors[1], zero_speed[1])
        if (sensors[4] == 1 or sensors[5] == 1) and states[2] == False:
            self.stop_motor(motors[2])
            states[2] = True
        elif (states[2] == True) and (sensors[4] != 1 and sensors[5] != 1):
            states[2] = False
            self.send_speed(motors[2], zero_speed[2])
        if sensors[6] == 1 and states[3] == False:
            self.stop_motor(motors[3])
            states[3] = True

    def control_set_zero_mode(self):
        motor_list = self.motor_list
        self.send_action_set_zero_motors(motor_list)
        sleep(0.5)
        self.send_action_reset_motors(motor_list)
        sleep(2)
        self.send_action_set_zero_motors(motor_list)
        sleep(0.5)
        self.send_action_reset_motors(motor_list)

    # -------------------- motor functions ---------- -------------------
    def send_speed(self, motor_id, speed):
        value = float(speed)
        data_send = self.decoi.getDataSpeed(value)
        # inicializar motor
        self.rmdx.setup()
        # motor_id = 0x141
        res = self.rmdx.setSpeedClosedLoop(motor_id, data_send)
        os.system('sudo /sbin/ip link set can0 down')

    def send_pos_with_speed(self, motor_id, value, speed):
        # print(f"sending {value} degrees to motor {motor_id} with {speed} rad/s")
        data_send = self.decoi.getDataDegreeWhitSpeed(value, speed)
        # inicializar motor
        self.rmdx.setup()
        # envio del angulo
        res = self.rmdx.setPositionClosedLoopWithSpeed(motor_id, data_send)
        os.system('sudo /sbin/ip link set can0 down')
        # Leer respuesta de encoder
        res_list = self.decoi.readResponseDataPos(res.data)
        return res_list

    def reset_motor(self, motor_id):
        # print(f"applying reset to motor: {motor_id}")
        rmdx = self.rmdx
        rmdx.setup()
        rmdx.resetSystemMotor(motor_id)

    def stop_motor(self, motor_id):
        rmdx = self.rmdx
        rmdx.setup()
        rmdx.stopMotor(motor_id)

    def off_motor(self, motor_id):
        print(f"turning motor {motor_id} off")

    def get_multi_turn_angle_value(self, motors):
        rmdx = self.rmdx
        decoi = self.decoi
        rmdx.setup()
        # motor_id = 0x142
        index = int(input("seleccione un motor (0 al 4): "))
        motor_id = motors[index]
        encoder = rmdx.getMultiTurnAngle(motor_id)
        res_encoder = decoi.readMultiTurnAngle(encoder.data)
        print("*********************************")
        print("angle_value", res_encoder)

    def get_single_turn_angle_value(self):
        motors = self.motor_list
        rmdx = self.rmdx
        decoi = self.decoi
        rmdx.setup()
        # motor_id = 0x142
        index = int(input("seleccione un motor (0 al 4): "))
        motor_id = motors[index]
        encoder = rmdx.getSingleTurnAngle(motor_id)
        res_encoder = decoi.readSingleTurnAngle(encoder.data)
        print("*********************************")
        print("angle_value", res_encoder)

    def set_zero_motor(self, motor_id):
        # print(f"setting zero to motor: {motor_id}")
        rmdx = self.rmdx
        rmdx.setup()
        res = rmdx.setCurrentEncoderOffset(motor_id)

    # ---------------------------- parallel or concurrent functions -------------------

    def send_rotational_motion(self, speeds):
        motors = self.motor_list
        # Tareas en paralelo
        with concurrent.futures.ThreadPoolExecutor() as executor:
            movimiento = []
            for motor, speed in zip(motors, speeds):
                task = executor.submit(self.send_speed, motor, speed)
                movimiento.append(task)

            # esperar a quee todas las tareas se completen
            concurrent.futures.wait(movimiento)

    def send_motion_to_zero_kine(self, angulos, speeds):
        motors = self.motor_list
        with concurrent.futures.ThreadPoolExecutor() as executor:
            movimiento = []
            for motor, angulo, speed in zip(motors, angulos, speeds):
                task = executor.submit(self.send_pos_with_speed, motor, angulo, speed)
                movimiento.append(task)

            # esperar a quee todas las tareas se completen
            concurrent.futures.wait(movimiento)

    def send_motion(self, angulos, speeds):
        motors = self.motor_list
        # Tareas en paralelo
        with concurrent.futures.ThreadPoolExecutor() as executor:
            movimiento = []
            for motor, angulo, speed in zip(motors, angulos, speeds):
                task = executor.submit(self.send_pos_with_speed, motor, angulo, speed)
                movimiento.append(task)

            # esperar a quee todas las tareas se completen
            concurrent.futures.wait(movimiento)

    def send_action_reset_motors(self, motors):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            action = []
            for motor in motors:
                task = executor.submit(self.reset_motor, motor)
                action.append(task)
            # esperar a quee todas las tareas se completen
            concurrent.futures.wait(action)

    def send_action_stop_motors(self, motors):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            action = []
            for motor in motors:
                task = executor.submit(self.stop_motor, motor)
                action.append(task)

            # esperar a quee todas las tareas se completen
            concurrent.futures.wait(action)

    def send_action_set_zero_motors(self, motors):
        # print("sending command set zero")
        with concurrent.futures.ThreadPoolExecutor() as executor:
            action = []
            for motor in motors:
                task = executor.submit(self.set_zero_motor, motor)
                action.append(task)

            # esperar a quee todas las tareas se completen
            concurrent.futures.wait(action)

    # ------------------------------------ Interface --------------------------------
    def go_zero(self):
        # enable set zero rutine
        enable = True
        # speed for set zero rutine
        zero_speed = [80.0, -20.0, 32.0, -20.0, 0.0]  # velocidad minima motor 3 = 30
        # zero_speed = [20.0,0.0,0.0,0.0,0.0] #velocidad minima motor 3 = 30
        angulos_zero_kine = [-118.0, 108.0, -159.0, 20.0, 0]
        speed_kine = [80.0, 100.0, 40.0, 40.0, 40.0]
        sensor_trama_true = [0, 0, 0, 0, 0, 0, 0]
        sensor_trama_anterior = [0, 0, 0, 0, 0, 0, 0]
        self.send_rotational_motion(zero_speed)

        while enable:
            sensor_trama = [GPIO.input(self.f_1), GPIO.input(self.f_2), GPIO.input(self.f_3),
                            GPIO.input(self.f_4), GPIO.input(self.f_5), GPIO.input(self.f_6),
                            GPIO.input(self.f_7)]
            for j in range(len(sensor_trama)):
                if sensor_trama[j] == sensor_trama_anterior[j]:
                    sensor_trama_true[j] = sensor_trama[j]
                else:
                    sensor_trama_true[j] = sensor_trama_anterior[j]
            if sensor_trama_true == [0, 1, 0, 1, 1, 0, 1]:
                self.control_set_zero_mode()
                sleep(2)
                self.send_motion_to_zero_kine(angulos_zero_kine, speed_kine)
                sleep(5)
                self.control_set_zero_mode()
                sleep(1)
                angulos_zero = [0.1, 0.1, 0.0, 0.0, 0.0]
                self.send_motion(angulos_zero, speed_kine)
                enable = False
            else:
                # print("********SEARCHING ZERO MODE*****")
                print("lectura: ", sensor_trama_true)
                sensor_trama_anterior = sensor_trama
                self.control_stop_motor(sensor_trama)
                enable = True
            sleep(0.1)

        print("Finish set zero")
        message = "finis set zero"
        return message

# --------------------------------------- MAIN ----------------------------------
# if __name__ == '__main__':
#     print("APP RUNNING")
#
#     # --------------- Raspberry configs --------------------
#     # define pines here
#     GPIO.setwarnings(False)
#     GPIO.setmode(GPIO.BCM)
#     #Definicion sensores Numero de GPIO
#     button_on_of = 15
#     f_1 = 17
#     f_2 = 7
#     f_3 = 21
#     f_4 = 20
#     f_5 = 19
#     f_6 = 13
#     f_7 = 12
#
#     #Seteo de pines
#     GPIO.setup(button_on_of, GPIO.IN)
#     GPIO.setup(f_1, GPIO.IN)
#     GPIO.setup(f_2, GPIO.IN)
#     GPIO.setup(f_3, GPIO.IN)
#     GPIO.setup(f_4, GPIO.IN)
#     GPIO.setup(f_5, GPIO.IN)
#     GPIO.setup(f_6, GPIO.IN)
#     GPIO.setup(f_7, GPIO.IN)
#     # enable set zero rutine
#     enable = True
#
#     #Motors id
#     rmdx = RMDX()
#     motor_list = rmdx.getMotorList()
#     #   motor_list = [0x144]
#     #speed for set zero rutine
#     zero_speed = [80.0,-20.0,32.0,-20.0,0.0] #velocidad minima motor 3 = 30
#     # zero_speed = [20.0,0.0,0.0,0.0,0.0] #velocidad minima motor 3 = 30
#     angulos_zero_kine =[-118.0,108.0,-159.0,20.0,0]
#     speed_kine=[80.0,100.0,40.0,40.0,40.0]
#
#     #   zero_speed = [15.0]
#
#     send_rotational_motion(motor_list,zero_speed)
#
#     #estados iniciales de stop
#     state_m0 = False
#     state_m1 = False
#     state_m2 = False
#     state_m3 = False
#
#     states = [state_m0,state_m1,state_m2,state_m3]
#     sensor_trama_true=[0,0,0,0,0,0,0]
#     sensor_trama_anterior=[0,0,0,0,0,0,0]
#     sensor_trama_anterior_anterior=[0,0,0,0,0,0,0]
#
#
#
#
#
#
#     while enable:
#         # step 1: if sensors equal 1 them set zero motors and reset motors
#         # sensor trama
#         sensor_trama = [GPIO.input(f_1),GPIO.input(f_2),GPIO.input(f_3),
#                         GPIO.input(f_4),GPIO.input(f_5),GPIO.input(f_6),GPIO.input(f_7)]
#
#         for j in range(len(sensor_trama)):
#             if sensor_trama[j]==sensor_trama_anterior[j]:
#                 sensor_trama_true[j]=sensor_trama[j]
#             else:
#                 sensor_trama_true[j]=sensor_trama_anterior[j]
#
#         if sensor_trama_true == [0,1,0,1,1,0,1]:
#             # print("*******SET ZERO ON******")
#             #-------------- set zero kinematics -------------------
#             control_set_zero_mode(motor_list)
#
#             sleep(2)
#             send_motion_to_zero_kine(motor_list,angulos_zero_kine,speed_kine)
#             sleep(5)
#             control_set_zero_mode(motor_list)
#             sleep(1)
#             angulos_zero = [0.1,0.1,0.0,0.0,0.0]
#             send_motion(motor_list,angulos_zero,speed_kine)
#
#
#             #---------------------------------------------------
#             while True:
#                 # step 2: send desired position
#                 path_plannig(motor_list,speed_kine)
#             enable = False
#         else:
#
#             # print("********SEARCHING ZERO MODE*****")
#             print("lectura: ",sensor_trama_true)
#             sensor_trama_anterior=sensor_trama
#
#             control_stop_motor(sensor_trama,motor_list,states)
#             enable = True
#
#
#         # step 3: stop motor when associated sensor A equal 1 or sensor B equal 1
#
#         sleep(0.1)
#
#     print("Finish set zero")
