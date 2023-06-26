from api_eva.celery import app
from .modules.controller_func import path_plannig, going_zero

@app.task
def mov_eva(**kwargs):
    print(kwargs)
    angles = [kwargs['angulo1'], kwargs['angulo2'], kwargs['angulo3'], kwargs['angulo4'], kwargs['angulo5']]
    speed = [kwargs['velocidad'], kwargs['velocidad'], kwargs['velocidad'], kwargs['velocidad'], kwargs['velocidad']]
    path_plannig(angles,speed)
  
@app.task
def mov_zero():
    going_zero()