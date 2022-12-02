import socket
from _socket import SHUT_WR


def createServer():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        serversocket.bind(("localhost", 9000))
        serversocket.listen(5)

        while True:
            (clientsocket, addres) = serversocket.accept()

            # data received FROM client
            data1 = clientsocket.recv(1024).decode()
            data2 = data1.split("\n")
            if len(data2) > 0: print(data2)

            # data = "HTTP/1.1 200 OK\r\n"
            # data += "Content-Type: text/html; charset=utf-8\r\n"
            # data += "\r\n"
            data = "<html><body>Helloooo World</body></html>\r\n\r\n"

            # sent TO client
            clientsocket.sendall(data.encode())
            # client shut down
            clientsocket.shutdown(socket.SHUT_WR)



    except KeyboardInterrupt:
        print("Itrerrupting..")

    except Exception as exc:
        print("Error:")
        print(exc)

    serversocket.close()


# createServer()


def create_server2():
    HOST = "localhost"
    PORT = 9000
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        serversocket.bind((HOST, PORT))
        serversocket.listen(5)

        while True:
            (clientsocket, addres) = serversocket.accept()

            recv_data = clientsocket.recv(1024).decode()
            recv_data2 = recv_data.split("\n")
            if len(recv_data2) > 0: print(recv_data2[0])

            data = "Munchkin"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("I..")

    except Exception as exc:
        print(exc)

    serversocket.close()


create_server2()
