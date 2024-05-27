import dns 
import dns.resolver
import socket

subs = "dns-scan.dns"  
dictionary = []  

with open(subs, "r") as f:
    dictionary = f.read().splitlines()

res = dns.resolver.Resolver()
res.nameservers = ["8.8.8.8"]
res.port = 53

domains = {}

def reverse_dns(ip):
    try:
        result = socket.gethostbyaddr(ip)
        return [result[0]] + result[1]
    except socket.herror:
        return [] 

def dns_request(domain):
    ips = []
    try:
        answers = res.resolve(domain)
        for rdata in answers:
            ips.append(rdata.address)
            if rdata.address not in domains:
                domains[rdata.address] = []
            domains[rdata.address].append(domain)
            # Reverse DNS for each IP found
            reverse_domains = reverse_dns(rdata.address)
            for rd in reverse_domains:
                if rd not in domains:
                    domains[rd] = [rdata.address]
                elif rdata.address not in domains[rd]:
                    domains[rd].append(rdata.address)
    except (dns.resolver.NXDOMAIN, dns.resolver.Timeout, dns.exception.DNSException) as e:
        # Handle specific DNS exceptions
        print(f"DNS query failed for {domain}: {e}")
    return ips

def host_search(domain, dictionary, nums):
    for word in dictionary:
        subdomain = word + "." + domain
        dns_request(subdomain)
        if nums:
            for i in range(10):  # 0 to 9
                num_subdomain = f"{word}{i}.{domain}"
                dns_request(num_subdomain)


domain = "google.com"
host_search(domain, dictionary, True)

for domain, ips in domains.items():
    print(f"{domain}: {ips}")
