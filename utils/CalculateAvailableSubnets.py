# Input: 
#   1) Address space, comma separated if multiple
#   2) Subnets, comma separated if multiple
# Output: 
#   Available subnets
#
# Return:
# Available subnets in (address spaces given MINUS subnets given)
#
# Example: python3 CalculateAvailableSubnets.py "10.223.0.0/16" "10.223.2.0/24,10.223.4.0/24"
#

import sys
import ipaddress

if len(sys.argv) != 3:
    print("Error! Incorrect parameters")
    exit(1)

VNETAddressSpaces = sys.argv[1].split(",")
VNETSubnets = sys.argv[2].split(",")

result = []

for VNETAddressSpace in VNETAddressSpaces:
    VNETAddressSpaceIPs = list(ipaddress.ip_network(VNETAddressSpace)) # All IPs possible in VNETAddressSpaces

    # Remove All subnets possible IPs from VNETAddressSpaceIPs
    for subnet in VNETSubnets:
        if not ipaddress.ip_network(subnet).subnet_of(ipaddress.ip_network(VNETAddressSpace)):
            continue
        ipSubnet = ipaddress.ip_network(subnet)
        for ip in ipSubnet:
            if ipaddress.IPv4Address(ip) in VNETAddressSpaceIPs:
                VNETAddressSpaceIPs.remove(ipaddress.IPv4Address(ip))

    # Factorize
    for subnetAvailable in list(ipaddress.collapse_addresses(VNETAddressSpaceIPs)):
        result.append(str(subnetAvailable))

print(result)