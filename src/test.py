import unittest
from lib.rmdx_funtions import RMDX as rmdx
from Interprete.decoder import deco as decoi

class Tests(unittest.TestCase):
    
    def test_send_position_degree(self):
        value = input("ingrese angulo: ")
        #obtener la trama del angulo
        data_send = decoi.getDataDegree(value)
        #inicializar motor
        rmdx.setup()
        motor_id = 0x142
        #envio del angulo
        res = rmdx.setPositionClosedLoop(motor_id,data_send)
        self.assertIsNotNone(res,"the data doesn't have to be null")


if __name__ == "__main__":
    unittest.main()