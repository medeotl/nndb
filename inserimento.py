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
        icon_remove = Gtk.Image()
        icon_remove.set_from_icon_name("list-remove", Gtk.IconSize.BUTTON)
        
        btn_remove.set_image( icon_remove )
        btn_remove.connect("clicked", self.remove_entry)

        btnbox.pack_end(entry, True, True, 0)
        btnbox.pack_end(btn_remove, True, True, 0)
        btnbox.child_set_property(btn_remove,"non-homogeneous", True)
        btn_remove.set_halign (Gtk.Align.CENTER)
        btn_remove.valign = Gtk.Align.CENTER

        vbox.pack_end( btnbox, True, True, 0 )

    def remove_entry(self, btn):
        btnbox = btn.get_parent()
        btnbox.destroy()
        window.resize(1, 1)


builder = Gtk.Builder()
builder.add_from_file("./data/ui/data_insertion.ui")
builder.connect_signals( Handler() )

window = builder.get_object("window")
window.show_all()

Gtk.main()

#FIXME non posso associare a soggetto e sceneggiatura la stessa EntryCompletion
