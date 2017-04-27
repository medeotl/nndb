#! /usr/bin/python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from database import db

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onAlboChange(self, spinBtn):
        albo = spinBtn.get_value_as_int()
        titolo = builder.get_object("titolo")
        soggetto = builder.get_object("soggetto")
        sceneggiatura = builder.get_object("sceneggiatura")
        disegni = builder.get_object("disegni")
        copertina = builder.get_object("copertina")

        if albo in db:
            titolo.set_text(       db[albo][0])
            soggetto.set_text(     db[albo][1])
            sceneggiatura.set_text(db[albo][2])
            disegni.set_text(      db[albo][3])
            copertina.set_text(    db[albo][4])
        else:
            titolo.set_text("")
            soggetto.set_text("")
            sceneggiatura.set_text("")
            disegni.set_text("")
            copertina.set_text("")

    def insert(self, btn):
        spinBtn = builder.get_object("albo")
        spinBtn.spin(Gtk.SpinType.STEP_FORWARD, 1)

    def add_soggettista(self, btn):
        vbox = btn.get_parent().get_parent()
        btnbox = Gtk.ButtonBox(Gtk.Orientation.HORIZONTAL, visible=True)

        entry = Gtk.Entry(visible=True)
        btn_remove = Gtk.Button(visible=True)
        btn_remove.set_image( Gtk.Image.set_from_icon_name("list-remove") )

        btnbox.pack_end(entry, True, True, 0)
        btnbox.pack_end(btn_remove, True, True, 0)

        vbox.pack_end( btnbox, True, True, 0 )



builder = Gtk.Builder()
builder.add_from_file("./data/ui/data_insertion.ui")
builder.connect_signals( Handler() )

window = builder.get_object("window")
window.show_all()

Gtk.main()

#FIXME non posso associare a soggetto e sceneggiatura la stessa EntryCompletion