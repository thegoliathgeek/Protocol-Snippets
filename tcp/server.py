import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_addr = ('localhost', 3000)
print('starting up on %s port : ', my_addr)
sock.bind(my_addr)
sock.listen(1)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        while True:
            data = connection.recv(16)
            print('received : ', data)
            if data:
                print('sending back to client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break

    finally:
        connection.close()
