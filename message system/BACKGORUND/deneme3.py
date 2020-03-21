# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:29:45 2019

@author: mücahit
"""

import socket
        
bind_ip='192.168.2.129'
bind_port=65432
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((bind_ip,bind_port))
    s.sendall(b'HELLO, WORLD')
    data=s.recv(1024)
print('received',repr(data))

