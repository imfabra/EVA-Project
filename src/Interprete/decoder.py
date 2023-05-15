
def getDataDegree(degree):
    if degree <= 360:
        unity_conv = 0.01
        pos_LSB = degree/unity_conv #convercion a rago del motor (LSB = low significant bit)
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

def getDataSpeed(speed):
    unity_conv = 0.01
    speed_LSB = speed * unity_conv
    data_speed = bytearray([
        speed_LSB & 0xFF,
        (speed_LSB >> 8) & 0xFF,
        (speed_LSB >> 16) & 0xFF,
        (speed_LSB >> 24) & 0xFF,
    ])
    return data_speed

