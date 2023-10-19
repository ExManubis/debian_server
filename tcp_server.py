#! /bin/python3
# IMPORTS
import socket

# VARIABLES
server_host = '127.0.0.1'
server_port = 65433

# PROGRAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_host, server_port))
    s.listen()
    connection, addr = s.accept()
    with connection:
        print(f'Connected by {addr}')
        #connection.setblocking(False)
        while True:
            message, client = connection.recvfrom(1024)
            print()
            print('===============================')
            print(message.decode(), f'\nIP: {addr}')
            print('===============================')
            print()
