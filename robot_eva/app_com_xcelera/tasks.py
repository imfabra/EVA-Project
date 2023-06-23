from robot_eva.celery import app
from time import sleep
from .robot_com import Connection
from app_robot_controller.app_eva_controller import going_zero , path_plannig

@app.task 
def add_numbers(x, y):
    while True:
        x = x + 1
        y = y + 1
        print('adding numbers', x, y)
        sleep(1)
        if x >= 50:
            break
    
    return x + y

@app.task 
def del_numbers(x, y):
    while True:
        x = x + 1
        y = y + 1
        print('adding numbers', x, y)
        sleep(1)
        if x >= 50:
            break
    
    return x + y


@app.task
def go_zero():
    going_zero()

@app.task
def going_to_point():
    path_plannig([45.0,45.0,45.0,45.0,45.0],[40.0,40.0,40.0,40.0,40.0])