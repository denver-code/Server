print('Start reciving file')
import socket
mip = open('values/mip.txt','r')
print(mip.read())
s = socket.socket()
host =  str(mip.read())
port = 25758
s.bind((host, port))
s.listen(1)
while True:
    c, addr = s.accept()
    data = c.recv(1024)
    if data[:3] == b'N:':
        filename = data[3:]
    if data[:3] == b'F:':
        format = data[3:]
    print ('Got connection from', addr)
    f = open('File/'+filename+'.'+format+'','wb')
    l = c.recv(1024)
    while (l):
        print ("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print ("Done Receiving")
    c.send('Thank you for connecting')
    c.close()
    break
