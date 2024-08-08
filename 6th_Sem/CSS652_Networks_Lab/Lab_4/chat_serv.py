import sys
import socket
import threading

class myThreadRecv(threading.Thread):
    global s, con
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        msgRecv(s, con)

class myThreadSend(threading.Thread):
    global s, con
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        msgSend(s, con)

def msgRecv(s):
    while True:
        data = s.recv(50)
        print("\t\t", data)
        if(data == "quit"):
            s.close()
            exit(1)

def msgSend(s):
    global name
    while True:
        print(" " +name+">>")
        string = input()
        msg = name+","+string

        s.send(msg)
        if(string=="quit"):
            s.close()
            exit(1)

if __name__ == "__main__":
    host="localhost"
    port=9999

    s = socket.socket()
    s.bind((host,port))

    print("Server Started on port: {} ".format(port))

    while True:
        s.listen(2)
        clientSock, clientAddr = s.accept()

        print()

        thread1 = myThreadRecv(1, "Thread-1", 1)
        thread2 = myThreadSend(2, "Thread-2", 2)

        thread1.start()
        thread2.start()


    
