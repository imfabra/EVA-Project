import configparser
from pathlib import Path
import os

def getValueConfig(header, param):
    path = Path(__file__)
    ROOT_DIR = path.parent.absolute()
    config_path = os.path.join(ROOT_DIR, "configs.properties")
    config = configparser.RawConfigParser()
    config.read(config_path)
    return config.get(header, param)



class deco:

    def __init__(self):
        self.header = 'ValuesConfigs'
    
    def getDataDegreeWhitSpeed(self,degree,speed):
        if degree <= 360 and speed <= 10000:
            unity_conv = 0.01 #0.01
            pos_LSB = int(degree/unity_conv)
            speed_LSB = int(speed*1)#LSB
            data_degree_speed = bytearray([
                speed_LSB & 0xFF,
                (speed_LSB >> 8) & 0xFF,
                pos_LSB & 0xFF,
                (pos_LSB >> 8) & 0xFF,
                (pos_LSB >> 16) & 0xFF,
                (pos_LSB >> 24) & 0xFF
            ])
            return data_degree_speed
        else:
            print("index out of avialable range")


    def getDataDegree(self,degree):
        #start_angle = 0
        if degree <= 360:
            unity_conv = 0.01 #0.01
            pos_LSB = int(degree/unity_conv) #convercion a rago del motor (LSB = low significant bit)
            #start_pos_LSB = int(start_angle/unity_conv)
            #data to motor
            data_degree = bytearray([
                pos_LSB & 0xFF,
                (pos_LSB >> 8) & 0xFF,
                (pos_LSB >> 16) & 0xFF,
                (pos_LSB >> 24) & 0xFF
            ])
            return data_degree
        else:
            print("index out of avialable range")

    def getDataSpeed(self,speed):
        unity_conv = 100
        speed_LSB = int(speed * unity_conv)
        data_speed = bytearray([
            speed_LSB & 0xFF,
            (speed_LSB >> 8) & 0xFF,
            (speed_LSB >> 16) & 0xFF,
            (speed_LSB >> 24) & 0xFF,
        ])
        return data_speed

    def getDataTorque(self,value):
        param = 'abs.torque'
        lim = getValueConfig(self.header,param)
        int_lim = int(lim)
        if value >= (-1*int_lim) & value <= int_lim:
            data_torque =bytearray([
                value & 0xFF,
                (value >> 8) & 0xFF
            ])
            return data_torque
        else:
            print("index out of avialable range")

    # --------------------- Lectura de encoder ------------------------

    def readResponseDataPos(self, response):


        command_byte = response[0]
        motor_temp = response[1]
        torque_current = (response[3] << 8) | response[2]
        motor_speed = (response[5] << 8) | response[4]
        encoder_pos = (response[7] << 8) | response[6]

        torque_current_amps = torque_current * 33 / 2048 # Rango -33A a 33A

        response_data = list()
        response_data.append(command_byte)
        response_data.append(motor_temp)
        response_data.append(torque_current_amps)
        response_data.append(motor_speed)
        response_data.append(encoder_pos)

        return response_data
    
    def readEncoderData(self,response):
        command_byte = response[0]
        encoder_position = (response[3] << 8) | response[2]
        encoder_original_position = (response[5] << 8) | response[4]
        encoder_offset = (response[7] << 8) | response[6]

        angle_degress_m1 = ((encoder_original_position - encoder_offset)* 360)/65535
        angle_degress_m2 = ((encoder_position - encoder_offset)* 360)/65535

        response_data = list()
        response_data.append(command_byte)
        response_data.append(encoder_position)
        response_data.append(encoder_original_position)
        response_data.append(encoder_offset)
        response_data.append(angle_degress_m1)
        response_data.append(angle_degress_m2)

        return response_data

    def readEncoderDatatoAngle(self,response):
        encoder_position = (response[3] << 8) | response[2]
        encoder_original_position = (response[5] << 8) | response[4]
        encoder_offset = (response[7] << 8) | response[6]
        
        resolution = 65535
        angle_degrees = encoder_position * (360 / resolution)
        # angle_degrees = (encoder_position - encoder_offset) *(360 / resolution)
        # angle_degrees = ((encoder_original_position - encoder_offset)* 360)/65535
        
        response_data = list()
        response_data.append(encoder_position)
        response_data.append(encoder_original_position)
        response_data.append(encoder_offset)
        response_data.append(angle_degrees)
        
        return response_data

    def readMultiTurnEncoderZeroOffset(self,response):
        
        offset_value = (response[7] << 24) | (response[6] << 16) | (response[5] << 8) | response[4] 
        return offset_value



