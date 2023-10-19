#! /bin/python3
# IMPORTS
import socket

# VARIABLES
HOST = "127.0.0.1"
PORT = 65431

# PROGRAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input('Message: ')
        s.sendto(message.encode(), (HOST, PORT))

