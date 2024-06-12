from random import getrandbits
from socket import inet_ntop, AF_INET6
from struct import pack

def random_ipv6():
    return inet_ntop(AF_INET6, pack('>QQ', getrandbits(64), getrandbits(64)))

# Generate and count the IPv6 addresses
ipv6_addresses = [random_ipv6() for _ in range(400)]

for ipv6 in ipv6_addresses:
    print(ipv6)

# If you need to count the unique addresses
unique_ipv6_addresses = set(ipv6_addresses)
print(f"Unique IPv6 addresses count: {len(unique_ipv6_addresses)}")
