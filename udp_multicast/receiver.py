import socket
import struct

multicast_ip = '224.9.9.9'
server_address = ('', 3333)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(server_address)

group = socket.inet_aton(multicast_ip)
print(socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, struct.pack('4sL', group, socket.INADDR_ANY))
while True:
    data, address = sock.recvfrom(1024)
    print(f'Data : {data} ------  Address : {address}')
    sock.sendto('ack'.encode('ascii'), address)   #Acc
