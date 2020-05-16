print('Start reciving file')
import socket
s = socket.socket()

s.setsockopt(socket.SOL_SOCKET,
socket.SO_REUSEADDR, 1)
mip = open('values/mip.txt','r')
print(mip.read())
host =  str(mip.read())
port = 25758
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
filen = open('values/filename.txt' 'r')
filename = filen.read()
filen.close()
op = open('File/'+str(filename), 'wb') 
while 1:
    data = conn.recv(1024)
    if not data:
        exit()
    op.write(data)
op.close()
