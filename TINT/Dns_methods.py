import requests
import json
import socket
import whois
import dns.resolver
import re


url="https://admin.google.com"
domain="google.com"



class Dns:
        #To check Live hosts
        @staticmethod
        def is_host_alive(domain, port=80, timeout=1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(timeout)
                    result = sock.connect_ex((domain, port))
                    return result == 0
            except socket.error:
                return False

        @staticmethod
        #Fetch Subdomains from Crt_sh 
        def crt_sh(domain):
            try:
                #url of crt.sh that gives a subdomains
                url=f"https://crt.sh/?q={domain}&output=json"

                #send requests and find store as response
                response=requests.get(url)

                #load json data
                data=json.loads(response.text)

                #find common_name from response
                subdomains=[entry['common_name'] for entry in data]

                #exclude duplicate subdomains
                unique_subdomains = list(set(subdomains))

                #print output of all subdomains
                for sub in unique_subdomains:
                    print(sub)
            except Exception as e:
                    print(f"Error: {e}")

        @staticmethod
        # Brute force function for find subdomains
        def brute_force(domain,wordlists):
            with open(wordlists, "r") as f:
                wordlist = f.read().split()
                
            for word in wordlist:
                full_domain = f"{word}.{domain}"
                if Dns.is_host_alive(full_domain):
                    print(f"[+] Found: {full_domain}")

        @staticmethod
        #Function for find redirection and history 

        def find_redirection(url):

            try:
                response=requests.get(url,allow_redirects=True,timeout=5)
                if response.history:
                    print("Redirection chain:")
                    for resp in response.history:
                        print(f"{resp.status_code} -> {resp.url}")
                    print(f"Final URL:{response.url}")
                    return response.url
                else:
                    print("no redirects.")
                    return domain
            except requests.RequestException as e:
                print(F"Error-> {e} ")
                return None

        @staticmethod
        def status_code_checker(url, code):
                try:
                    response = requests.get(url, timeout=5)
                    if response.status_code == code:
                        result = f"{url} -> {response.status_code}"
                        print(result)
                except requests.RequestException as e:
                    print(f"Failed to connect to {url}: {e}")
        

            
        @staticmethod
        #Find whois information for domain
        def get_whois_data(domain):
            try:
                data = whois.whois(domain)
                result = {
                    "domain": data.domain_name,
                    "registrar": data.registrar,
                    "creation_date": data.creation_date,
                    "expiration_date": data.expiration_date,
                    "updated_date": data.updated_date,
                    "status": data.status,
                    "name_servers": data.name_servers,
                    "emails": data.emails,
                    "whois_server": data.whois_server
                }
                return result
            except Exception as e:
                return {"error": str(e)}

        #This function is use for dns resolver
        def get_dns_info(domain):

            dns_info = {}

            try:
                print(f"\n🔍 DNS Recon for: {domain}")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

                # A Records (IP Address)
                print("🌐 A Records:")
                try:
                    a_records = dns.resolver.resolve(domain, 'A')
                    dns_info['A Record'] = [ip.address for ip in a_records]
                    for ip in dns_info['A Record']:
                        print(f"   └─ {ip}")
                except dns.resolver.NoAnswer:
                    print("   └─ No A records found.")

                # MX Records (Mail Servers)
                print("\n📧 MX Records:")
                try:
                    mx_records = dns.resolver.resolve(domain, 'MX')
                    dns_info['MX Records'] = [(mx.preference, mx.exchange.to_text()) for mx in mx_records]
                    for pref, exch in dns_info['MX Records']:
                        print(f"   └─ {exch} (Preference: {pref})")
                except dns.resolver.NoAnswer:
                    print("   └─ No MX records found.")

                # NS Records (Name Servers)
                print("\n📘 NS Records:")
                try:
                    ns_records = dns.resolver.resolve(domain, 'NS')
                    dns_info['NS Records'] = [ns.to_text() for ns in ns_records]
                    for ns in dns_info['NS Records']:
                        print(f"   └─ {ns}")
                except dns.resolver.NoAnswer:
                    print("   └─ No NS records found.")

                # CNAME Records
                print("\n🔁 CNAME Records:")
                try:
                    cname_records = dns.resolver.resolve(domain, 'CNAME')
                    dns_info['CNAME Records'] = [cname.to_text() for cname in cname_records]
                    for cname in dns_info['CNAME Records']:
                        print(f"   └─ {cname}")
                except dns.resolver.NoAnswer:
                    print("   └─ No CNAME record found.")

                # TXT Records
                print("\n📝 TXT Records:")
                try:
                    txt_records = dns.resolver.resolve(domain, 'TXT')
                    dns_info['TXT Records'] = [txt.to_text() for txt in txt_records]
                    for txt in dns_info['TXT Records']:
                        print(f"   └─ {txt}")
                except dns.resolver.NoAnswer:
                    print("   └─ No TXT records found.")

                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
                return dns_info

            except dns.resolver.NXDOMAIN as e:
                print(f"❌ Domain does not exist: {str(e)}")
                return {'error': f"Domain does not exist: {str(e)}"}
            except Exception as e:
                print(f"⚠️  DNS query failed: {str(e)}")
                return {'error': f"DNS query failed: {str(e)}"}


        #reverse_dns i.e IP to Domain and Domain to IP 
        @staticmethod
        def reverse_dns(ip):
            strict_ip_pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|1?\d{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|1?\d{1,2})\b"

            try:
                matches=re.findall(strict_ip_pattern,ip)
                if matches: 
                    host_info = socket.gethostbyaddr(ip)
                    return host_info[0] 
                else:
                    host_info = socket.gethostbyname(ip)
                    return host_info
            except socket.herror:
                return "No PTR record found."


