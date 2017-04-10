#!/usr/bin/python2
# -*- coding: utf-8 -*-
# otteniamo la versione di sqlite3 usando with

import sqlite3 as lite
#~ import sys # non serve più 

conn = lite.connect('test.db')

with conn:

    c = conn.cursor()
    c.execute('SELECT SQLITE_VERSION()')

    data = c.fetchone()

    print "SQLite version: %s" % data

# Nota1: lite.connect() se non trova il db lo crea (non genera errore, lo 
#        fa in altri casi, tipo se il disco è pieno)
#
# Nota2: l'uso di with ci permette di delegare a python il rilascio della 
#        risorsa ( conn.close() ) e la gestione degli errori.
#        riferimento: http://effbot.org/zone/python-with-statement.htm
