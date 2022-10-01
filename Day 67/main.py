import socket

# s = socket.socket(socket_family, socket_type, protocol=0)
# socket family is either Af_UNIX or AF_INET
# socket type is either SOCK_STREAM or SOCK_DGRAM
# PROTOCOL default is 0

# server socket method
# s.bind() -> bind address (hostname, port number pair) to socket.
# s.listen() -> sets up and start TCP listener.
# s.accept() => this passively accept TCP client connection, wait until connection arrives (blocking).

# client socket method 
# s.connect() => this method actively initiates TCP Server  connection. 