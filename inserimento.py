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
        """ carica un entry aggiuntiva (per autori multipli) """
        vbox = btn.get_parent().get_parent()
        btnbox = Gtk.ButtonBox(Gtk.Orientation.HORIZONTAL)

        entry = Gtk.Entry()
        btn_remove = Gtk.Button()
        icon_remove = Gtk.Image()
        icon_remove.set_from_icon_name(
            "list-remove", Gtk.IconSize.BUTTON)

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
        """ rimuove l'entry aggiuntiva (per autori multipli) """
        btnbox = btn.get_parent()
        btnbox.destroy()
        window.resize(1, 1)

builder = Gtk.Builder()
builder.add_from_file("./data/ui/data_insertion.ui")
builder.connect_signals( Handler() )

# creo lista autori/disegnatori/copertinista per autocompletamento
scrittori_store = Gtk.ListStore(str)
disegnatori_store = Gtk.ListStore(str)
copertinista_store = Gtk.ListStore(str)

conn = sqlite3.connect('./data/nn.db')
with conn:

    # AUTORI (soggettisti e sceneggiatori)
    c = conn.cursor()
    c.execute("""SELECT nome, cognome
                 FROM autori
                 WHERE tipo = 1 OR tipo = 3""")

    lista_autori = c.fetchall()

    for autore in lista_autori:
        autore = autore[0] + " " + autore[1]
        iter = scrittori_store.append()
        scrittori_store.set(iter, 0, autore)

    # DISEGNATORI
    c.execute("""SELECT nome, cognome
                 FROM autori
                 WHERE tipo = 2 OR tipo = 3""")

    lista_disegnatori = c.fetchall()

    for disegnatore in lista_disegnatori:
        disegnatore = disegnatore[0] + " " + disegnatore[1]
        iter = disegnatori_store.append()
        disegnatori_store.set(iter, 0, disegnatore)

    # COPERTINISTI
    lista_copertinisti = ("Claudio Castellini", "Roberto De Angelis",
        "Sergio Giardo")
    for copertinista in lista_copertinisti:
        iter = copertinista_store.append()
        copertinista_store.set(iter, 0, copertinista)


sogg_entry = builder.get_object("soggetto_entry")
scen_entry = builder.get_object("sceneggiatura_entry")
dis_entry = builder.get_object("disegni_entry")
cop_entry = builder.get_object("copertinista_entry")

sogg_completion = Gtk.EntryCompletion()
scen_completion = Gtk.EntryCompletion()
dis_completion = Gtk.EntryCompletion()
cop_completion = Gtk.EntryCompletion()

sogg_entry.set_completion(sogg_completion)
scen_entry.set_completion(scen_completion)
dis_entry.set_completion(dis_completion)
cop_entry.set_completion(cop_completion)

sogg_completion.set_model(scrittori_store)
scen_completion.set_model(scrittori_store)
dis_completion.set_model(disegnatori_store)
cop_completion.set_model(copertinista_store)

sogg_completion.set_text_column(0)
scen_completion.set_text_column(0)
dis_completion.set_text_column(0)
cop_completion.set_text_column(0)

window = builder.get_object("window")
window.show_all()

Gtk.main()
