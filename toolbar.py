#! /usr/bin/python2
# -*- coding: utf-8 -*-
from gi.repository import Gtk

# prova di toolbar

class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="Nathan Never DB viewer")
        self.set_border_width(10)

        grid = Gtk.Grid()
        self.add(grid)
        
        img = Gtk.Image()
        img.set_from_file("./data/cover/nat0001.jpg")
        grid.add(img)
        
        ag_naviga = Gtk.ActionGroup("albi_navigator")
        
        btl_prv = Gtk.Button()
        
        
win = MainWindow()
win.connect("delete-event", Gtk.main_quit) # fuori dall'init???
win.show_all()

Gtk.main()
	
	

