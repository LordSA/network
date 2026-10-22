import socket
import time
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("Enter the ip: ")

for i in range(10):
    client.sendto(b"TIME", (ip,6000))
    data, addr = client.recvfrom(1024)
    print(f"Time : {data.decode()}")
    if i < 5 :
        time.sleep(5)

client.close()