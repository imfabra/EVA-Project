from lib.rmdx_funtions import RMDX 

if __name__ == "__main__":
    rmdx = RMDX()
    rmdx.setup()
    data = [0x64,0x64,0x64,0x64]
    motor_id = 0x142
    res = rmdx.setSpeedClosedLoop(motor_id,data)
    print(res)



