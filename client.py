# TCP client
# Author:
# Date:

import sys
import socket

HOST = "172.0.0.1"
PORT = 5000
# create socket 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
# send data
client_socket.send("Hello from client".encode()) # send data to server
res = client_socket.recv(1024) # recv response from server
print("Received: {}".format(res))