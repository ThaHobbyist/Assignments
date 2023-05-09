import socket

host = 'localhost'
port = 9999
server = socket.socket()
server.bind((host, port))
server.listen(1)
print("Server Started")
print("Waiting for connection...")

while True:
    c, addr = server.accept()
    data = c.recv(1024).decode()
    t = data.split("#", 3)
    opr = int(t[0])
    num1 = int(t[1])
    num2 = int(t[2])

    res = 0
    if opr == 1:
        res = num1 + num2
        print("{} + {} = {}".format(num1, num2, res))
    elif opr == 2:
        res = num1 - num2
        print("{} - {} = {}".format(num1, num2, res))
    elif opr == 3:
        res = num1 * num2
        print("{} * {} = {}".format(num1, num2, res))
    elif opr == 4:
        res = num1 / num2
        print("{} / {} = {}".format(num1, num2, res))
    elif opr == 5:
        res = num1 ** num2
        print("{} ^ {} = {}".format(num1, num2, res))
    else:
        res = 0
    
    c.send(str(res).encode())
    c.close()