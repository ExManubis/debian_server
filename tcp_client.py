#! /bin/python3
# IMPORTS
import socket
import sys


# VARIABLES
server_host = "127.0.0.1"
#server_port = 2222

# PROGRAM
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        server_port_str = input('2222, 3333 eller 4444 ')
        server_port = int(server_port_str)
        s.connect((server_host, server_port))
        bruger = '\nObservant: ' + input('Dit navn: ')
        while True:
            tid = 'Tid: ' + input('Tid: ')
            spiller = '\nSpiller: ' + input('Spiller: ')
            obs = '\nObservation: ' + input('Observation: ')
            message = tid + spiller + obs + bruger
            s.sendto(message.encode(), (server_host, server_port))
            print()
except KeyboardInterrupt:
    print('quitting...')
    sys.exit()

