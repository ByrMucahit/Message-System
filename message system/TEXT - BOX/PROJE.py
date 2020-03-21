# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:13:53 2019

@author: mücahit
"""

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



    
etiket=Label(text="PLEASE , YOU WRİTE THE MESSAGE İN THİS SPACE TO SEND")
etiket.config(font=("Comic Sans MS",15,"bold"))
etiket.pack(anchor="w",padx=20)


veri=Entry(bg="white" , fg="green")
veri.config(font=("Comic Sans MS",10,"bold"))
veri.pack(ipadx=500 , ipady = 50 )

Buton=Button(text="SEND",command=lambda : ListeKutusu.insert(END,veri.get(ACTIVE)))
Buton.pack(anchor="w",padx=18,ipadx=15,ipady=10)

ListeKutusu=Listbox()
ListeKutusu.pack()

mainloop()