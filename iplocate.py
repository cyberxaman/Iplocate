#!/bin/python3

# made by cyberxaman

# modules required
import argparse
import os
import requests
import socket
import sys

# arguments and parser
parser = argparse.ArgumentParser()
parser.add_argument("-v", help="target/host IP address and about victim machine", type=str, dest='target')
parser.add_argument("-m", help="get your machine ip (only)", action='store_true')
args = parser.parse_args()

if args.m:
    ip = requests.get('https://api.ipify.org').text
else:
    if not args.target:
        print("Please provide either -m or -v <victim_ip>")
        sys.exit(1)
    ip = args.target

api = "http://ip-api.com/json/"

# colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# clear screen 
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# banner
print(red+"""

 _____       _                            
(_____)     | |                 _         
   _   ____ | | ___   ____ ____| |_  ____ 
  | | |  _ \| |/ _ \ / ___) _  |  _)/ _  )
 _| |_| | | | | |_| ( (__( ( | | |_( (/ / 
(_____) ||_/|_|\___/ \____)_||_|\___)____)
      |_|                                 

"""+red)
print (yellow+bold+"   <---(( Coded by cyberxaman ))--> \n"+clear)


try:
    data = requests.get(api + ip).json() if not args.m else None
    sys.stdout.flush()
    a = lgreen + bold + "[$]"
    b = cyan + bold + "[$]"
    print(a, "[IP Address]:", data['query'] if not args.m else ip)
    if not args.m:
        print(red + "<--------------->" + red)
        print(b, "[ISP]:", data['isp'])
        print(red + "<--------------->" + red)
        print(a, "[Organisation]:", data['org'])
        print(red + "<--------------->" + red)
        print(b, "[City]:", data['city'])
        print(red + "<--------------->" + red)
        print(a, "[Region]:", data['regionName'])
        print(red + "<--------------->" + red)
        print(b, "[Country]:", data['country'])
        print(red + "<--------------->" + red)
        print(a, "[Longitude]:", data['lon'])
        print(red + "<--------------->" + red)
        print(b, "[Latitude]:", data['lat'])
        print(red + "<--------------->" + red)
        print(b, "[Time zone]:", data['timezone'])
        print(red + "<--------------->" + red)
        print(a, "[Zip code]:", data['zip'])
        url = f"https://www.google.com/maps/place/{data['lat']},{data['lon']}"
        print(red + "<--------------->" + red)
        print(a, "[Google Maps URL]:", url)
    else:
        print(" " + yellow)
except KeyboardInterrupt:
    print('Terminating, Bye' + lgreen)
    sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(red + "[~]" + " check your internet connection!" + clear)
    sys.exit(1)
