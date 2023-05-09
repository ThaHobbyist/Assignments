import socket
c = socket.socket()
c.connect(('localhost', 9999))
connected = True

while connected:
    msg = input("Enter Message: ")
    c.send(msg.encode('utf-8'))
    if msg == "!DISCONNECT":
        connected = False
    else:
        msg = c.recv(1024).decode('utf-8')
        print(f"server: {msg}")

c.close()