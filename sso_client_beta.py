# IMPORTS
from socket import *

# VARIABLES
serverName = ''
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# PROGRAM
print('=====================================')
print('SSO_klient v0.1 klar til at sende')
print('=====================================')

while True:
    message = input('Message for server: ')
    clientSocket.sendto(message.encode(), (serverName, serverPort))
