import socket

mysocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket2.connect(("data.pr4e.org", 80))

cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()

# mysocket2.connect(("literature.org", 80))
#
# cmd = "GET https://literature.org/authors/stoker-bram/dracula/chapter-01.html HTTP/1.0\r\n\r\n".encode()
mysocket2.send(cmd)

while True:
    data = mysocket2.recv(1024)
    if len(data) < 1: break

    print(data.decode(), end="")

mysocket2.close()