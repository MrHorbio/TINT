import random
from Dns_methods import Dns
import port_scanner
import argparse

def get_banners():
    return [
        r"""
     _______  _______  __   __  _______ 
    |       ||       ||  |_|  ||       |
    |    _  ||   _   ||       ||  _____|
    |   |_| ||  | |  ||       || |_____ 
    |    ___||  |_|  ||       ||_____  |
    |   |    |       || ||_|| | _____| |
    |___|    |_______||_|   |_||_______|

     Target Information Gathering Tool (TINT)
        """,
         r'''
 ████████╗██╗███╗   ██╗████████╗     ████████╗██╗███╗   ██╗████████╗
 ╚══██╔══╝██║████╗  ██║╚══██╔══╝     ╚══██╔══╝██║████╗  ██║╚══██╔══╝
    ██║   ██║██╔██╗ ██║   ██║           ██║   ██║██╔██╗ ██║   ██║   
    ██║   ██║██║╚██╗██║   ██║           ██║   ██║██║╚██╗██║   ██║   
    ██║   ██║██║ ╚████║   ██║           ██║   ██║██║ ╚████║   ██║   
    ╚═╝   ╚═╝╚═╝  ╚═══╝   ╚═╝           ╚═╝   ╚═╝╚═╝  ╚═══╝   ╚═╝  
    ''',
        r"""
       ______________________________
      |                              |
      |     [TINT LAUNCH TERMINAL]   |
      |______________________________|
         \ ^__^
          (oo)\_______
          (__)\       )\/\
              ||----w |
              ||     ||

      Target Info Gathering Tool - by Ankush Kumar Rajput
        """,
        r"""
      ____ _____ _   _ _____ 
     |_   _|_   _| \ | |_   _|
       | |   | | |  \| | | |  
       | |   | | | |\  | | |  
      _| |_ _| |_|_| \_|_| |_ 
     |_____|_____|           
     
     TINT: Target Info Gathering Tool
        """,
        r"""
        ____________
       / ____/ ____/
      / /_  / /_     
     / __/ / __/     
    /_/   /_/        
    ------------------
    TINT - Terminal Recon Tool
    by Ankush Kumar Rajput
        """,
        r"""
     __________________________
    < Gathering intelligence... >
     --------------------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||

    TINT | Subdomains | DNS | WHOIS | Ports | Redirects
        """
    ]

def print_description():
    description = '''
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 Developed By: Ankush Kumar Rajput
📌 Description:
TINT stands for 'Target information gathering tool'. It helps to automate 
your task and gather valuable information from the internet.

🔍 Features:
 + Subdomains Enumeration           + Port Scanning
 + Finding Redirections             + Filter subdomains by status code
 + DNS Resolver                     + Reverse DNS
 + WHOIS Lookup                     + And more...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''
    print(description)

def main2():
    banners = get_banners()
    print(random.choice(banners))
    print_description()


def scanner(domain,port,filename):
    result = port_scanner.open_ports(domain,port)
    if filename:
        with open(filename,"w") as f:
            f.write(result)


def  host_discovery(domain,timeout=None):
    t = timeout if timeout else 5 
    
    result = Dns.is_host_alive(domain,port=80,timeout=t)
    if result:
        print(f"✔️  {domain} -> host is up")





# CLI Setup 
def main():

        #show banner 
    main2()


    parser = argparse.ArgumentParser(description="TINT - Target Information Gathering Tool")
    subparsers = parser.add_subparsers(dest='command',metavar='')


    #Scanner command
    host_parser = subparsers.add_parser('host',help="  Perform host discovery")
    host_parser.add_argument('-d', '--domain', required=True, help='Target domain to scan')
    #host_parser.add_argument('-p', '--port', help='Target port number')
    host_parser.add_argument('-t', '--timeout', type=int, help='Timeout in seconds (default: 5)')
   
    












    

    args = parser.parse_args()  

    


    if args.command == 'host':
        host_discovery(args.domain,args.timeout)
    else:
        parser.print_help()



if __name__ == "__main__":
    main()
