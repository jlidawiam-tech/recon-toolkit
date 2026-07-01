#!/usr/bin/env python3
"""
recon-toolkit v0.1
Built by: github.com/jlidawiam
"""

import argparse
import sys
from modules.host_discovery import discover_hosts


def main():
    parser = argparse.ArgumentParser(
        description='recon-toolkit — Automated Network Reconnaissance'
    )
    parser.add_argument(
        '--target', '-t',
        required=True,
        help='Target IP range (CIDR notation, e.g., 192.168.1.0/24)'
    )
    parser.add_argument(
        '--output', '-o',
        default='report.html',
        help='Output file for report (default: report.html)'
    )
    
    args = parser.parse_args()
    
    print("=" * 50)
    print("  recon-toolkit v0.1")
    print("  github.com/jlidawiam/recon-toolkit")
    print("=" * 50)
    print()
    
    live_hosts = discover_hosts(args.target)
    
    if not live_hosts:
        print("[-] No live hosts found. Exiting.")
        sys.exit(1)
    
    print(f"\n[+] Discovered {len(live_hosts)} live hosts")
    print(f"[+] Report will be saved to: {args.output}")
    print("\n[*] Next: Port scanning, service detection...")
    print("[*] Full framework coming in v0.2")


if __name__ == '__main__':
    main()
