import socket

def client():
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect(("localhost", 9000))

    cmd = 'GET  http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()

    mysocket.send(cmd)

    while True:
        data = mysocket.recv(1024)
        if len(data)<0:
            break

        print(data.decode(), end="")

    socket.close()

def client2():
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    mysocket.connect(("localhost", 9000))

    cmd = 'Yo bitches'.encode()
    mysocket.send(cmd)

    while True:
        data = mysocket.recv(100)

        if len(data)<0:
            break

        print(data.decode(), end="")

    mysocket.close()

client2()