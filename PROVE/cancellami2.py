#!/usr/bin/python3
# -*- coding: utf-8 -*-

class MiaClasse():
    a = "nico"
    def __init__(self):
        self.b = "dico"
        c = "fico"
        
    def pipp(self):
        print(self.c)

x = MiaClasse()
y = MiaClasse()

print (id (x.a))
print (id (y.a))

print (id (x.b))
print (id (y.b))

x.pipp()
y.pipp()

x.a = "ciao"
print ( id(x.a) )
