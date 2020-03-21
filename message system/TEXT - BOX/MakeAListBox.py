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


#Chech - Button oluşturma


x = IntVar()


def kontrol ( ):
    if x.get() == 0:
        etiket["text"]="SECİLMEDİ"
        etiket["bg"]="red"
    else:
        etiket["text"]="SECİLDİ"
        
buton=Checkbutton(text="onay" , variable= x , command = kontrol )
buton.pack()        

etiket=Label()
etiket.pack()
mainloop()    