import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1",5000))
server_socket.listen(1)

print("waiting")

conn, addr = server_socket.accept()
print("Connected")
n = int.from_bytes(conn.recv(4), "big")
data = b""

while len(data) < n*n*4:
    data += conn.recv(n*n*4 - len(data))

matrix = []
index = 0

for i in range(n):
    row = []
    for j in range(n):
        value = int.from_bytes(data[index:index+4], "big")
        row.append(value)
        index += 4
    matrix.append(row)
upper = True
lower = True
diagonal = True

for i in range(n):
    for j in range(n):
        if i>j and matrix[i][j] != 0:
            upper = False
        if i<j and matrix[i][j] != 0:
            lower = False
        if i != j and matrix[i][j] != 0:
            diagonal = False

if diagonal:
    result = "Diagonal"
elif upper:
    result = "Upper"
elif lower:
    result = "Lower"
else:
    result = "Not Triangular"

conn.send(result.encode())

print("M")
for row in matrix:
    print(row)
print("Type :", result)
conn.close()
server_socket.close()