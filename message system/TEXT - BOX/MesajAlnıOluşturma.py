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
etiket.pack(anchor="w",padx=20)
veri=Entry(bg="white" , fg="green")
veri.pack(ipadx=500 , ipady = 50, )
etiket.config(font=("Comic Sans MS",15,"bold"))

buton3=Button(text="EKLE",command=lambda : ListeKutusu.insert(END,veri.get()))
buton3.pack()
    
ListeKutusu=Listbox()
ListeKutusu.pack(ipadx=50 , ipady = 20,anchor="w",padx=35 )
ListeKutusu.insert(0,"MESSAGE GİVEN LİKE THAT :")
buton=Button(text="SİL" , command=lambda : ListeKutusu.delete(ListeKutusu.get(ACTIVE)))
buton.pack(anchor="w",padx=125)
oku=ListeKutusu.get(END)
print(oku)


mainloop()