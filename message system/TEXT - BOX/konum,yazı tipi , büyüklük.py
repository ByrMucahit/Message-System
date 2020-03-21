from tkinter import *
pencere=Tk()

def degistir():
    etiket["text"]="Merhaba Dünya"
    
etiket=Label(text='Hello World',
            bg="yellow")
etiket.pack()
buton=Button(text="Cevir",
              command=degistir)
buton.pack()