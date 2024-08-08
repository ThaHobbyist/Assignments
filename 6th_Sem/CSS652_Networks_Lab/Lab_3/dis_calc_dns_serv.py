import socket

s = socket.socket()
s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connection...")

while True:
    c, addr = s.accept()
    data = c.recv(1024).decode()
    p = data.split("#", 3)
    opr = int(p[0])
    res = None

    s1 = socket.socket()
    s1.connect(('localhost', 9999-opr))
    s1.send(data.encode())

    while res == None:
        res = s1.recv(1024).decode()
        
    print(res)
    print("result: {}".format(res))
    
    c.send(str(res).encode())
    c.close()