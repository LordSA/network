import socket
HOST = "127.0.0.1"
PORT = 2000

dict = {
    "tbh" : "to be held",
    "wtf" : "what the fuck",
    "wth" : "what the hell"
}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST,PORT))
print("cooking...")

while True:
    data, add = server.recvfrom(1024)
    s = data.decode()
    words = s.split()
    result = []
    for word in words:
        punc = ""
        if word[-1] in ", . ! ?":
            punc = word[-1]
            word = word[:-1]
        if word.lower() in dict:
            trans = dict[word.lower()]
        else:
            trans = word
        result.append(trans + punc)
    transs = " ".join(result)
    print("rec : ", s)
    print("transe : ", transs)
    server.sendto(transs.encode(), add)