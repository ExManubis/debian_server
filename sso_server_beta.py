#! /bin/python3
# IMPORTS
from socket import *

# VARIABLES
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) # use TCP
serverSocket.bind(('', serverPort)) # bind serverport

# PROGRAM
print('=====================================================')
print('SSO_server v.01 klar til at modtage')
print('=====================================================')

while True:
    message, client = serverSocket.recvfrom(2048)
    print(message.decode())
    print()
