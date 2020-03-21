# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:59:14 2019

@author: mücahit
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""DATA-BASE"""

from tkinter import *

import sqlite3
import socket
import sys


con=sqlite3.connect("mesajlar.db")

im=con.cursor()

def TabloOlustur():
    im.execute("CREATE TABLE IF NOT EXISTS mesajlar(Mesajlar TEXT)")
    con.commit()

TabloOlustur()

#1-PENCERE OLUŞTURMA
pencere = Tk()

# 2-TİTLE OF WİNDOW
pencere.title("İNPUT THE MESSAGE")

#3-ekranı sınırlandırma
pencere.resizable(FALSE,TRUE)

#4-PENCERE KONUM
pencere.geometry("1200x800+350+50")

# KULLANICIDAN VERİ ALMA
etiket=Label(text="PLEASE , YOU WRİTE THE MESSAGE İN THİS SPACE TO SEND")
etiket.pack(anchor="w",padx=20)

veri=Entry(bg="white" , fg="green" ) #Veri Girmek 
veri.pack(ipadx=520 , ipady = 50 )  #Veriyi şekillendirmek
etiket.config(font=("Comic Sans MS",15,"bold"))


ListeKutusu=Listbox()
ListeKutusu.pack(ipadx=50 , ipady = 20,anchor="w",padx=35 )
ListeKutusu.insert(0,"MESSAGE GİVEN LİKE BELOW:")

def verikaydet():
    ListeKutusu.insert(END,veri.get())
    info=veri.get()
    im.execute("INSERT INTO Mesajlar(Mesajlar) VALUES('"+info+"')")
    con.commit() 

verikaydet()

buton3=Button(text="EKLE",command= verikaydet)
buton3.pack()

mainloop()  

"""Verileri Çekiyoruz"""

im.execute("SELECT * FROM Mesajlar")

veriler=im.fetchall()

boyut=len(veriler)
print(boyut)
    
blog_1=[]
blog_2=[]
blog_3=[]
i=0
while 1:
    if  i < boyut/5:
        blog_1  +=veriler[i]
        i=i+1
    elif boyut/5 <= i < boyut/3:
        blog_2 +=veriler[i]
        i=i+1
        
    elif boyut/3 <= i < boyut:
        blog_3 +=veriler[i]
        i=i+1
       
    else:
        break


print(blog_1)
print(blog_2)
print(blog_3)


mesajlar=[]
mesajlar= blog_1 + blog_2 + blog_3
print('\n\n\n',mesajlar)
#SERVER

#CLİENT
"""TCP ile veri gönderme"""
Client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#GÖNDEREN VE ALAN

TCP_IP='192.168.2.129'
TCP_PORT=1024
adress=(TCP_IP , TCP_PORT)
#client.connect((target,port))
Client.connect(adress)
Client.send(mesajlar)
addr=Client.recv(1024)
print(addr)



client.close()









