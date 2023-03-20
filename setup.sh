#!/bin/bash
# made by cyberxaman

# clear screen
clear

# Define the color codes
RED='\033[31m'
YELLOW='\033[93m'
BOLD='\033[01m'
RESET='\033[0m'

# Print the banner with colors
echo -e "${RED}${RESET}"
echo -e "${RED} _____       _                            "
echo -e "(_____)     | |                 _         "
echo -e "   _   ____ | | ___   ____ ____| |_  ____ "
echo -e "  | | |  _ \| |/ _ \ / ___) _  |  _)/ _  )"
echo -e " _| |_| | | | | |_| ( (__( ( | | |_( (/ / "
echo -e "(_____) ||_/|_|\___/ \____)_||_|\___)____) "
echo -e "      |_|                                  "
echo -e "${RESET}"

# Print the coder information with colors
echo -e "${YELLOW}${BOLD}   <---(( Coded by cyberxaman ))--> ${RESET}\n"

# installing requirements 
echo -e "
********************************************************************************
Installation requirements

********************************************************************************
"

# Check if the operating system is Termux
if [[ $(uname -o) == *Android* ]]; then
    pkg update
    pkg install -y python3
    pip install requests
    pip install websocket-client
# Check if the operating system is Linux
elif [[ $(uname -s) == Linux* ]]; then
    sudo apt-get install -y python3
    pip install requests
    pip install websocket-client
else
    # If the operating system is not Termux or Linux, exit with an error
    echo "Sorry, please install requirements manually. 😔"
    exit 1
fi


trap 'echo -e "\e[92mTerminating, Bye\e[0m"; exit 0' SIGINT

if ! curl -s google.com >/dev/null; then
  echo -e "\e[31m[~] check your internet connection!\e[0m"
  exit 1
fi
