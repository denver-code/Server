import socket
s = socket.socket()
ipf = open('sip.txt','r')
ip = ipf.read()
host = str(ip)
port = 25758
s.connect((host, port))
filen = open('filename.txt', 'r')
filename = filen.read()
filen.close()
op = open(filename, 'rb')
while (True):
    data = op.read(1024)
    if not data:
        print('Complete!')
        exit()
    s.send(data)
op.close()
s.shutdown(socket.SHUT_WR)
