#! /usr/bin/python3
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

class ButtonWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self, title="button padding")
        self.set_border_width(10)
        self.set_default_size(400, 400)
        box = Gtk.Box(orientation = "vertical")
        
        btnBox1 = Gtk.ButtonBox()
        btnBox1.set_layout(Gtk.ButtonBoxStyle.START)
        btnBox2 = Gtk.ButtonBox()
        btnBox2.set_layout(Gtk.ButtonBoxStyle.START)
        btn11 = Gtk.Button("Claudio Castellini")
        btn12 = Gtk.Button("Michele Medda")
        btn21 = Gtk.Button("Claudio Castellini", name='btnAutori')
        btn22 = Gtk.Button("Michele Medda", name='btnAutori')
        
        btnBox1.add(btn11)
        btnBox1.add(btn12)
        btnBox2.add(btn21)
        btnBox2.add(btn22)
        
        box.pack_start(btnBox1, False, True, 0)
        box.pack_start(btnBox2, False, True, 0)
        
        self.add(box)
        
cssProvider = Gtk.CssProvider()
cssProvider.load_from_path('style.css')
screen = Gdk.Screen.get_default()
styleContext = Gtk.StyleContext()
styleContext.add_provider_for_screen(screen, cssProvider,
                                     Gtk.STYLE_PROVIDER_PRIORITY_USER)

w = ButtonWindow()
w.connect("delete-event", Gtk.main_quit)
w.show_all()

Gtk.main()

#FIXME: il secondo pulsante ha più padding :-/
