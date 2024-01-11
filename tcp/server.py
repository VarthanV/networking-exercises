import socket

def server ():
    HOST , PORT = socket.gethostbyname(socket.gethostname()),8888
    server  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()

    print(F"Listening on {HOST}:{PORT}")

    while True:
        connection , address = server.accept()
        print(f"Received connection from address {address}")
        message = connection.recv(1024).decode('utf-8')
        print(f"Message from client {message}")
        connection.send("foo".encode('utf-8'))
        connection.close()

if __name__ == "__main__":
    server()