import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_addr = ('localhost', 3000)
print('connecting to %s port : ' , my_addr)
sock.connect(my_addr)
try:
    message = 'Transmitting TCP over TCP'
    print('sending : ' , message)
    sock.sendall(message.encode('utf8'))
    initial = 0
    Total = len(message)
    while initial < Total:
        data = sock.recv(16)
        initial += len(data)
        print(data.decode('utf8'))

finally:
    print('closing socket')
    sock.close()
