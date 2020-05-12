#!/usr/bin/env python3
print('Start a new server!')
import socket
import os
from time import sleep
import datetime
from datetime import date,datetime
import  subprocess
DEBUG = 1
if DEBUG == 1:
    g = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    g.connect(("gmail.com",80))
    print(g.getsockname()[0])
    ssdd = g.getsockname()[0]
    g.close()
ips = socket.gethostbyname(socket.gethostname())
today = datetime.time(datetime.now())
timel = date.today()
log = ('log'+str(timel)+'.log')
print('Log file:',log)
ipfile = open('values/mip.txt','w')
ipfile.write(str(ssdd))
ipfile.close()
print('Ip writed to file!'+str(ssdd))
try:
    os.mkdir('log')
    os.mkdir('utilites')
except Exception:
    pass
if DEBUG == 1:
    HOST = ssdd
else:
    ipadd = str(input('Enter Your ip:'))
    HOST = ipadd
PORT = 22589
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()
    with conn:
        logw = open('log/'+log,'a')
        logw.write('!-----------!New conection!-----------!\n')
        logw.write('Real ip:'+str(addr)+'\n')
        logw.write(('Time:'+str(today)+str('\n')))
        logw.close()
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                print('Break no data!')
                print('Clean up')
                break
            print('Get-data:',data)
            #PICK HOSTNAME
            if data[:2] == b'H:':
                hostname = data[2:]
                print('Get Host-Name:',hostname)
                logw = open('log/'+log,'a')
                logw.write(('Hostname:'+str(hostname.decode())+str('\n')))
                logw.close()
                #PICK IP
            elif data[:2] == b'I:':
                ip = data[2:]
                print('Get ip:',ip)
                logw = open('log/'+log,'a')
                logw.write(('Ip:'+str(ip.decode())+str('\n')))
                logw.close()
                #PICK PLATFORM
            elif data[:2] == b'P:':
                platform = data[2:]
                print('Get platform:',platform)
                logw = open('log/'+log,'a')
                logw.write(('Platform:'+str(platform.decode())+str('\n')))
                logw.close()
                #Recive index.html
            elif data == b'webpage':
                logw = open('log/'+log,'a')
                logw.write(('User want recive index.html\n'))
                logw.close()
                g = subprocess.Popen(['python3','values/recive.py'])
                conn.sendall('Complete file started!Go to ip/www/'.encode())
                #LOG VIEW
            elif data == b'logw':
                logw = open('log/'+log,'a')
                logw.write(('User want view log\'s\n'))
                logw.close()
                print('Command log viewer')
                catlog = open(str('log/')+log,'r')
                catval = catlog.read()
                print(catval)
                conn.sendall(catval.encode())
                #CLEAN LOG
            elif data == b'clear-log':
                clog = open('log/'+log,'w')
                clog.write('Clean!')
                print('Clear log!')
                conn.sendall('Clean!'.encode())
                clog.close()             
                #TIME
            elif data == b'time':
                logw = open('log/'+log,'a')
                logw.write(('User chech time\n'))
                logw.close()
                conn.sendall(str(timel).encode())
                #CREATE WEB SERVER
            elif data == b'create server':
                logw = open('log/'+log,'a')
                logw.write(('User want create server\n'))
                logw.close()
                scrb = open('values/server.txt','r')
                serverscr = scrb.read()
                server = open('utilites/server.py','w')
                server.write(serverscr)
                scrb.close()
                server.close()
                pro = subprocess.Popen(['python3','utilites/server.py'])
                #subprocess.Popen(['python -m SimpleHTTPServer 8000'])
                #os.system('python -m SimpleHTTPServer 8000')
                conn.sendall(str('SCI:'+HOST).encode())
                #KILL WEB SERVER
            elif data == b'kill server':
               logw = open('log/'+log,'a')
               logw.write(('User want kill existing server\n'))
               logw.close()
               try:
                pro.kill()
                conn.sendall(str('Server closed!').encode())
               except NameError:
                print('NameError')
                logw = open('log/'+log,'a')
                logw.write(('Name error for kill server\n'))
                logw.close()
               #RUN WEB SERVER
            elif data == b'run server':
                try:
                    logw = open('log/'+log,'a')
                    logw.write(('User want start existing server\n'))
                    logw.close()
                    pro = subprocess.Popen(['python3','utilites/server.py'])
                    conn.sendall(str('Server created!').encode())
                except FileNotFoundError:
                    logw = open('log/'+log,'a')
                    logw.write(('User except FileNotFoundError\n'))
                    logw.close()
                    print('Please run command:create server')
                    conn.sendall(str('Please run command:create server').encode())
                    #RESTART SOCKET
            elif data == b'restart':
                conn.sendall(str('Goodbuy').encode())
                break
            #HECLP COMMAND
            elif data == b'help':
                logw = open('log/'+log,'a')
                logw.write(('User want view help\n'))
                logw.close()
                conn.sendall('''Commands:
-clear `Clear terminal`
-create server `create a new web server in folder utilites`
-run server `run existing server.py in folder utilites.py`
-kill server `kill server`
-time `print time`
-clean log `clean a today log-file`
-restart `restart socket server and web server`
'''.encode())
#-logw `Read current log file` DELETED

            else:
                conn.sendall('Incorrect command!'.encode())
            #conn.sendall(data)
logw = open('log/'+log,'a')
logw.write(('User exit\n'))
logw.close()
os.system('python3 server.py')
