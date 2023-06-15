# import socket
# import RPi.GPIO as GPIO
# s = socket.socket()
# s.bind(("192.168.6.10",2020))
# s.listen(10)
# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(2,GPIO.OUT)

# while True:
#     (sc,addrc) = s.accept()
#     print("Ejecutando:",addrc)
#     continuar = True
#     while continuar:
#         dato = sc.recv(64)
#         if not dato:
#             continuar = False
#             print("CLiente desconectado")
#         else:
#             dato2 = dato.decode()
#             if dato2 == "a":
#                 print("Led encendido")
#                 GPIO.output(2,GPIO.HIGH)
#             elif dato2 == "b":
#                 print("Led apagado")
#                 GPIO.output(2,GPIO.LOW)

# s.close()
# print("Fin de Programa")

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.6.11', 2000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()