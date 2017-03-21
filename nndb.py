#! /usr/bin/python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from database import db

class Handler:
    
    showed_issue = 1
    last_issue = 10
    
    def onDeleteMainWindow(self, *args):
        Gtk.main_quit(*args)

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
        maschera = d.get(issue, (True, True, True, True) )
            
        builder.get_object('btn_first').set_sensitive(maschera[0])
        builder.get_object('btn_previous').set_sensitive(maschera[1])
        builder.get_object('btn_next').set_sensitive(maschera[2])
        builder.get_object('btn_last').set_sensitive(maschera[3])

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
        cover = builder.get_object( "cover" )
        cover.set_from_file(COVER_PATH + str_albo + ".jpg")
        window.set_title( str(albo) + " - " + db[albo][0] )
        
        # popolo la finestra con i dati degli autori
        competenze = ('soggetto', 'sceneggiatura', 'disegni', 'copertina')
        linea_autori = 1
        for competenza in competenze:
            bbox = builder.get_object( "bbox_"+competenza )
            for pulsante in bbox.get_children():
                pulsante.destroy()
            for autore in db[albo][linea_autori].split(", "):
                bbox.add(Gtk.Button(str(autore), relief=Gtk.ReliefStyle.NONE))
            bbox.show_all()
            linea_autori += 1
            
        self.set_showed_issue(albo)
        self.set_navigation_buttons(albo)
        window.resize(1, 1) # rimuovo spazio in eccesso
        

GUI = './data/ui/main.ui'
COVER_PATH = './data/cover/nat'

builder = Gtk.Builder()
builder.add_from_file( GUI )
builder.connect_signals( Handler() )

window = builder.get_object( "window1" )
window.set_title("1 - " + db[1][0])
window.show_all()

Gtk.main()
