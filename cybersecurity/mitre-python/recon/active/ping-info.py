from pythonping import ping 
class PingConnectivity: 
    def check_ping_connectivity(self, host) -> None:
        ping(host, verbose = True)

if __name__ == "__main__":
    ping_check_connectivity = PingConnectivity()
    ping_check_connectivity.check_ping_connectivity("192.168.56.10")