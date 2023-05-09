import socket
import sys
import time
import os
import struct

print("\nWelcome to the FTP server.\n\nTo get started, connect a client.")

IP = "localhost"
PORT = 9999 
BUFFER_SIZE = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)
conn, addr = s.accept()

print("\nConnected to by address: {}".format(addr))

def upld():
    
    conn.send("1".encode())
    
    file_name_size = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_size).decode()

    conn.send("1".encode())
    
    file_size = struct.unpack("i", conn.recv(4))[0]

    start_time = time.time()
    output_file = open(file_name, "wb")
    bytes_recieved = 0
    print("\nRecieving...")
    while bytes_recieved < file_size:
        l = conn.recv(BUFFER_SIZE)
        output_file.write(l)
        bytes_recieved += BUFFER_SIZE
    output_file.close()
    print("\nRecieved file: {}".format(file_name))
   
    conn.send(struct.pack("f", time.time() - start_time))
    conn.send(struct.pack("i", file_size))
    return

def dwld():
    conn.send("1".encode())
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    print(file_name_length)
    file_name = conn.recv(file_name_length).decode()
    print(file_name)
    if os.path.isfile(file_name):
        
        conn.send(struct.pack("i", os.path.getsize(file_name)))
    else:
    
        print("File name not valid")
        conn.send(struct.pack("i", -1))
        return
    
    conn.recv(BUFFER_SIZE).decode()
  
    start_time = time.time()
    print("Sending file...")
    content = open(file_name, "rb")
    
    l = content.read(BUFFER_SIZE)
    while l:
        conn.send(l)
        l = content.read(BUFFER_SIZE)
    content.close()
  
    conn.recv(BUFFER_SIZE).decode()
    conn.send(struct.pack("f", time.time() - start_time))
    return

def quit():
    # Send quit conformation
    conn.send("1".encode())
    # Close and restart the server
    conn.close()
    s.close()
    os.execl(sys.executable, sys.executable, *sys.argv)

while True:
    
    print("\n\nWaiting for instruction")
    data = conn.recv(BUFFER_SIZE).decode()
    print("\nRecieved instruction: {}".format(data))
  
    if data == "UPLD":
        upld()
    elif data == "DWLD":
        dwld()
    elif data == "QUIT":
        quit()
 
    data = None