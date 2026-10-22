import socket

HOST = "127.0.0.1"
PORT = 2000
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s = input("Text :")
client.sendto(s.encode(), (HOST, PORT))
data, add = client.recvfrom(1024)

print("Transalated")
print(data.decode())

client.close()