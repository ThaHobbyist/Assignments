import socket
c = socket.socket()
c.connect(('localhost', 9999))
print("Connected to server")

msg = c.recv(1024)
print("Recieved Message: ", msg)

c.close()