
def getDataDegree(degree):
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

