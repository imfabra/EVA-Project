from api_eva.celery import app
from time import sleep
from .modules.controller_func import path_plannig, going_zero
from .modules.controll_kine import ControlKine

last_angles = []
speeds_motors = ControlKine()

@app.task
def mov_zero():
    last_angles = [0] * 5
    going_zero()
    pass

@app.task
def mov_eva(**kwargs):
    print(kwargs)
    angles, speeds = speeds_motors.speed_angles(last_angles ,[kwargs[f'angle{p+1}'] for p in range(5)], [kwargs['velocidad']]*5)
    path_plannig(angles,speeds)
    last_angles = [kwargs[f'angle{p+1}'] for p in range(5)]

@app.task
def sep_eva(**kwargs):
    angulos_lista = []
    lista_velocidades = []


    print("--------------------------------")
    for punto in kwargs['secuencia_puntos'].values():
        velocidad = [punto['puntos_data']['velocidad'], punto['puntos_data']['velocidad'], punto['puntos_data']['velocidad'], punto['puntos_data']['velocidad'],punto['puntos_data']['velocidad']]
        lista_velocidades.append(velocidad)
    print(lista_velocidades)

    print("--------------------------------")
    for punto_key, punto_data in kwargs['secuencia_puntos'].items():
        if punto_key.startswith('punto'):
            angulos = [] 
            for angulo_key, angulo_valor in punto_data['puntos_data'].items():
                if angulo_key.startswith('angulo'):
                    angulos.append(angulo_valor)

            angulos_lista.append(angulos)
            print(angulos)
            
            #path_plannig(angulos,lista_velocidades[0])
            sleep(4)

    print("--------------------------------")
    print(angulos_lista)
