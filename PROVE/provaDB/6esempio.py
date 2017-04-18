#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# * uso di lastrowid
# * creazione in memoria di un database
# * chiave primaria e suo autoincremento

import sqlite3

conn = sqlite3.connect(':memory:') #

with conn:

    c = conn.cursor()
    c.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    c.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    c.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')") # no ;
    c.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    c.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

    lid = c.lastrowid
    print "The last Id of the inserted row is %d" % lid

# Nota: in questo esercizio l'autore ha messo il ";" finale alle query SQL
#       può anche essere omessa (vedi linea 16)
