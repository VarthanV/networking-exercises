import socket

'''
    s = socket.socket(addr_family, type)
    Address family
    socket.AF_INET Internet protocol (IPv4)
    socket.AF_INET6 Internet protocol (IPv6)

    Socket type
    socket.SOCK_STREAM Connection based stream (TCP)
    socket.SOCK_DGRAM Datagrams (UDP)
'''

# Address family -
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Making outgoing connection
s.connect(("www.google.com",80)) # Connect
s.send(b"GET /index.html HTTP/1.0\n\n") # Send request
data = s.recv(10000) # Get response
print("data is ",data)
s.close()
