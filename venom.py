#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import os
import random
from colorama import Fore

os.system('clear')
w = Fore.WHITE
g = Fore.GREEN
r = Fore.RED
b = Fore.BLUE
c = Fore.CYAN
y = Fore.YELLOW

colors = (w, g, r, b, c, y)
color = random.choice(colors)

banner = '''

██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗      ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║      ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║█████╗██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝

     [+] Created By Venom
     [+] Instagram: i.m.gauravchaudhary
     [+] Whatsapp: +91 9910332273


'''
print(color + banner + color)
tool = input(w + '    [+] ' + w + color + 'Enter the Attack/Tool/Type of tool you want to download: ' + color)
url = 'https://www.google.com/search?q=site:github.com+' + tool
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
ok = soup.find_all('div', class_='kCrYT')
ok = str(ok)
new = re.findall('<a href="(.*?)"', ok)
new_link = len(new)
tools = []
x = 0
print(' ')
if new_link > 1:
    for i in new:
        i = str(i)
        if i.startswith('/url?q=') is True:
            i = i[7:-100]
            print(w + '     [' + w + y +str(x) + y + w + '] ' + w + color + i + color)
            tools.append(i)
            x += 1
        else:
            pass
else:
    pass
print(' ')
choice = int(input(w + '     [+] ' + w + color + 'Enter the tool number you want to download: ' + color))
print(' ')
def download(num):
    _tool = str(tools[num])
    os.system('git clone ' + _tool)
download(choice)
