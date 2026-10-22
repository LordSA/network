import socket
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 6000))
print("Cooking...")
while True:
    data, add = server.recvfrom(1024)
    print("recieved", add)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    server.sendto(time.encode(), add)