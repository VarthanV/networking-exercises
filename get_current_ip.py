# Python Program to Get IP Address
import socket
import os
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

print("Host name is " + host_name)
print("IP Address is " + ip_address)