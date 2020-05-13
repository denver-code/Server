#!/usr/bin/env python3
'''
Code writed by Igorek's
Credits:
    -Twitter @Igoreks3
    -Instagram @igorek_savenko
    -Youtube RAMZEES
    -Telegram @pydevops
'''
print('Start a new server!')
import socket
import os
from time import sleep
import datetime
from datetime import date,datetime
import  subprocess
'''Please delete in production!'''
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
pfile = open('values/port.txt','w')
pfile.write(str(PORT))
pfile.close()
print('Port writed to file!'+str(PORT))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    conn, addr = s.accept()
    commands = [helpsecret,h4nb3u8]
    with conn:
        logw = open('log/'+log,'a')
        logw.write('!-----------!New conection!-----------!\n')
        logw.write('Real ip:'+str(addr)+'\n')
        logw.write(('Time:'+str(today)+str('\n')))
        logw.close()
        print('Connected by', addr)
        while True:
            try:
                direc = open('values/directive.d', 'r')
                directive = int(direc.read())
                direc.close()
            except FileNotFoundError:
                direc = open('values/directive.d', 'w')
                direc.write(int(1))
                directive = 1
            data = conn.recv(1024)
            def h4nb3u8():
                conn.sendall(directive.encode())
            def recivehtmlww():
                logw = open('log/'+log,'a')
                logw.write(('User want recive index.html\n'))
                logw.close()
                g = subprocess.Popen(['python3','utilites/recivehtml.py'])
            def recivefile():
                logw = open('log/'+log,'a')
                logw.write(('User want recive file\n'))
                logw.close()
                g = subprocess.Popen(['python3','utilites/recivefile.py'])
                conn.sendall('Complete file recived!'.encode())
            def cleanlog():
                clog = open('log/'+log,'w')
                clog.write('Clean!')
                print('Clear log!')
                conn.sendall('Clean!'.encode())
                clog.close()
            def helps():
                logw = open('log/'+log,'a')
                logw.write(('User want view help\n'))
                logw.close()
                conn.sendall('''Commands:
-send web `Transfer index.html to www folder`
-clear `Clear terminal`
-create server `create a new web server in folder utilites`
-run server `run existing server.py in folder utilites.py`
-kill server `kill web server`
-time `print time`
-clean log `clean a today log-file`
-restart `restart socket server and web server`
-send file `send file =)`
'''.encode())
            def runwebserver():
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
            def killwebserver():
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
            def createwebserver():
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
                conn.sendall(str('SCI:'+HOST).encode())
            def sendtime():
                logw = open('log/'+log,'a')
                logw.write(('User chech time\n'))
                logw.close()
                conn.sendall(str(timel).encode())
            if not data:
                print('Break no data!')
                print('Clean up')
                break
            print('Get-data:',data)

            '''Grab data : ip/hostname/platform'''
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

                '''End grabing data : ip/hostname/platform'''
                '''Start function sector'''
                    #Recive file
            elif data == b'recivefile':
                directive = 2
                if directive == 2:
                    recivefile()
                else:
                    conn.sendall('Directive is not support'.encode())
                directive = 1
                    #Recive index.html
            elif data == b'webpage':
                directive = 2
                if directive == 2:
                    recivehtmlww()
                else:
                    conn.sendall('Directive is not support'.encode())
                directive = 1
                    #CLEAN LOG
            elif data == b'clear-log':
                if directive == 4:
                    cleanlog()
                else:
                    conn.sendall('Directive is not support'.encode())
                    #TIME
            elif data == b'time':
                sendtime()
                    #CREATE WEB SERVER
            elif data == b'create server':
                if directive == 1:
                    createwebserver()
                else:
                    conn.sendall('Directive is not support'.encode())
                    #KILL WEB SERVER
            elif data == b'kill server':
                if directive == 1:
                    killwebserver()
                else:
                    conn.sendall('Directive is not support'.encode())
                    #RUN WEB SERVER
            elif data == b'run server':
                if directive == 1:
                    runwebserver()
                else:
                    conn.sendall('Directive is not support'.encode())
                    #RESTART SOCKET
            elif data == b'restart':
                conn.sendall(str('Goodbuy').encode())
                break
                    #HECLP COMMAND
            elif data == b'help':
                helps()
            #Top secret
            elif data == b'h4nb3u8':
                h4nb3u8()
           # elif data == b'help321':
                #Always Pass =)
            else:
                #conn.sendall('Incorrect command!'.encode())
                pass
            #conn.sendall(data)
logw = open('log/'+log,'a')
logw.write(('Session deleted\n'))
logw.close()
os.system('python3 server.py')
