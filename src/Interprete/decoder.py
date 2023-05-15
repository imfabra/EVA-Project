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

    def getDataDegree(self,degree):
        if degree <= 360:
            unity_conv = 0.01
            pos_LSB = int(degree/unity_conv) #convercion a rago del motor (LSB = low significant bit)
            #data to motor
            data_degree = bytearray([
                pos_LSB & 0xFF,
                (pos_LSB >> 8) & 0xFF,
                (pos_LSB >> 16) & 0xFF,
                (pos_LSB >> 24) & 0xFF,
            ])
            return data_degree
        else:
            print("index out of avialable range")

    def getDataSpeed(self,speed):
        unity_conv = 0.01
        speed_LSB = speed * unity_conv
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

