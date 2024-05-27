from shodan import Shodan 
import json

api = Shodan("JAYiUKBxU1XiVP4tYx4fqXIJQEyeD3EO")

class ShodanHostDetails: 
    def print_host_details(self, ip_address):
        ipinfo = api.host(ip_address)
        print(json.dumps(ipinfo, indent=4))

if __name__== "__main__": 
    shodan_info = ShodanHostDetails()
    shodan_info.print_host_details("89.44.105.62")