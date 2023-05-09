import socket
import threading
import sys

class myThread1(threading.Thread):
    global s, conn

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    
    def run(self):
        msgSend(s, conn)

def msgSend(s, conn):
    while True:
        conn.send("Enter the operation")
        # Enter necessary code here
        if(download):
            f1 = open("path_to_file", r+)
            conn.send("Choose the name of the file")
            l = f1.read(100)
            while len(l) != 0:
                conn.send(l)
            f1.close()
        
        elif(upload):
            #code for upload
            f1 = ...
            con.send("file_name")
            filename = con.recv(..)
            filename = "uploaded" + str(filename)
            f1.close()
            print(conn.recv(1024))
        else :
            pass

'''
host
portname
bind 
listen
connection established
'''