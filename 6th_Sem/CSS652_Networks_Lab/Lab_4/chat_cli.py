import socket
import select
import sys
import threading


class myThreadSend(threading.Thread):
    global s
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        msgSend(s)

class myThreadRecv(threading.Thread):
    global s
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        msgRecv(s)
    

def msgRecv(s):
    while True:
        data = s.recv(2048).decode()
        print(data)
        if(data == "quit"):
            s.close()
            exit(0)

def msgSend(s):
    msg = input("")
    while msg:
        s.send(msg.encode())
        if(msg=="quit"):
            s.close()
            exit(0)
        msg = None
 
# while True:
    # sockets_list = [sys.stdin, server]
    # read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])

    # for socks in read_sockets:
    #     if socks == server:
    #         message = socks.recv(2048).decode()
    #         print(message)
    #     else:
    #         message = input()
    #         if message == "quit":
    #             server.send(message.encode())
    #             server.close()
    #         else:
    #             server.send(message.encode())
    #             print("<You>"+message)

# server.close()

if __name__ == "__main__":
    s = socket.socket()

    host = 'localhost'
    port = 9999
    s.connect((host, port))

    while True:
        threadSend = myThreadSend(1, "ThreadSend", 1)
        threadRecv = myThreadRecv(2, "threadRecv", 2)

        threadSend.start()
        threadRecv.start()
        threadSend.join()
        threadSend.join()
    
    s.close()
