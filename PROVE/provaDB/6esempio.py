#! /usr/bin/python2
# -*- coding: utf-8 -*-
# * uso di lastrowid
# * creazione in memoria di un database
# * chiave primaria e suo autoincremento

import sqlite3 as lite

con = lite.connect(':memory:') #

with con:

    cur = con.cursor()
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Rebecca')") # no ;
    cur.execute("INSERT INTO Friends(Name) VALUES ('Jim');")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Robert');")

    lid = cur.lastrowid
    print "The last Id of the inserted row is %d" % lid

# Nota: in questo esercizio l'autore ha messo il ";" finale alle query SQL
#       può anche essere omessa (vedi linea 16)