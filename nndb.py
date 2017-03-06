#! /usr/bin/python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from database import db

class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_border_width(10)

        self.grid = Gtk.Grid()
        self.add(self.grid)
        
        self.cover = Gtk.Image()
        self.cover_path = "./data/cover/nat"
        self.showed_issue = 1
        self.last_issue = 10
        self.set_title("1 - " + db[1][0])
        self.cover.set_from_file(self.cover_path + "001.jpg")
        self.grid.attach(self.cover,0,0,4,8)
        
        # pulsanti per scorrere le cover
        
        self.btn_first = Gtk.Button("first", sensitive=False)
        self.btn_previous = Gtk.Button("previous", sensitive=False)
        self.btn_next = Gtk.Button("next")
        self.btn_last = Gtk.Button("last")
        
        self.grid.attach_next_to(self.btn_first, self.cover, 
                            Gtk.PositionType.BOTTOM, 1, 1 )
        self.grid.attach_next_to(self.btn_previous, self.btn_first, 
                            Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.btn_next, self.btn_previous, 
                            Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.btn_last, self.btn_next, 
                            Gtk.PositionType.RIGHT, 1, 1)
    
        self.btn_first.connect("clicked", self.show_first_issue)
        self.btn_previous.connect("clicked", self.show_previous_issue)
        self.btn_next.connect("clicked", self.show_next_issue)
        self.btn_last.connect("clicked", self.show_last_issue)

        lbl_soggetto = Gtk.Label()
        lbl_soggetto.set_markup("<b>Soggetto</b>")
        self.bbox_soggetto = Gtk.ButtonBox(Gtk.Orientation.HORIZONTAL)
        lbl_sceneggiatura = Gtk.Label("<b>Sceneggiatura</b>")
        self.bbox_sceneggiatura = Gtk.ButtonBox(Gtk.Orientation.HORIZONTAL)
        lbl_disegni = Gtk.Label("<b>Disegni</b>")
        self.bbox_disegni = Gtk.ButtonBox(Gtk.Orientation.HORIZONTAL)
        lbl_copertina = Gtk.Label("<b>Copertina</b>")
        self.bbox_copertina = Gtk.ButtonBox(Gtk.Orientation.HORIZONTAL)
        
        self.grid.attach_next_to(lbl_soggetto, self.cover, 
                            Gtk.PositionType.RIGHT, 1, 1)
        self.grid.attach_next_to(self.bbox_soggetto, lbl_soggetto,
                            Gtk.PositionType.BOTTOM, 1, 1)
                            
        self.grid.attach_next_to(lbl_sceneggiatura, self.bbox_soggetto, 
                            Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.bbox_sceneggiatura, lbl_sceneggiatura,
                            Gtk.PositionType.BOTTOM, 1, 1)
                            
        self.grid.attach_next_to(lbl_disegni, self.bbox_sceneggiatura, 
                            Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.bbox_disegni, lbl_disegni,
                            Gtk.PositionType.BOTTOM, 1, 1)
                            
        self.grid.attach_next_to(lbl_copertina, self.bbox_disegni, 
                            Gtk.PositionType.BOTTOM, 1, 1)
        self.grid.attach_next_to(self.bbox_copertina, lbl_copertina,
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
        str_albo = '{:03}'.format(albo)
        self.cover.set_from_file(self.cover_path + str_albo + ".jpg")
        self.set_title( str(albo) + " - " + db[albo][0] )
        
        # popolo la finestra con i dati degli autori
        for pulsante in self.bbox_soggetto.get_children():
            pulsante.destroy()
        for soggettista in db [albo] [ 1].split (", "):
            self.bbox_soggetto.add( 
                Gtk.Button( str(soggettista),
                            relief=Gtk.ReliefStyle.NONE ) 
            )
        self.bbox_soggetto.show_all()
        
        for pulsante in self.bbox_sceneggiatura.get_children():
            pulsante.destroy()
        for sceneggiatore in db [albo] [2].split (", "):
            self.bbox_sceneggiatura.add( 
                Gtk.Button( str(sceneggiatore),
                            relief=Gtk.ReliefStyle.NONE) 
            )
        self.bbox_sceneggiatura.show_all()
        
        for pulsante in self.bbox_disegni.get_children():
            pulsante.destroy()
        for disegnatore in db [albo] [3].split (", "):
            self.bbox_disegni.add( 
                Gtk.Button( str(disegnatore),
                            relief=Gtk.ReliefStyle.NONE ) 
            )
                        
        self.bbox_disegni.show_all()
        
        for pulsante in self.bbox_copertina.get_children():
            pulsante.destroy()
        for copertinista in db [albo] [4].split (", "):
            self.bbox_copertina.add( 
                Gtk.Button( str(copertinista),
                            relief=Gtk.ReliefStyle.NONE ) 
            )
        self.bbox_copertina.show_all()
        
        self.set_showed_issue(albo)
        self.set_navigation_buttons(albo)
        

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()
