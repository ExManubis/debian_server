#! /bin/python3

# IMPORTS
import socket
import threading
from _thread import*

# VARIABLES
print_lock = threading.Lock()

# FUNCTIONS
def threaded(c):
    while True:

        data = c.recv(1024)
        if not data:
            print('Bye')

            print_lock.release()
            break

        data = data [::-1]

        c.send(data)

    c.close()


def Main():
    host = ""

    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

    s.listen(5)
    print("socket is listening")
    
    # loop until clients exit
    while True:
        
        # establish connection
        c, addr = s.accept()
        
        # lock acquired by client
        print_lock.acquire()
        print('Connected to: ', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()

if __name__ == '__main__':
    Main()
