#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# primo esempio di prelevamento dati dal db
# uso di c.fetchall() che ritorna una tupla di tuple

import sqlite3

conn = sqlite3.connect('test.db')

with conn:

    c = conn.cursor()
    c.execute("SELECT * FROM Cars")

    rows = c.fetchall()

    for row in rows:
        print row
