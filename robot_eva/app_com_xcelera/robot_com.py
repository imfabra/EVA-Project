from app_robot_controller.app_eva_controller import Robot



#Aqui van todas laa funciones de comunicacion de xcelera con el robot

class Connection:

    def __init__(self):
        self.robot = Robot()

    def send_go_zero(self):
        return self.robot.go_zero()