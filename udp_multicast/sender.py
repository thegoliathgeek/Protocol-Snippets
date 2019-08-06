import socket
import struct

message = 'Hello world it is multicast'
mutli_ip = ('224.9.9.9', 3333)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack('b', 1))

try:

    sent = sock.sendto(message.encode('ascii'), mutli_ip)

    # while True:
    try:
        data, server = sock.recvfrom(16)
    except socket.timeout as e:
        print(e)
        # break
    else:
        print(f'Data : {data} ----- Address : {server}')
finally:
    sock.close()
