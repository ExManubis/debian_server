#! /bin/python3
# IMPORTS
import socket
import sys

# VARIABLES

# set server IP and port
server_host = '127.0.0.1'
server_port = 65431

# open data file and make variable for appending data
f = open('data.txt', 'a') # a = appending 

# PROGRAM
try:
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
                besked = message.decode() + f'\nIP: {addr}'
                if besked == f'\nIP: {addr}':
                    break
                else:
                    print(besked)
                    print('===============================')
                    print()
                    f.write('==============================')
                    f.write('\n')
                    f.write(besked)
                    f.write('\n')
                    f.write('==============================')
                    f.write('\n')
                    f.close
except KeyboardInterrupt:
    print('quitting SSO....')
    sys.exit()
