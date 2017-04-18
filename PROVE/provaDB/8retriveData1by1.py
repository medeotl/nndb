#! /usr/bin/python2
# -*- coding: utf-8 -*-
#
# uso di cur.fetchone()

import sqlite3 as lite

con = lite.connect("test.db")

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Cars")

    while True:
        
        row = cur.fetchone()

        if row == None:
            break
        
        print row[0], row[1], row[2]
