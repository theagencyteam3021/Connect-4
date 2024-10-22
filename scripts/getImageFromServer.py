import socket

def getImageFromServer():
    s = socket.socket()
    host = '127.0.0.1'
    port = 8080
    s.connect((host, port))
    data = s.recv(2048)
    s.close()
    return data

