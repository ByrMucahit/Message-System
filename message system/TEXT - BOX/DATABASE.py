# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:09:06 2019

@author: mücahit
"""


import sqlite3  

con = sqlite3.connect("Mesahlar.db")
cursor=con.cursor()

def tabloolustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS ogrenciler(Name TEXT , Surname TEXT , NUMBER INT , Grade INT  )")
    con.commit()
    con.close()
tabloolustur()    