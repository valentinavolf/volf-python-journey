from nslookup import Nslookup 

class NslookupInfo:
    def print_dns_query(self, domain):
        dns_resolver = Nslookup()
        dns_query = dns_resolver.dns_lookup(domain)
        print(dns_query.response_full)

if __name__ == "__main__":
    dns_info = NslookupInfo()
    dns_info.print_dns_query("handcrafted-nature.ro")