import socket
from time import sleep
request_text = """\
GET /posts/1 HTTP/1.1\r\n\
Host: jsonplaceholder.typicode.com:80\r\n\
User-Agent: search4.py (Foundations of Python Network Programming)\r\n\
Connection: close\r\n\
\r\n\
"""
def geocode():
    sock = socket.socket()
    sock.connect(('jsonplaceholder.typicode.com', 80))
    request = (request_text)
    sock.sendall(request.encode('ascii'))
    sleep(2)
    raw_reply = b''
    while True:
        more = sock.recv(4096)
        print(len(more))
        if not more:
            break
        raw_reply += more
        print(raw_reply.decode('utf-8'))
if __name__ == '__main__':
    geocode()