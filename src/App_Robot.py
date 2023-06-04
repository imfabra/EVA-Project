# esqueleto base para tercera capa del framework del robot
# --- CAPA N°3 CONTROL ---------------------

# ------------------ control functions -----------
def direct_kinematics():
    print("run direct kinematics")


def inverse_kinematics():
    print("run inverse kinematics")
    # code here


# -------------------- motor functions ----------
def send_pos_with_speed(motor_id, value, speed):
    print(f"sending {value} degrees to motor {motor_id} with {speed} rad/s")


def reset_motor(motor_id):
    print(f"applying reset to motor: {motor_id}")


def stop_motor(motor_id):
    print(f"stopping motor {motor_id}")


def off_motor(motor_id):
    print(f"turning motor {motor_id} off")


def get_multi_turn_angle_value(motor_id):
    print(f" motor {motor_id} has angle value : ")


def set_zero_motor(motor_id):
    print(f"setting zero to motor: {motor_id}")


# ---------------------------- parallel or concurrent functions -------------------

def send_motion(motors):
    print("sending motion ..")


def send_action_reset_motors(motors):
    print("sending reset ..")


def send_action_stop_motors(motors):
    print("sending stop ..")


def send_action_set_zero_motors(motors):
    print("sending command set zero")


# --------------------------------------- MAIN ----------------------------------
if __name__ == '__main__':
    print("APP RUNNING")
