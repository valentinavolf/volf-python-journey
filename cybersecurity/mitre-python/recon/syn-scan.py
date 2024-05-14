from scapy.all import * 
import ipaddress 

host = "8.8.8.8"
ports = [ 25,80,53,443,445,8080,8443]

def synscan(host): 
    ans,unans = sr(IP(dst=host)/TCP(sport=3333,dport=ports, flags="S") ,timeout=2, verbose=1)
    print("Open ports at %s:"%host) 
    for (s,r) in ans:
        if s[TCP].dport == r[TCP].sport and r[TCP].flags=="SA": 
            print(s[TCP].dport)

def DNSScan(host):
    ans, unans = sr( IP(dst=host) / UDP(dport=53)/ DNS(rd=1, qd=DNSQR(qname="google.com")) ,timeout=2, verbose=1)
    if ans and ans[UDP]:
        print("DNS Server at %s"%host)

try: 
    ipaddress.ip_address(host) 
except: 
    print("Invalid address") 
    exit(-1) 
synscan(host) 
DNSScan(host)


