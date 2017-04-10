#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sqlite3 as lite
from pathlib import Path # per verificare se esiste file db

db_name = "test.db"
my_db = Path("./" + db_name)

if my_db.is_file():
    # il file esiste
    conn = lite.connect(db_name) 

    c = conn.cursor()
    c.execute('SELECT SQLITE_VERSION()')

    data = c.fetchone()

    print( "SQLite version: {}".format(data) )

    conn.close()
    
else:
    print( "File {} non esistente".format(db_name) )
