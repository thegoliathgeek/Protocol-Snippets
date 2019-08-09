import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 3000))
print('Listening at {}'.format(sock.getsockname()))
while True:
    data, address = sock.recvfrom(65535)
    text = data.decode('ascii')
    print('Response from {} says: {}'.format(address, text))
