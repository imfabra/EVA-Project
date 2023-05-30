#Aplicación de control para el robot
import RPi.GPIO as GPIO 
from time import sleep 


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
#Definicion sensores Numero de GPIO
button_on_of = 2
f_1 = 3
f_2 = 7
f_3 = 12
f_4 = 13
f_5 = 19
f_6 = 20
f_7 = 21

#Seteo de pines
GPIO.setup(button_on_of, GPIO.IN)
GPIO.setup(f_1, GPIO.IN)
GPIO.setup(f_2, GPIO.IN) 
GPIO.setup(f_3, GPIO.IN) 
GPIO.setup(f_4, GPIO.IN)    
GPIO.setup(f_5, GPIO.IN)
GPIO.setup(f_6, GPIO.IN)
GPIO.setup(f_7, GPIO.IN) 


while True:
    print(GPIO.input(button_on_of),GPIO.input(f_1),
          GPIO.input(f_2),GPIO.input(f_3),GPIO.input(f_4),
          GPIO.input(f_5),GPIO.input(f_6),GPIO.input(f_7))
    sleep(0.5)
    

