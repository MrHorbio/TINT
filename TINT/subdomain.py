import requests
import json
domain="o7services.com"


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




def get_subdomains():
  
        url = f"https://subdomainfinder.c99.nl/scans/2025-04-10/google.com"
        response=requests.get(url)
        print(response.text)



get_subdomains()