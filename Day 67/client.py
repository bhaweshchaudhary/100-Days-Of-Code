# a simple client

# let us write a very simple client program which opens a connection to a given port 8920 and given host. this is very simple to create a socket client using python socket module function. the socket.connect(hostname, port) open a tcp connection to hostname on the port. once you have a socket open, you can read from it like any IO object. When done remember to close it, as you would close a file. The following code is a very simple client that connects to a given host and port, reads any available data from the socket, and then exits -

#!/usr/bin/python
import socket # import socket module
s = socket.socket() # create socket object
host = socket.gethostname # get local machine name
port = 8920 # reserve a port for your service
s.connect((host, port))
print(s.recv(1024))
s.close() # close socket when done