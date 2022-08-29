#!/bin/python3
# A Simple function that finds NS records, resolves their IP, and attempts a DNS Zone Transfer
import dns.zone
import dns.resolver

ns_servers = []
def dns_zone_xfer(address):
    ns_answer = dns.resolver.resolve(address, 'NS')
    for server in ns_answer:
        print(f"[*] Found NS: {server}")
        ip_answer = dns.resolver.resolve(server.target, 'A')
        for ip in ip_answer:
            print(f"[*] IP for {server} is {ip}")
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(str(ip), address))
                for host in zone:
                    print(f"[*] Found Host: {host}.{address}")
            except Exception as e:
                print(f"[*] NS {server} refused zone transfer!")
                continue

domain = input('Enter the top level domain you would like to check for DNS Zone Transfer:>\n')
dns_zone_xfer(domain)