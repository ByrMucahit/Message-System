# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:59:14 2019

@author: mücahit
"""

from tkinter import *
from tkinter.ttk import Combobox
#1-PENCERE OLUŞTURMA
pencere = Tk()

# 2-TİTLE OF WİNDOW
pencere.title("İNPUT THE MESSAGE")

#3-ekranı sınırlandırma
pencere.resizable(FALSE,TRUE)

#4-PENCERE KONUM
pencere.geometry("1200x800+350+50")


#COMBOBOX
def bastir():
    deger=BOX.get()
    print(deger)
    
    
lis=["Pazartesi" , "Salı" , "Çarşamba","Perşembe","Cuma"]
gun=list(range(1,32))

BOX=Combobox(pencere,values=gun , height=5)
BOX.pack()

buton=Button(pencere,text="Yazdır",command=bastir)
buton.pack()


mainloop()    