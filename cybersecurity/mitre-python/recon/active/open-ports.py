import nmap3
import json 

class NmapPortScanner: 
    def port_scan(self, host) -> None: 
        nmap = nmap3.Nmap()
        scan_results = nmap.scan_top_ports(host)
        print(json.dumps(scan_results, indent=4))

if __name__ == "__main__": 
    nmap_scanner = NmapPortScanner()
    nmap_scanner.port_scan("192.168.56.10")
