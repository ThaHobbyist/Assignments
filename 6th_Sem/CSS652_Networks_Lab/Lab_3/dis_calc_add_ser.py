import socket

s = socket.socket()
s.bind(('localhost', 9998))
s.listen(3)

while True:
    c, addr = s.accept()
    data = c.recv(1024).decode()
    p = data.split('#')
    x = int(p[1])
    y = int(p[2])
    res = str(x + y)
    print(res)
    c.send(res.encode())
    c.close()
