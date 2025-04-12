import requests
import json
import socket
domain="google.com"


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





def is_host_alive(domain, port=80 or 443, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((domain, port))
            return result == 0
    except socket.error:
        return False
    


def brute_force(wordlist):
    url=f"{wordlist}.{domain}"

    # Example usage
    if is_host_alive(url):
        print(f"{url} is up!")
    else:
        print(f"{url} seems to be down or blocking port 80.")

 
with open("wordlists.txt","r") as f:
    wordlists=f.read.split()
    for wordlist in wordlists:
        brute_force(wordlist)
