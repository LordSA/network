import socket
import threading
import os

HOST = "127.0.0.1"
PORT = 7000

def handle(client):
    file = client.recv(1024).decode()
    pid = os.pid()
    if os.path.exists(file) and os.path.isfile(file):
        with open(file, "r") as file:
            cont = file.read()
        message = f"PID: {pid} \n Found\n{cont}"
    else:
        message = f"{pid} \n NOT FOUND"
    client.sendall(message.encode())
    client.close()


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print("Cooking...")

while True:
    client, add = server.accept()
    print(f"Connected : {add}")
    thread = threading.Thread(
        target = handle,
        args = (client,)
    )
    thread.start()