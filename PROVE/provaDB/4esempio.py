#! usr/bin/python3
# -*- coding: utf-8 -*-
#
# popoliamo la tabella usando c.executemany()

import sqlite3

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)

conn = sqlite3.connect('test.db')
with conn:

    c = conn.cursor()

    # Eliminiamo la tabella Cars se presente
    c.execute("DROP TABLE IF EXISTS Cars")

    c.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    c.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
