#!/usr/bin/python

import socket

# s = socket.socket(socket_family, socket_type, protocol=0)
# socket family is either Af_UNIX or AF_INET
# socket type is either SOCK_STREAM or SOCK_DGRAM
# PROTOCOL default is 0

# server socket method

# s.bind() -> bind address (hostname, port number pair) to socket.
# s.listen() -> sets up and start TCP listener.
# s.accept() => this passively accept TCP client connection, wait until connection arrives (blocking).

<<<<<<< HEAD
# general socket method

# s.recv() => this method receives TCP message 
# s.send() => this method transmits TCP message
# s.recvfrom() => this method receives UDP message
# s.sendto() => this method transmits UDP message
# s.close() => this method close socket
# socket.gethostname() => returns the hostname

# A simple server

# to write internet servers, we use the socket function available in socket module to create a socket object. a socket object is then used to call other functions to setup a socket server. Now call bind(hostname, port) function to specify a port for your service on the given host.

# Next call the accept method of the returned object. This method waits until a client connects to the port you specified, and then returns a connection object that represents the connection to that client.

s = socket.socket() # create a socket object
host = socket.gethostname() # get local machine name
port = 8920 # Reserver a port for your service
s.bind((host, port)) # bind to the port

s.listen(5) # Now wait for client connection 

while True:
    c, addr = s.accept() # establish connection with the client
    print('got connection from', addr)
    c.send('thank you for connecting')
    c.close() # close the connection
=======
# client socket method 
# s.connect() => this method actively initiates TCP Server  connection. 
>>>>>>> e204af7a6b13430c48e5790ef57187e363682cf3
