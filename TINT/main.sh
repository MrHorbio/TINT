#!/bin/bash



cat << "EOF"
                                    ████████╗██╗███╗░░██╗████████╗
                                    ╚══██╔══╝██║████╗░██║╚══██╔══╝
                                    ░░░██║░░░██║██╔██╗██║░░░██║░░░
                                    ░░░██║░░░██║██║╚████║░░░██║░░░
                                    ░░░██║░░░██║██║░╚███║░░░██║░░░
                                    ░░░╚═╝░░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░
EOF
echo -e "                                  Developed By: Ankush Kumar Rajput\n      "
echo -e "                                           Discription           "
echo -e " TINT stands for 'Target information gathering tool'. It helps to automate your task and helps to gather informtaion from internet.\n Features:\n + Subdomains Enumeration           + Port Scanning\n + Finding Redirections             + Filter subdomains based on status code\n + Dns resolver                     + Reverse DNS\n + WHOIS Lookup \n  "

#check if the script is run as root
if [ $EUID -ne 0 ]; then 

    echo "Please run this script as root or use sudo."
    exit 1
fi

