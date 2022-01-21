import ipaddress

network = ipaddress.ip_network("192.168.1.0/28")

print(network)
print(network.netmask)
print(network.hostmask)
                    
for host in network.hosts():
    print(host)

    