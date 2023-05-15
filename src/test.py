import unittest
from lib.rmdx_funtions import RMDX 
from Interprete.decoder import deco 
import os

class Tests(unittest.TestCase):
    
    def test_send_position_degree(self):

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
        self.assertIsNotNone(res,"the data doesn't have to be null")
        
        #Leer respuesta de encoder
        res_list = list()
        res_list = decoi.readResponseDataPos(res.data)

        print("temp: "+str(res_list[1]))
        print("current: "+str(res_list[2]))
        print("speed: "+str(res_list[3]))
        print("encoder_pos: "+str(res_list[4]))
        
        
    
    def test_send_speed_value(self):
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
        self.assertIsNotNone(res,"the data doesn't have to be null")
    
    def test_send_speed_hexa(self):
        rmdx= RMDX()
        rmdx.setup()
        motor_id= 0x142
        data = [0x64,0x64,0x64,0x64]
        res = rmdx.setSpeedClosedLoop(motor_id,data)
        self.assertIsNotNone(res,"the data doesn't have to be null")
    
    def test_send_post_hexa(self):
        rmdx= RMDX()
        rmdx.setup()
        motor_id= 0x142
        data = [0x5A,0x5A,0x5A,0x5A]
        res = rmdx.setPositionClosedLoop(motor_id,data)
        self.assertIsNotNone(res,"the data doesn't have to be null")
    
    def test_read_encoder(self):
        os.system('sudo /sbin/ip link set can0 down')
        rmdx = RMDX()
        decoi = deco()
        rmdx.setup()
        motor_id = 0x142
        encoder = rmdx.getEncoder(motor_id)
        res_encoder = decoi.readEncoderData(encoder.data)

        print("Command ",res_encoder[0])
        print("Encoder Position ",res_encoder[1])
        print("Encoder Original Position ",res_encoder[2])
        print("Encoder offset ",res_encoder[3])
        print("Angulo",res_encoder[4])

    



if __name__ == "__main__":
    unittest.main()