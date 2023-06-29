class ControlKine:
    def __init__(self):
        self.__last_angles = list()
        pass

    def speed_angles(self, current_angles, expected_angles, velocity):
        if isinstance(velocity, int):
            velocity = [velocity] * len(current_angles)

        full_angles = [round(abs((a)-(d)), 2) for a, d in zip(current_angles, expected_angles)]

        max_angle = max(full_angles)
        speeds = [round((v * angle / max_angle), 2) if (angle != 0) else 0 for angle, v in zip(full_angles, velocity)]
        speeds[1] = speeds[1]*2
        print(f'''
            \r---------------------- Velocidad Motores  ----------------------
            \rAngulos actuales:  {current_angles},
            \rAngulos deseados:  {expected_angles},
            \rRecorrido motores: {full_angles},
            \rVelocidad:         {speeds}
            \r----------------------------------------------------------------
        ''')

        return [expected_angles, speeds]
    
    def get_last_move(self):
        return self.__last_angles
    
    def set_last_move(self,list):
        self.__last_angles=list