import whois as ws 
 
class WhoisInfo: 
    def print_whois_info(self, host): 
        whois_info = ws.whois(host)  
        print(whois_info) 
 
if __name__ == "__main__": 
    whois_info = WhoisInfo() 
    whois_info.print_whois_info("handcrafted-nature.ro")