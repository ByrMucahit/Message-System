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
pencere.geometry("600x600+350+50")
#FORM (pack and place) elemanları

buton=Button(text="buton")
buton.pack(anchor="nw" , padx=15 , pady=20)

buton2=Button(text="buton_2")
buton2.place(relwidth = 0.10 , relheight= 0.10)




mainloop()    