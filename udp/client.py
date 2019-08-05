import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 4000)
message = 'Hello from UDP'

try:

    sent = sock.sendto(message.encode('utf8'), server_address)
    data, server = sock.recvfrom(1024)

except Exception as e:
    print(e)

finally:
    sock.close()
