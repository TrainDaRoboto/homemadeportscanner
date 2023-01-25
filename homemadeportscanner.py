# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 12:51:11 2023

@author: npark
"""

import socket

# get the current IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
current_ip = s.getsockname()[0]
print("Current IP:", current_ip)
s.close()

# scan the ports
for port in range(1, 65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    result = sock.connect_ex((current_ip, port))
    if result == 0:
        print("Port " + str(port) + " is open")
    sock.close()