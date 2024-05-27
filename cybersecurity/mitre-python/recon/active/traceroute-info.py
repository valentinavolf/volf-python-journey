from icmplib import traceroute 

class Traceroute():
    
    def check_traceroute(self, host) -> None: 
        print("Checking hoops for the target:")
        hops = traceroute(host, max_hops = 20)
        print("All hoops:\n', hops, '\n'")
        print("Distance/ TTL \tAddrss \tAverage round-trip time \tPackets Sent")

        last_distance = 0 
        for hop in hops: 
            if last_distance + 1 != hop.distance: 
                print("No response from gateway")

            print(f'{hop.distance:<15} {hop.address: <15} {hop.avg_rtt} ms \t\t\t[hop.packets_sent :<5]')
            last_distance = hop.distance 

if __name__ == "__main__":
    traceroute_check = Traceroute()
    traceroute_check.check_traceroute("8.8.8.8")
