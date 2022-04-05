# Python TCP server program 
# Author: Mose
# date 5 Apr 2022

import socket
import sys

def main():

    interface = ("0.0.0.0", 5000) # network host and port

    #create socket
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind socket
    server_soc.bind(interface)
    #listen for incoming connections
    server_soc.listen(3)
    print("Listening for connections @{}:{}".format(interface[0], interface[1]))

    while True:
        con, addr = server_soc.accept() # accept new connections
        client_handler(con, addr) # pass task to client handler

def client_handler(client_socket, client_addr):
    # Function to handle new client connections

    # receive client data
    data = client_socket.recv(1024)
    print("Received: {} from {}".format(data, client_addr))
    # send ACK
    client_socket.send('ACK'.encode())
    # close socket 
    client_socket.close()

if __name__ == "__main__":
    main()

