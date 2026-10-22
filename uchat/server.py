import socket
import threading
HOST = "127.0.0.1"
PORT = 1000
clients = []
def broadcast( message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break
            print(message.decode())
            broadcast(message, client)
        except:
            break

    clients.remove(client)
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("st cooking .. ")

while True :
    client, addr = server.accept()
    print(f'Connected : {addr}')
    clients.append(client)

    thread =  threading.Thread(
        target=handle,
        args = (client,)
    )
    thread.start()