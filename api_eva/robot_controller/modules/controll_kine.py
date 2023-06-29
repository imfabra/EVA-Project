class ControlKine:
    def __init__(self):
        pass

    def speed_angles(current_angles, expected_angles, velocity):
        if isinstance(velocity, int):
            velocity = [velocity] * len(current_angles)

        full_angles = [abs((a)-(d)) for a, d in zip(current_angles, expected_angles)]

        max_angle = max(full_angles)
        speeds = [round((v * angle / max_angle), 2) for angle, v in zip(full_angles, velocity)]

        print(f'''
            \r---------------------- Velocidad Motores  ----------------------
            \rAngulos actuales:  {current_angles},
            \rAngulos deseados:  {expected_angles},
            \rRecorrido motores: {full_angles},
            \rVelocidad:         {speeds}
            \r----------------------------------------------------------------
        ''')

        return [expected_angles, speeds]