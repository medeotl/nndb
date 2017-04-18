#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# memorizzo le righe in dizionari invece che in tuple
# in questo modo per riferirmi ai dati posso usare il nome delle colonne 

import sqlite3

conn = sqlite3.connect('test.db')

with conn:

    conn.row_factory = sqlite3.Row  #le righe saranno dizionari

    c = conn.cursor()
    c.execute("SELECT * FROM Cars")

    rows = c.fetchall()

    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])
