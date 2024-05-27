from pycrtsh import Crtsh 
import json 

class CrtshCrtInfo: 
    def cert_query(self, host):
        crtsh = Crtsh()
        certs = crtsh.search(host)
        print(json.dumps(certs, indent = 4, default=str))

if __name__ == "__main__": 
    cert_info = CrtshCrtInfo()
    cert_info.cert_query("handcrafted-nature.ro")