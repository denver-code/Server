import re
import requests
from bs4 import BeautifulSoup
import  subprocess
def parse_server():
    url = 'https://pastebin.com/raw/QwmmM4UC'
    r = requests.get(url)
    with open('test.update', 'w') as output_file:
        output_file.write(r.text)
        script = open('server.py', 'w')
        script.write(r.text)
    print('Downloaded')
def parse_creator():
    url = 'https://pastebin.com/raw/'
    r = requests.get(url)
    with open('testcr.update', 'w') as output_file:
        output_file.write(r.text)
        script = open('creator.py', 'w')
        script.write(r.text)
    print('Downloaded')
def backup():
    exist_script = open('server.py', 'r')
    tovalid = exist_script.read()
    exist_script.close()
    backup_s = open('server_bak.py', 'w')
    backup_s.write(str(tovalid))
    print('Backup Complete!')
if __name__ == '__main__':
    backup()
    parse_server()
    parse_creator()