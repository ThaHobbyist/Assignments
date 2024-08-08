import socket

host = 'localhost'
port = 9999
client = socket.socket()
client.connect((host, port))

print("Select an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")

sel = input("Enter: ")
x = input("Enter X: ")
y = input("Enter Y: ")
string = sel + "#" + x + "#" + y

client.send(string.encode())
data = client.recv(1024).decode()
print("Result = {}".format(data))
client.close()
