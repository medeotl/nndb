#!/usr/bin/python3
# -*- coding: utf-8 -*-
# creiamo e popoliamo una tabella

import sqlite3 as lite

conn = lite.connect('test.db')

with conn:

    c = conn.cursor()
    c.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    c.execute("INSERT INTO Cars VALUES(1, 'Audi', 52642)")
    c.execute("INSERT INTO Cars VALUES(2, 'Mercedes', 57127)")
    c.execute("INSERT INTO Cars VALUES(3, 'Skoda', 9000)")
    c.execute("INSERT INTO Cars VALUES(4, 'Volvo', 29000)")
    c.execute("INSERT INTO Cars VALUES(5, 'Bentley', 350000)")
    c.execute("INSERT INTO Cars VALUES(6, 'Citroen', 21000)")
    c.execute("INSERT INTO Cars VALUES(7, 'Hummer', 41400)")
    c.execute("INSERT INTO Cars VALUES(8, 'Volkswagen', 21600)")

# Nota: Using the with keyword the changes are automatically committed. 
#       Otherwise, we would have to commit them manually ( conn.commit() )
