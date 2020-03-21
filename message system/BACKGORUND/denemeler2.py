# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:25:56 2019

@author: mücahit
"""
import socket
bind_ip='192.168.2.129'
bind_port=65432

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((bind_ip,bind_port))
    s.listen()
    conn,addr=s.accept()
    
    with conn:
        print('Connected by' , addr)
        while True:
            data=conn.recv(1024)
            if not data:
                break
            conn.sendall(data)