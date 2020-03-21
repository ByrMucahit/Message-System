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
#FORM ELEMANLARI -Radio-Button Olusturma

x = StringVar()
x.set("PHYTON")

def dil():
    etiket["text"]=x.get()
    etiket["fg"]="claret red"
    
yazi=Label(text="HANGİ DİLLERİ BİLİYORSUN ? ")
yazi.pack()    

PHYTON=Radiobutton(text="PHYTON" , indicatoron = 1 , value="PYHTON" ,variable = x, command=dil)
PHYTON.pack()

PHP=Radiobutton(text="PHP",indicatoron=1 , value="PHP",variable = x ,command=dil)
PHP.pack()

JAVA=Radiobutton(text="JAVA" , indicatoron=1, value="java",variable = x , command=dil)
JAVA.pack()

etiket=Label()
etiket.pack()
mainloop()    