import pydig as pd 

class DigInfo: 
    def print_dig_info(self, host, type):
        dig_info = pd.query(host, type)
        print(dig_info)

if __name__ == "__main__": 
    dig_info = DigInfo()
    dig_info.print_dig_info("handcrafted-nature.ro" , "A")
    dig_info.print_dig_info("handcrafted-nature.ro" , "NS")