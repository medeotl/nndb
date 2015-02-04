#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Testing Application")
        self.set_border_width(10)
        self.set_default_size(400, 400)
        
        self.grid = Gtk.Grid()
        self.add(self.grid)
        
        self.bbox = Gtk.ButtonBox( Gtk.Orientation.HORIZONTAL )
        print ( id(self.bbox) )
        self.btn_popola = Gtk.Button("Popola pulsanti")
        self.btn_popola.connect("clicked", self.popola)
        self.grid.attach( self.btn_popola, 0, 0, 1, 1 )
        self.grid.attach_next_to(self.bbox, self.btn_popola, 
                                 Gtk.PositionType.BOTTOM, 1, 1)
        
        
        self.btn_nico = Gtk.Button("Nico")
        self.btn_dico = Gtk.Button("Dico")
        self.btn_fico = Gtk.Button("Fico")
        
        #~ self.bbox.add( btn_nico )
        #~ self.bbox.add( btn_dico )
        #~ self.bbox.add( btn_fico )

    def popola(self, button):
        print ( id(self.bbox) )
        lista = ("Nico", "Dico", "Fico")
        
        for nome in lista:
            self.bbox.add( Gtk.Button(nome) )
        print ( id(self.bbox) )
        self.bbox.show_all()
        
        
win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
