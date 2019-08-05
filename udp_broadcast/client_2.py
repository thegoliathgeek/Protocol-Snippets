import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 4000)
message = 'Hello from UDP'
sock.sendto('Client 2'.encode('utf8'), server_address)
while True:
    try:
        data, server = sock.recvfrom(1024)
        print(data)

    except Exception as e:
        print(e)
