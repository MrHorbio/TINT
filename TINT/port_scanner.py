from Dns_methods import Dns

def open_ports(domain, ports):
    """
    This function checks if ports are open for a given domain. 
    It accepts both single port or a range of ports.
    
    :param domain: The domain to check (e.g., 'example.com')
    :param ports: Either a single port (int) or a range of ports (tuple/list of two integers).
    """
    if isinstance(ports, int):  # Single port
        print(f"Checking port {ports}...")
        if Dns.is_host_alive(domain, ports):
            print(f"[+] Port {ports} is open on {domain}")
        else:
            print(f"[-] Port {ports} is closed on {domain}")
    elif isinstance(ports, tuple) and len(ports) == 2:  # Range of ports
        start_port, end_port = ports
        print(f"Checking ports in the range {start_port}-{end_port}...")
        for port in range(start_port, end_port + 1):
            if Dns.is_host_alive(domain, port):
                print(f"[+] Port {port} is open on {domain}")
            
    else:
        print("[ERROR] Invalid port input. Please provide a single port or a range of ports (start, end).")



