# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:59:14 2019

@author: mücahit
"""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""DATA-BASE"""

from tkinter import *
import time
import sqlite3
import socket

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

x=veri.get()


buton3=Button(text="EKLE",command= verikaydet)
buton3.pack()

ListeKutusu=Listbox()
ListeKutusu.pack(ipadx=50 , ipady = 20,anchor="w",padx=35 )

ListeKutusu.insert(0,"MESSAGE GİVEN LİKE BELOW:")


  
def verikaydet():
    ListeKutusu.insert(END,veri.get())
    info=veri.get()
    im.execute("INSERT INTO Mesajlar(Mesajlar) VALUES('"+info+"')")
    con.commit() 
      
"""Verileri Çekiyoruz"""

im.execute("SELECT * FROM Mesajlar")
veriler=im.fetchall()
print(veriler)

"""TCP ile veri gönderme"""
Client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#◘GÖNDEREN VE ALAN"""
TCP_IP="www.google.com.tr"
TCP_PORT=80
adress=(TCP_IP , TCP_PORT)
#client.connect((target,port))
Client.connect(adress)
Client.send(veriler)




verikaydet()
mainloop()
im.close()
con.close()
Client.close()# -*- coding: utf-8 -*-




