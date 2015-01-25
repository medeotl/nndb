#!/usr/bin/python2
# -*- coding: utf-8 -*-
# prima interazione con sqlite3: otteniamo la versione di sqlite3


import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('test.db') 

    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print "SQLite version: %s" % data

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con: # se il valore di con è *ritenuto* vero
        con.close() 

# Nota finale: "if variabile" è equivalente a "if variabile is True"
# a seconda del tipo di variabile, il suo valore può essere o meno equivalente
# a False
# nel nostro caso, None è equivalente a False
# anche 0 (numero), e le sequenze vuote ([],'', etc) sono equivalenti a False
# riferimenti:  http://docs.python.org/library/stdtypes.html