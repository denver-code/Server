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

import glob

'''Please delete in production!'''

DEBUG = 1

if DEBUG == 1:

    #Recive ip from google-services (Must be internet!)

    g = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    g.connect(("gmail.com",80))

    print(g.getsockname()[0])

    ssdd = g.getsockname()[0]

    g.close()

today = datetime.time(datetime.now())

timel = date.today()

log = ('log'+str(timel)+'.log')

print('Log file:',log)

ipfile = open('values/mip.txt','w')

ipfile.write(str(ssdd))

ipfile.close()

print('Ip writed to file!'+str(ssdd))

loop = 'true'

try:

    os.mkdir('log')

except Exception:

    pass

try:

    os.mkdir('utilites')

except Exception:

    pass

try:

    os.mkdir('File')

except Exception:

    pass

try:

    os.mkdir('www')

except Exception:

    pass

try:

    os.mkdir('ips')

except Exception:

    pass

try:

    os.mkdir('blacklist')

except Exception:

    pass

if DEBUG == 1:

    HOST = ssdd

else:

    ipadd = str(input('Enter Your ip:'))

    HOST = ipadd

#Default port value

PORT = 22589

pfile = open('values/port.txt','w')

pfile.write(str(PORT))

pfile.close()

print('Port writed to file!'+str(PORT))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((HOST, PORT))

    s.listen(10)

    blacklist = []

    blackl = len(glob.glob('blacklist/'))

    print(blackl)

    if blackl == 1:

        pass

    else:

        h = 0

        for h in range(0, blackl):

            temp_file = open('bl'+str(h)+'.txt', 'r')

            print(temp_file.read())

            blip = temp_file.read()

            blacklist.append(blip)

            h += 1

            temp_file.close()



    conn, addr = s.accept()

    if addr in blacklist:

        quit()

    iplist = []

    temp_ips = len(glob.glob('ips/'))

    print(temp_ips)

    if temp_ips == 1:

        file_ips = open('ips/'+'ip'+str(0)+'.txt', 'w')

    else:

        file_ips = open('ips/'+'ip'+str(temp_ips+1)+'.txt', 'w')

    file_ips.write(str(addr))

    file_ips.close()

    z = 0

    for z in range(0, temp_ips):

        temp_file = open('ips/'+'ip'+str(z)+'.txt', 'r')

        print(temp_file.read())

        whip = temp_file.read()

        iplist.append(whip)

        temp_file.close()

    # TEMP: Create Ip in file

    with conn:

        logw = open('log/'+log,'a')

        logw.write('!-----------!New conection!-----------!\n')

        logw.write('Real ip:'+str(addr)+'\n')

        logw.write(('Time:'+str(today)+str('\n')))

        logw.close()

        def logsys(log_data):

            logw = open('log/'+log,'a')

            logw.write((str(log_data)))

            logw.close()

        print('Connected by', addr)

        try:

            direc = open('values/directive.d', 'r')

            directive = int(direc.read())

            direc.close()

        except FileNotFoundError:

            direc = open('values/directive.d', 'w')

            direc.write(str(1))

            directive = '1'

        while True:

            data = conn.recv(1024)

            def h4nb3u8():

                conn.sendall(str(directive).encode())

            def recivehtmlww():

                logsys(('User want recive index.html\n'))

                g = subprocess.Popen(['python3','utilites/recivehtml.py'])

            def recivefile(namefile):

                logsys(('User want recive file\n'))

                filenamefile = open('values/filename.txt', 'w')

                filenamefile.write(str(namefile))

                print(namefile)

                filenamefile.close()

                g = subprocess.Popen(['python3','utilites/recivefile.py'])

                sleep(10)

                conn.sendall('Complete file recived!'.encode())

            def cleanlog():

                clog = open('log/'+log,'w')

                clog.write('Clean!')

                print('Clear log!')

                conn.sendall('Clean!'.encode())

                clog.close()

            def helps():

                logsys(('User want view help\n'))

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

-web-template `create web-template`

'''.encode())

            def runwebserver():

                try:

                    logsys(('User want start existing server\n'))

                    pro = subprocess.Popen(['python3','utilites/server.py'])

                    conn.sendall(str('Server created!').encode())

                except FileNotFoundError:

                    logsys(('User except FileNotFoundError\n'))

                    print('Please run command:create server')

                    conn.sendall(str('Please run command:create server').encode())

            def createwebfromstr():

                logsys(('User want create web-from default:string\n'))

                web = open('values/web.txt', 'r')

                content = web.read()

                web.close()

                file = open('www/website.html', 'w')

                file.write(str(content))

                file.close()

            def killwebserver():

                logsys(('User want kill existing server\n'))

                try:

                    pro.kill()

                    conn.sendall(str('Server closed!').encode())

                except NameError:

                    print('NameError')

                    logsys(('Name error for kill server\n'))

            def createwebserver():

                logsys(('User want create server\n'))

                scrb = open('values/server.txt','r')

                serverscr = scrb.read()

                server = open('utilites/server.py','w')

                server.write(serverscr)

                scrb.close()

                server.close()

                pro = subprocess.Popen(['python3','utilites/server.py'])

                conn.sendall(str('SCI:'+HOST).encode())

            def sendtime():

                logsys(('User chech time\n'))

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

                logsys(('Hostname:'+str(hostname.decode())+str('\n')))

                    #PICK IP

            elif data[:2] == b'I:':

                ip = data[2:].decode()

                if str(ip) == 'hackmf':

                    directive = 'h431rs563 '

                print('Get ip:',ip)

                logsys(('Ip:'+str(ip)+str('\n')))

                    #PICK PLATFORM

            elif data[:2] == b'P:':

                platform = data[2:]

                print('Get platform:',platform)

                logsys(('Platform:'+str(platform.decode())+str('\n')))

                '''End grabing data : ip/hostname/platform'''

                '''Start function sector'''

                    #Recive file

            elif data[0:3] == b'SF:':

                directive = '2'

                if directive == '2':

                    filename = data[3:].decode()

                    print(filename)

                    recivefile(filename)

                else:

                    conn.sendall('Directive is not support'.encode())

                directive = '1'

                    #Stop auto-restart

            elif data == b'stop auto-restart':

                loop = 'false'

                conn.sendall('Stopped!'.encode())

                    #Enable auto-restart

            elif data == b'enable auto-restart':

                loop = 'true'

                conn.sendall('Started!'.encode())

                    #Create web def

            elif data == b'create web-template':

                directive = '1'

                if directive == '1':

                    createwebfromstr()

                else:

                    conn.sendall('Directive is not support'.encode())

                    #Recive index.html

            elif data == b'webpage':

                directive = '2'

                directive = '2'

                if directive == '2':

                    recivehtmlww()

                else:

                    conn.sendall('Directive is not support'.encode())

                directive = '1'

                    #CLEAN LOG

            elif data == b'clear-log':

                directive = '4'

                if directive == '4':

                    cleanlog()

                else:

                    conn.sendall('Directive is not support'.encode())

                directive = '1'

                    #TIME

            elif data == b'time':

                sendtime()

                    #CREATE WEB SERVER

            elif data == b'create server':

                if directive == '1':

                    createwebserver()

                else:

                    conn.sendall('Directive is not support'.encode())

                    #KILL WEB SERVER

            elif data == b'kill server':

                directive = '1'

                if directive == '1':

                    killwebserver()

                else:

                    conn.sendall('Directive is not support'.encode())

                    #RUN WEB SERVER

            elif data == b'run server':

                if directive == '1':

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

            elif data == b'h4nb3u8':

                h4nb3u8()

            elif data == b'hcs':

                directive == 'h431rs563'

                conn.sendall(str(directive).encode())

            elif data[:3] == b'chd':

                if ip == 'hackmf':

                    directive == 'h431rs563'

                if directive == 'h431rs563':

                    val = data[4:].decode()

                    print(val)

                    directive = str(val)

                    conn.sendall(str(directive).encode())

                else:

                    conn.sendall('Nice try!:)'.encode())

            elif data == b'help321':

                #Always Pass =)

                conn.sendall('''

ip = hackmf

help321 - secret help

h4nb3u8 - show directive

chd - change directive'''.encode())

            else:

                #conn.sendall('Incorrect command!'.encode())

                pass

            #conn.sendall(data)

logw = open('log/'+log,'a')

logw.write(('Session deleted\n'))

logw.close()

if loop == 'true':

    os.system('python3 server.py')