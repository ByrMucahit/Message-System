# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:59:14 2019

@author: mücahit
"""

from tkinter import *
#1-PENCERE OLUŞTURMA
pencere = Tk()

# 2-TİTLE OF WİNDOW
pencere.title("İNPUT THE MESSAGE")

#3-ekranı sınırlandırma
pencere.resizable(FALSE,TRUE)

#4-PENCERE KONUM
pencere.geometry("1200x800+350+50")
# KULLANICIDAN VERİ ALMA

def Verileri_al():
    etiket["text"]=veri.get()
    
    
    
    
    
veri=Entry()#show komutuyla şifrelenebilir
veri.pack()

Buton = Button(text="Verileri al" , command=Verileri_al , bg="red" , fg="black")
Buton.pack()

etiket=Label(text="Veriler buraya Yazılacak"  )
etiket.pack()

veri.insert(0,"Giriliyor...") # Yazıcıya bir talimat 
veri.pack()

veri.delete(0,"end") # talimatı siler
veri.pack()

mainloop()