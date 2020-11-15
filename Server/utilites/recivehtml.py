print('Start reciving')
import socket
mip = open('values/mip.txt','r')
print(mip.read())
s = socket.socket()
host =  str(mip.read())
port = 25695
s.bind((host, port))
f = open('www/index.html','wb')
s.listen(5)
while True:
    c, addr = s.accept()
    print ('Got connection from', addr)
    print ("Receiving...")
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
