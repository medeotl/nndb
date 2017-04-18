#! /usr/bin/python3
# -*- coding: utf-8 -*-
#
# uso di c.fetchone()

import sqlite3

conn = sqlite3.connect("test.db")

with conn:

    c = conn.cursor()
    c.execute("SELECT * FROM Cars")

    while True:
        
        row = c.fetchone()

        if row == None:
            break
        
        print row[0], row[1], row[2]
