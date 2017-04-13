#!/usr/bin/python3
# -*- coding: utf-8 -*-
# otteniamo la versione di sqlite3 usando with

import sqlite3
from pathlib import Path # per verificare se esiste file db

db_name = "test.db"
my_db = Path("./" + db_name)

if my_db.is_file():
    with sqlite3.connect('test.db') as conn:

        c = conn.cursor()
        c.execute('SELECT SQLITE_VERSION()')

        data = c.fetchone()

        print( "SQLite version: " + str(data[0]) )
else:
    print( "File {} non esistente".format(db_name) )
        

# Nota: l'uso di with ci permette di delegare a python il rilascio della 
#       risorsa ( conn.close() ) e la gestione degli errori.
#       Inoltre le *modifiche* al db sono salvate ( conn.commit() ) 
#       automaticamente (vedi esempio successivo).
#
# Nota: La normale *interrogazione* del db non richede con.commit()
#
# riferimento: http://effbot.org/zone/python-with-statement.htm
