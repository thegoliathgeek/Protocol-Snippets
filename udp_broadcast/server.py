import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 4000)
address_array = []
sock.bind(server_address)
while True:
    data, addr = sock.recvfrom(1024)
    if addr not in address_array:
        address_array.append(addr)
    for i in address_array:
        sock.sendto('Hello From UDP Broad Cast'.encode('utf8'), i)
