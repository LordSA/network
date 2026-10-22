import socket
HOST = "127.0.0.1"
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

file = input("Enter the file name :")
client.send(file.encode())
data = b""
while True:
    part = client.recv(1024)
    if not part:
        break
    data += part

print("resp")
print(data.decode())
client.close()