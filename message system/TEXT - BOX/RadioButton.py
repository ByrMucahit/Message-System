# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:59:14 2019

@author: mücahit
"""

from tkinter import *
from tkinter import messagebox
#1-PENCERE OLUŞTURMA
pencere = Tk()

# 2-TİTLE OF WİNDOW
pencere.title("İNPUT THE MESSAGE")

#3-ekranı sınırlandırma
pencere.resizable(FALSE,TRUE)

#4-PENCERE KONUM
pencere.geometry("1200x800+350+50")


# MESSAGE BOX AND DİALOG
#bilgi = messagebox.showinfo("Bilgi" , "Bilgi Ekranı") # ilk bosluk baslık icin , 2.si kutudaki yazı icin
#uyarı=messagebox.showwarning("uyarı", "UYARI EKRANI")
#hata=messagebox.showerror("hata" , "HATA EKRANI")

#Evet_Hayir=messagebox.askquestion("soru ekranı" ,"tamam \devam")

#messagebox.askokcancel("İPTAL" , "İPTAL EDİLSİN Mİ?")
#messagebox.askyesno("yes","yes or NO")
mainloop()    