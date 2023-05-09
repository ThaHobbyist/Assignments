import socket
s = socket.socket() # creating socket object
print("socket Created")

s.bind(('localhost', 9999)) # Binding to localhost at port 9999
s.listen(3) # Listen to atmost 3 clients at a time
print("Waiting for connection")

# Running the socket to listed for client connections
message = "Welcome"
while True: 
    c, addr = s.accept()
    print("Connected with ", addr)
    c.send(bytes("Welcome", 'utf-8'))
    c.close()