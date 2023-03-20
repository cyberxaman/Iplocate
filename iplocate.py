# made by cyberxaman

# modules required
import argparse
import requests, json
import socket
import sys

# arguments and parser
parser = argparse.ArgumentParser()
parser.add_argument("-v", help="target/host IP address", type=str, dest='target')
parser.add_argument("-m", help="get details about your machine", action='store_true')
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

try:
    data = requests.get(api + ip).json() if not args.m else None
    sys.stdout.flush()
    a = lgreen + bold + "[$]"
    b = cyan + bold + "[$]"
    print(a, "[IP Address]:", data['query'] if not args.m else ip)
    print(red + "<--------------->" + red)
    print(b, "[ISP]:", data['isp'] if not args.m else ip)
    print(red + "<--------------->" + red)
    print(a, "[Organisation]:", data['org'] if not args.m else ip)
    print(red + "<--------------->" + red)
    print(b, "[City]:", data['city'] if not args.m else ip)
    print(red + "<--------------->" + red)
    print(a, "[Region]:", data['regionName'] if not args.m else ip)
    print(red + "<--------------->" + red)
    print(b, "[Country]:", data['country'] if not args.m else ip)
    print(red + "<--------------->" + red)
    print(a, "[Longitude]:", data['lon'] if not args.m else ip)
    print(red + "<--------------->" + red)
    print(b, "[Latitude]:", data['lat'] if not args.m else ip)
    if args.m:
        url = f"https://www.google.com/maps/place/{data['lat']},{data['lon']}"
        print(red + "<--------------->" + red)
        print(a, "[Google Maps URL]:", url)
    else:
        url = f"https://www.google.com/maps/place/{data['lat']},{data['lon']}"
        print(red + "<--------------->" + red)
        print(a, "[Google Maps URL]:", url)
    print(" " + yellow)
except KeyboardInterrupt:
    print('Terminating, Bye' + lgreen)
    sys.exit(0)
except requests.exceptions.ConnectionError as e:
    print(red + "[~]" + " check your internet connection!" + clear)
    sys.exit(1)
