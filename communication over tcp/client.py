import socket
import random

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 5000))
n = int(input("Enter the order of matrix :"))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(i,50))
    matrix.append(row)

print("matrix :")
for row in matrix:
    print(*row)

client_socket.send(n.to_bytes(4, "big"))
data = b""

for row in matrix:
    for value in row:
        data += value.to_bytes(4, "big")

client_socket.sendall(data)
result = client_socket.recv(1024).decode()
print("Matrix = ", result)
client_socket.close()