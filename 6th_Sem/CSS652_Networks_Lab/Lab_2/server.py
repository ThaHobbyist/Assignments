# Multithreding
import socket
import threading
s = socket.socket()

s.bind(('localhost', 9999))
s.listen()
print("Waiting for connection...")

def handle_client(c, addr):
    print("Client Code...")
    connected = True
    while connected:
        msg = c.recv(1024).decode('utf-8')
        if msg == '!DISCONNECT':
            connected = False
        
        print(f"[{addr}]{msg}")
        msg=f"msg recieved: {msg}"
        c.send(msg.encode('utf-8'))
        c.close()


while True:
    c, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(c, addr))
    print(f"No. of active connection: {threading.active_count()}")
