from app_robot_controller.app_eva_controller import Robot


# Aqui van todas laa funciones de comunicacion de xcelera con el robot

class Connection:

    def __init__(self):
        self.robot = Robot()

    def send_go_zero(self):
        return self.robot.go_zero()
    
    def send_off_robot(self):
        return self.robot.send_off_robot()

    def send_pos_to_robot(self, joins_data):
        desired_pos = []
        for join in joins_data:
            value = float(joins_data[join])
            desired_pos.append(value)
        self.robot.send_motion(desired_pos)
