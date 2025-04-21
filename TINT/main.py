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

def UI():
    banners = get_banners()
    print(random.choice(banners))
    print_description()


'''def scanner(domain,port,filename):
    result = port_scanner.open_ports(domain,port)
    if filename:
        with open(filename,"w") as f:
            f.write(result)'''

#function for  host discovery 
def  host_discovery(domain,wordlist=None,timeout=None):
    t = timeout if timeout else 5 
    if wordlist:
        for word in wordlist:
            try:
                result = Dns.is_host_alive(word,port=80,timeout=t)
                if result:
                    print(f"✔️  {word}-> host is up")
                else:
                    print(f"❌  {word} -> host is down")
            except Exception as e:
                print(f"⚠️  Error checking {word}: {e}")
    else:
        # Only one domain to check
        try:
            result = Dns.is_host_alive(domain, port=80, timeout=t)
            if result:
                print(f"✔️  {domain} -> host is up")
            else:
                print(f"❌  {domain} -> host is down")
        except Exception as e:
            print(f"⚠️  Error checking {domain}: {e}")


#function for subdomain enumeration

def subdomain(domain,wordlists):
    
    if wordlists:
        print("Brute force is running.... ")
        a = Dns.brute_force(domain,wordlists)
        print(a)
    else:
       print("Fetching Subdomains..... ")
       a = Dns.crt_sh(domain)
       print(a)


#check redirection 
def redirection_checker(url,domainlist):
    try:
        if domainlist:
            with open(domainlist,'r') as file:
                domains = file.read().splitlines()

                for domain in domains:
                    domain = domain.strip()
                    if domain and '.' in domain:
                        url = f"https://{domain}/"
                        try:
                            Dns.find_redirection(url)
                        except Exception as e :
                            print(e)
                        
        else:
            if not url.startswith(("https" or "http")):
                correct_url = f"https://{url}/"
            else:
                correct_url = url
            
            Dns.find_redirection(correct_url)

    except Exception as e:
        print(f"⚠️  Error ->  {e}")


#status code checker

def status_checker(url_or_file, code):
    try:
        # If the input is a file
        if url_or_file.endswith('.txt'):
            with open(url_or_file, "r") as file:
                urls = file.read().split()
        else:
            # Otherwise, treat it as a single URL
            urls = [url_or_file]

        for url in urls:
            Dns.status_code_checker(url, int(code))

    except FileNotFoundError:
        print(f"❌ File '{url_or_file}' not found.")
    except Exception as e:
        print(f"⚠️ Error checking status codes: {e}")


  # Get WHOIS Data
def recon(domain):
    if not domain:
        print("❌ No domain provided for WHOIS lookup.")
        return

    try:
        print(f"🔍 Fetching WHOIS info for: {domain}")
        whois_data = Dns.get_whois_data(domain)
        print(whois_data)
    except Exception as e:
        print(f"⚠️  Error fetching WHOIS data for {domain}: {e}")


#Fetech Dns info
def dns_enum(domain):
    if not domain:
        print("❌ No domain provided for WHOIS lookup.")
        return
    try:
        print(f"🔍 Fetching Dns info for: {domain}")
        dns_data = Dns.get_dns_info(domain)
        print(dns_data)
    except Exception as e:
        print(f"⚠️  Error fetching dns info for {domain}: {e}")



                
   

    
   
        



# CLI Setup 
def main():

    #show banner 
    UI()


    parser = argparse.ArgumentParser(description="TINT - Target Information Gathering Tool")
    subparsers = parser.add_subparsers(dest='command',metavar='')

    #Scanner command
    host_parser = subparsers.add_parser('host',help="  Perform host discovery")
    host_parser.add_argument('-d', '--domain',  help='Target domain to scan',metavar='')
    host_parser.add_argument('-iL','--inputfile',  help='-iL <inputfilename>: Input from list of hosts/networks',metavar='')
    #host_parser.add_argument('-p', '--port', help='Target port number')
    host_parser.add_argument('-t', '--timeout', type=int, help='Timeout in seconds (default: 5)',metavar='')


    '''  #Port Scanner command [ To scan open ports with range and without range ]
    port_parser = subparsers.add_parser('port',help="  Perform port Scanning")
    port_parser.add_argument('-d','--domain',required=True,help="   Target domain to scan",metavar='')
    port_parser.add_argument('-p','--port',required=True,help="  port number[ ex: 21 OR Range-> 1,100 ]",metavar='')
    port_parser.add_argument('-o','--output', help="  output file",metavar='')'''


    #Subdomain enumeration command
    sub = subparsers.add_parser('sub',help="Perform subdomain enumeration")
    sub.add_argument('-d','--domain', required=True,help="Target domain to scan", metavar="")
    sub.add_argument('-w','--wordlists',help="PATH/of/Wordlist",metavar="")


    #find redirections
    red = subparsers.add_parser('redir',help="Perform redirection check ")
    red.add_argument('-u','--url',help="Test redirection on single url",metavar=" ")
    red.add_argument('-iL','--inputfile',help="list of target urls",metavar= " ")

    #status code Checker 
    sc= subparsers.add_parser('code',help="To check status_code for urls OR find redirection url, Forbidden pages")
    sc.add_argument('-u','--url',help="check status code for single url",metavar=" ")
    sc.add_argument('-i','--urlfile',help="Input urls file",metavar=" ")
    sc.add_argument('-c','--status_code',help="put status code 403,200,302 etc.",metavar="")


    #Whois recon
    whois = subparsers.add_parser("whois",help="Fetch whois data")
    whois.add_argument('-d','--domain',required=True,help="Target domain")


    # DNS recon
    dns = subparsers.add_parser("dns", help="DNS Recon (NS, MX, CNAME, A Record, TXT Record)")
    dns.add_argument('-d', '--domain', required=True, help="Target Domain")


    args = parser.parse_args()  

    


    if args.command == 'host':
        wordlist=None
        if args.inputfile:
            with open(args.inputfile) as f:
                wordlist = [line.strip() for line in f if line.strip()]
        host_discovery(args.domain,wordlist,args.timeout)

    #elif args.command == "port":
        #scanner(args.domain,args.port,args.output)

    elif args.command == "sub":
        subdomain(args.domain,args.wordlists)

    elif args.command == "redir":
        redirection_checker(args.url,args.inputfile)

    elif args.command == "code":
     url_input = args.url if args.url else args.urlfile
     if not url_input or not args.status_code:
        print("❌ Please provide either a single URL or a file of URLs along with a status code.")
     else:
        status_checker(url_input, args.status_code)

    elif args.command == "whois":
        recon(args.domain)

    elif args.command == "dns":
        dns_enum(args.domain)

    else:
        parser.print_help()



if __name__ == "__main__":
    main()
