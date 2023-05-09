import socket
import select
import sys
from _thread import *

server = socket.socket()

host='localhost'
port=9999

server.bind((host, port))

server.listen(100)

list_of_clients = []

def clientthread(conn, addr):

    conn.send("Welcome to this chatroom!".encode())

    while True:
            try:
                message = conn.recv(2048).decode()
                if message:
                    if message == "quit":
                        conn.close()
                        print(addr[0]+"closed")
                        remove(conn)
                    else:
                        print ("<" + addr[0] + "> " + message)
                        message_to_send = "<" + addr[0] + "> " + message
                        broadcast(message_to_send, conn)
                else:
                    remove(conn)
            except:
                continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:

    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr)

    print (addr[0] + " connected")

    start_new_thread(clientthread,(conn,addr))	

conn.close()
server.close()
