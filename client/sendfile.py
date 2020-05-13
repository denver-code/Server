import socket
from time import sleep
s = socket.socket()
ipf = open('sip.txt','r')
ip = ipf.read()
host = str(ip)
port = 25758
s.connect((host, port))
fileformat = str(input('File format[txt/png/jpg]:'))
filename = str(input('Filename no format[index.html >> index]:'))
f = open(filename+'.'+fileformat,'rb')
print ('Sending...')
s.sendall('N:'+filename)
sleep(1)
s.sendall('F:'+fileformat)
l = f.read(1024)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print ("Done Sending")
print (s.recv(1024))
s.close
