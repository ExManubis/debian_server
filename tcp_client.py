#! /bin/python3
# IMPORTS
import socket
import time

# VARIABLES
server_host = "127.0.0.1"
server_port = 65433

# PROGRAM
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_host, server_port))
    bruger = '\nObservant: ' + input('Dit navn: ')
    while True:
        tid = 'Tid: ' + input('Tid: ')
        spiller = '\nSpiller: ' + input('Spiller: ')
        obs = '\nObservation: ' + input('Observation: ')
        message = tid + spiller + obs + bruger
        s.sendto(message.encode(), (server_host, server_port))
        print()

