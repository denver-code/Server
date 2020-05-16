#Import Sector
import socket
from colorama import Fore, Back, Style
import platform
import re
import os
import uuid
import psutil
from time import sleep
import webbrowser
import subprocess
#Debug sector
DEBUG = 0
#Take info from os
def sysinfo():
    ip = socket.gethostbyname(socket.gethostname())
    arc = platform.machine()
    pver = platform.version()
    plat = platform.platform()
    psys = platform.system()
    proc = platform.processor()
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    hostname = socket.gethostname()
    print('IP:',ip)
    print('Machine:',arc)
    print('Platform version:',pver)
    print('Platform:',plat)
    print('Platform system:',psys)
    print('Proccesor:',proc)
    print('Mac:',mac)
    print('Ram:',ram)
    print('Hostname:',hostname)
sysinfo()
if DEBUG == 1:
    HOST = '192.168.1.110'
else:
    ipadd = str(input('Enter Server ip:'))
    mips = open('sip.txt','w')
    mips.write(str(ipadd))
    mips.close()
    HOST = ipadd
PORT = 22589
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str('H:').encode()+(socket.gethostname()).encode())
    sleep(1)
    s.sendall(str('I:').encode()+(socket.gethostbyname(socket.gethostname())).encode())
    sleep(1)
    s.sendall(str('P:').encode()+(platform.machine()).encode())
    print('Type /exit to exit')
    while 4 != 5:
        send_data = str(input('Command:'))
        if send_data == 'send web':
            s.sendall('webpage'.encode())
            pro = subprocess.Popen(['python','cl.py'])
        if send_data[:9] == 'send file ':
            filename = send_data[9:]
            filen = open('filename.txt', 'w')
            filen.write(str(filename))
            filen.close()
            s.sendall(('SF:'+str(filename)).encode())
            pro = subprocess.Popen(['python','sendfile.py'])
            sleep(5)
        if send_data == 'clear':
            if platform.system() == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
        elif send_data == '/exit':break
        else:
            s.sendall(send_data.encode())
        data = s.recv(1024)
        if data[:4] == b'SCI:':
            webbrowser.open(('http://'+data.decode()[4:]+':8000'), new=0, autoraise=True)
        if data == b'Incorrect command!':
            print('Incorrect command!')
        else:
            print('Get value:\n',data.decode())
