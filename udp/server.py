import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)
sock.bind(server_address)
while True:
    data, address = sock.recvfrom(1024)
    print('Data : ', data)
    if data:
        sent = sock.sendto(data, address)
