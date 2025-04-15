import random
import Dns_methods
import port_scanner

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

def main():
    banners = get_banners()
    print(random.choice(banners))
    print_description()


def scanner(domain,port,filename):
    result = port_scanner.open_ports(domain,port)
    if filename:
        with open(filename,"w") as f:
            f.write(result)




if __name__ == "__main__":
    main()
