#! /usr/bin/python2
# -*- coding: utf-8 -*-

from gi.repository import Gtk, Gdk #, GObject

class EntryWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Entry Autocomplete Demo", 
                            border_width=10)
        self.set_size_request(200, 100)

        VERTICAL = Gtk.Orientation.VERTICAL
        vbox = Gtk.Box(orientation=VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        self.textbuffer = self.entry.get_buffer()
        self.entry.connect("key-press-event", self.print_key_pressed)
        
        vbox.pack_start(self.entry, True, True, 0)

    def print_key_pressed(self, widget, eventKey):
        # print type(widget)
        # print eventKey.string
        self.entry.modify_fg(Gtk.StateType.NORMAL, Gdk.Color(32000,32000,32000))

        if eventKey.string == "a":
            widget.set_text("ntonio Serra")
    
win = EntryWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
