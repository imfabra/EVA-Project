from api_eva.celery import app
from time import sleep
from .modules.controller_func import path_plannig, going_zero

@app.task
def mov_zero():
    going_zero()
    pass

@app.task
def mov_eva(**kwargs):
    print(kwargs)
    angles = [kwargs['angulo1'], kwargs['angulo2'], kwargs['angulo3'], kwargs['angulo4'], kwargs['angulo5']]
    speed = [kwargs['velocidad'], kwargs['velocidad'], kwargs['velocidad'], kwargs['velocidad'], kwargs['velocidad']]
    #path_plannig(angles,speed)

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
            
            path_plannig(angulos,lista_velocidades[0])
            sleep(4)

    print("--------------------------------")
    print(angulos_lista)
