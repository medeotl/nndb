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
        self.current_issue = 1
        self.last_issue = 10 
        self.set_title(db[1][0])
        self.cover.set_from_file(self.cover_path + "001.jpg")
        grid.attach(self.cover,0,0,4,8)
        
        # provo a inserire pulsanti primo/precedente/successivo/ultimo
        # per scorrere le cover, in futuro devono essere toolbar
        
        self.btn_first = Gtk.Button("first")
        self.btn_first.set_sensitive(False) # disabilito il pulsante
        self.btn_previous = Gtk.Button("previous")
        self.btn_previous.set_sensitive(False) # come sopra
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

        
    def show_first_issue(self, button):
        """ mostra il primo albo """
        if self.current_issue == self.last_issue:
            # riabilito pulsanti next e last
            self.btn_next.set_sensitive(True)
            self.btn_last.set_sensitive(True)
        self.show_issue(1)
        # disabilito pulsanti first e previous
        self.btn_first.set_sensitive(False)
        self.btn_previous.set_sensitive(False)
        
    
    def show_last_issue(self, button):
        """ mostra l'ultimo albo """
        if self.current_issue == 1:
            # riabilito pulsanti first e previous
            self.btn_first.set_sensitive(True)
            self.btn_previous.set_sensitive(True)
        self.show_issue(self.last_issue)
        # disabilito pulsanti next e last
        self.btn_next.set_sensitive(False)
        self.btn_last.set_sensitive(False)      
    
    def show_previous_issue(self, button):
        """ mostra il precedente albo """
        self.show_issue(self.current_issue-1)
        if self.current_issue == 1:
            # disabilito pulsanti first e previous
            self.btn_first.set_sensitive(False)
            self.btn_previous.set_sensitive(False)
        elif self.current_issue == self.last_issue-1:
            # riabilito pulsanti next e last
            self.btn_next.set_sensitive(True)
            self.btn_last.set_sensitive(True)
    
    def show_next_issue(self, button):
        """ mostra il successivo albo """
        self.show_issue(self.current_issue+1)
        if self.current_issue == self.last_issue:
            # disabilito pulsanti next e last
            self.btn_next.set_sensitive(False)
            self.btn_last.set_sensitive(False)
        elif self.current_issue == 2:
            # riabilito pulsanti first e previous
            self.btn_first.set_sensitive(True)
            self.btn_previous.set_sensitive(True)
        
    def show_issue(self, albo):
        """ mostra l'albo passato come parametro """
        str_albo = '{:03}'.format(albo)
        self.cover.set_from_file(self.cover_path + str_albo + ".jpg")
        self.set_title(db[albo][0])
        
        
win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()
	
	

