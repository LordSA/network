import socket
import struct

raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Capturing.....")
print("CTRL+c to stop")

try:
    while True:
        packet, add = raw_socket.recvfrom(65535)
        eth_prot = struct.unpack("!H", packet[12:14])[0]
        if eth_prot == 0x0800:
            ip_h = packet[14:34]
            iph = struct.unpack("!BBHHHBBH4s4s", ip_h)
            ttl = iph[5]
            proto = iph[6]
            ip = socket.inet_ntoa(iph[8])
            d_ip = socket.inet_ntoa(iph[9])
            pl = len(packet)

            print(f"SIP : {ip} \nDIP : {d_ip} \nPROTO : {proto}\nTTL : {ttl}\nPL : {pl}\n")
except KeyboardInterrupt:
    print("\nStopped...")
finally:
    raw_socket.close()