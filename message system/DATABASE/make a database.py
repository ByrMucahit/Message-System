# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 09:58:44 2019

@author: mücahit
"""

import sqlite3

con=sqlite3.connect("dersler.lb")
cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT , soyad TEXT , numara INT , ogrencınotu INT )")
    con.commit()

def ekle():
    cursor.execute("INSERT INTO ogrenciler VALUES ('Muhammed Mucahit' ,'BAYAR',181213068,80)")
    con.commit()
    con.close()
    
tabloolustur()
ekle()
    