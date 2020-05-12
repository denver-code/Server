import socket             
s = socket.socket()
ipf = open('sip.txt','r')
ip = ipf.read()
host = str(ip)
port = 25695
s.connect((host, port))
f = open('index.html','rb')
print ('Sending...')
l = f.read(1024)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print ("Done Sending")
print (s.recv(1024))
s.close  