import whois # This imports the module

class WhoisInfo:
    def print_whois_info(self, host):
        try:
            whois_data = whois.whois(host)  # Correctly calling the whois function from the whois module
            print(whois_data)
        except Exception as e:
            print(f"Failed to retrieve WHOIS data: {e}")

print(dir(whois))  # This will print all attributes and functions available in the 'whois' module


if __name__ == "__main__":
    whois_info_instance = WhoisInfo()
    whois_info_instance.print_whois_info("google.com")
