#! /usr/bin/python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from database import db
import sqlite3

class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onAlboChange(self, spinBtn):
        albo = spinBtn.get_value_as_int()
        titolo = builder.get_object("titolo")
        soggetto = builder.get_object("soggettisti")
        sceneggiatura = builder.get_object("sceneggiatori")
        disegni = builder.get_object("disegnatori")
        copertina = builder.get_object("copertinista")

        if albo in db:
            titolo.set_text( db[albo][0] )
            soggetto_entry = soggetto.get_children()[0].get_children()[0]
            soggetto_entry.set_text( db[albo][1] )
            sceneggiatura_entry = \
                sceneggiatura.get_children()[0].get_children()[0]
            sceneggiatura_entry.set_text(db[albo][2])
            disegni_entry = disegni.get_children()[0].get_children()[0]
            disegni_entry.set_text(      db[albo][3])
            copertina.set_text(    db[albo][4])
        else:
            titolo.set_text("")
            soggetto.set_text("")
            sceneggiatura.set_text("")
            disegni.set_text("")
            copertina.set_text("")

    def insert(self, btn):
        spinBtn = builder.get_object("albo")
        # prelevo dati albo e li visualizzo nel terminale
        titolo = builder.get_object("titolo")
        print( titolo.get_text() )
        soggetto = builder.get_object("soggettisti")
        for item in soggetto.get_children():
            print( item.get_children()[0].get_text() )
            print( item.get_children()[0].get_completion() )
        spinBtn.spin(Gtk.SpinType.STEP_FORWARD, 1)


    def add_entry(self, btn):
        vbox = btn.get_parent().get_parent()
        btnbox = Gtk.ButtonBox(Gtk.Orientation.HORIZONTAL)

        entry = Gtk.Entry()
        btn_remove = Gtk.Button()
        icon_remove = Gtk.Image()
        icon_remove.set_from_icon_name("list-remove", Gtk.IconSize.BUTTON)

        btn_remove.set_image( icon_remove )
        btn_remove.connect("clicked", self.remove_entry)

        btnbox.pack_start(entry, True, True, 0)
        btnbox.pack_end(btn_remove, True, True, 0)
        btnbox.child_set_property(btn_remove,"non-homogeneous", True)
        btn_remove.set_halign (Gtk.Align.CENTER)
        btn_remove.valign = Gtk.Align.CENTER

        vbox.pack_end( btnbox, True, True, 0 )
        vbox.show_all()

    def remove_entry(self, btn):
        btnbox = btn.get_parent()
        btnbox.destroy()
        window.resize(1, 1)

# costruisco lista *autori* per autocompletamento
conn = sqlite3.connect('./data/nn.db')

with conn:

    c = conn.cursor()
    c.execute("""SELECT nome, cognome
                 FROM autori
                 WHERE tipo = 1 OR tipo = 3""")

    lista_autori = c.fetchall()

    for row in lista_autori:
        print (row)

# costruisco lista *disegnatori* per autocompletamento
    c.execute("""SELECT nome, cognome
                 FROM autori
                 WHERE tipo = 2 OR tipo = 3""")

    lista_disegnatori = c.fetchall()

    for row in lista_disegnatori:
        print (row)



builder = Gtk.Builder()
builder.add_from_file("./data/ui/data_insertion.ui")
builder.connect_signals( Handler() )

window = builder.get_object("window")
window.show_all()

Gtk.main()

#FIXME non posso associare a soggetto e sceneggiatura la stessa EntryCompletion
