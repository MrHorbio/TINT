import requests
import json
import socket
import whois
import dns.resolver

url="https://admin.google.com"
domain="google.com"



class Dns:
        #To check Live hosts
        @staticmethod
        def is_host_alive(domain, port=80 or 443, timeout=1):
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
                for subdomain in unique_subdomains:
                    print(subdomain)
            except Exception as e:
                print(e)

        @staticmethod
        # Brute force function for find subdomains
        def brute_force(wordlists, domain):
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
                print(F"Error: {e}")
                return None

        @staticmethod
        #Function for find all status code of url 
        def status_code_checker(url,code):
            response=requests.get(url,timeout=5)
            if response.status_code==code:
                result =f"{url} -> {response.status_code}"
            
            return result
            
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
                # A Records (IP Address)
                a_records = dns.resolver.resolve(domain, 'A')
                dns_info['A Record'] = [ip.address for ip in a_records]

                # MX Records (Mail Servers)
                mx_records = dns.resolver.resolve(domain, 'MX')
                dns_info['MX Records'] = [(mx.preference, mx.exchange.to_text()) for mx in mx_records]

                # NS Records (Name Servers)
                ns_records = dns.resolver.resolve(domain, 'NS')
                dns_info['NS Records'] = [ns.to_text() for ns in ns_records]

                # CNAME Records (Canonical Names)
                try:
                    cname_records = dns.resolver.resolve(domain, 'CNAME')
                    dns_info['CNAME Records'] = [cname.to_text() for cname in cname_records]
                except dns.resolver.NoAnswer:
                    dns_info['CNAME Records'] = None

                # TXT Records (Text information)
                txt_records = dns.resolver.resolve(domain, 'TXT')
                dns_info['TXT Records'] = [txt.to_text() for txt in txt_records]

                return dns_info

            except dns.resolver.NoAnswer as e:
                return {'error': f"No DNS record found: {str(e)}"}
            except dns.resolver.NXDOMAIN as e:
                return {'error': f"Domain does not exist: {str(e)}"}
            except Exception as e:
                return {'error': f"DNS query failed: {str(e)}"}



                
                


