#! /usr/bin/python2
# -*- coding: utf-8 -*-
# primo esempio di prelevamento dati dal db
# uso di cur.fetchall() che ritorna una tupla di tuple

import sqlite3 as lite

con = lite.connect('test.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print row
