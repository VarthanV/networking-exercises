import socket

def connect():
    HOST , PORT = socket.gethostbyname(socket.gethostname()),8888
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    s.send("hi".encode())
    print(f"Received response {s.recv(1024)}")

if __name__ == "__main__":
    connect()