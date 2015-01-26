#! /usr/bin/python3
# -*- coding: utf-8 -*-
from gi.repository import Gtk
from database import db

class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(10)

        grid = Gtk.Grid()
        self.add(grid)
        
        self.cover = Gtk.Image()
        self.cover_path = "./data/cover/nat"
        self.showed_issue = 1
        self.last_issue = 10 
        self.set_title(db[1][0])
        self.cover.set_from_file(self.cover_path + "001.jpg")
        grid.attach(self.cover,0,0,4,8)
        
        # pulsanti per scorrere le cover
        
        self.btn_first = Gtk.Button("first")
        self.btn_first.set_sensitive(False) # disabilito il pulsante
        self.btn_previous = Gtk.Button("previous")
        self.btn_previous.set_sensitive(False)
        self.btn_next = Gtk.Button("next")
        self.btn_last = Gtk.Button("last")
        
        grid.attach_next_to(self.btn_first, self.cover, 
                            Gtk.PositionType.BOTTOM, 1, 1 )
        grid.attach_next_to(self.btn_previous, self.btn_first, 
                            Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.btn_next, self.btn_previous, 
                            Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.btn_last, self.btn_next, 
                            Gtk.PositionType.RIGHT, 1, 1)                            
    
        self.btn_first.connect("clicked", self.show_first_issue)
        self.btn_previous.connect("clicked", self.show_previous_issue)                                
        self.btn_next.connect("clicked", self.show_next_issue)
        self.btn_last.connect("clicked", self.show_last_issue)        

        lbl_soggetto = Gtk.Label("Soggetto")
        bbox = Gtk.ButtonBox(Gtk.Orientation.HORIZONTAL)
        lbl_sceneggiatura = Gtk.Label("Sceneggiatura")
        lbl_disegni = Gtk.Label("Disegni")
        lbl_copertina = Gtk.Label("Copertina")
        
        grid.attach_next_to(lbl_soggetto, self.cover, 
                            Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(bbox, lbl_soggetto,
                            Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(lbl_sceneggiatura, lbl_soggetto, 
                            Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(bbox, lbl_sceneggiatura,
                            Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(lbl_disegni, lbl_sceneggiatura, 
                            Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(bbox, lbl_disegni,
                            Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(lbl_copertina, lbl_disegni, 
                            Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(bbox, lbl_copertina,
                            Gtk.PositionType.BOTTOM, 1, 1)

    def get_showed_issue(self):
        return self.showed_issue
        
    def set_showed_issue(self, issue):
        self.showed_issue = issue
        
    def set_navigation_buttons(self, issue):
        """ 
        setta i pulsanti btn_(first|prev|next|last) correttamente
        """
        d = {1               : (False, False, True, True),
             self.last_issue : (True, True, False, False)
            }
        try:
            maschera = d[issue]
        except KeyError:
            maschera = (True, True, True, True)
            
        self.btn_first.set_sensitive(maschera[0])
        self.btn_previous.set_sensitive(maschera[1])
        self.btn_next.set_sensitive(maschera[2])
        self.btn_last.set_sensitive(maschera[3])

    def show_first_issue(self, button):
        """ mostra il primo albo """
        self.show_issue( 1 )
    
    def show_last_issue(self, button):
        """ mostra l'ultimo albo """
        self.show_issue( self.last_issue )
    
    def show_previous_issue(self, button):
        """ mostra il precedente albo """
        self.show_issue( self.get_showed_issue()-1 )
    
    def show_next_issue(self, button):
        """ mostra il successivo albo """
        self.show_issue( self.get_showed_issue()+1 )
        
    def show_issue(self, albo):
        """ mostra l'albo passato come parametro """
        print(albo)
        str_albo = '{:03}'.format(albo)
        self.cover.set_from_file(self.cover_path + str_albo + ".jpg")
        self.set_title( db[albo][0] )
        self.set_showed_issue(albo)
        self.set_navigation_buttons(albo)
        
        
win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()
	
	


