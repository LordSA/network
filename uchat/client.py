import socket 
import threading
HOST = "LOCALHOST"
PORT = 1000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

name = input("Enter the Name :")
def rec_m():
    while True :
        try:
            message = client.recv(1024)
            print(message.decode())
        except:
            break

threading.Thread(target=rec_m,daemon=True).start()

while True:
    message = input()
    if message.lower() == "exit":
        break
    client.send(f"{name} : {message}".encode())
client.close()