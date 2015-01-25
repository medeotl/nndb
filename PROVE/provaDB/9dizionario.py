#! /usr/bin/python2
# -*- coding: utf-8 -*-
# memorizzo le righe in dizionari invece che in tuple
# in questo modo per riferirmi ai dati posso usare il nome delle colonne 

import sqlite3 as lite

con = lite.connect('test.db')

with con:

    con.row_factory = lite.Row  #le righe saranno dizionari

    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])

