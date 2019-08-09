import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server.settimeout(0.2)
server.bind(("", 1454))
message = b"Hello From UDP"
while True:
    server.sendto(message, ('<broadcast>', 3000))
    print("message sent!")
    time.sleep(1)