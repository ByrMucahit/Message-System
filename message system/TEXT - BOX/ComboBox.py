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

def yazdir():
    print(spin.get())

spin=Spinbox(pencere , from_=1 , to=10)
spin.pack()

buton=Button(pencere , text="BASTİR" , command=yazdir )
buton.pack()


mainloop()    