#!/usr/bin/env python3
"""
Host Discovery Module — recon-toolkit
Built by: github.com/jlidawiam
"""

import nmap


def discover_hosts(target_range):
    """
    Discover live hosts in the given IP range.
    
    Args:
        target_range: CIDR notation (e.g., '192.168.1.0/24')
    
    Returns:
        list: Live host IP addresses
    """
    nm = nmap.PortScanner()
    print(f"[+] Scanning {target_range} for live hosts...")
    
    # -sn: Ping scan (no port scan)
    nm.scan(hosts=target_range, arguments='-sn')
    
    live_hosts = []
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            live_hosts.append(host)
            print(f"    [UP] {host}")
    
    print(f"[+] Found {len(live_hosts)} live hosts")
    return live_hosts


if __name__ == '__main__':
    hosts = discover_hosts('192.168.1.0/24')
    print(f"Live hosts: {hosts}")
