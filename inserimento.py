#! /usr/bin/python3
# -*- coding: utf-8 -*-

import gi
gi.require_version( 'Gtk', '3.0' )
from gi.repository import Gtk
from database import db
import sqlite3

class Handler:

    def onDeleteWindow( self, *args ):
        Gtk.main_quit( *args )

    def onAlboChange( self, spinBtn ):
        """  """
        pass

    def insert( self, btn ):
        """ inserisco i dati nel database e passo ad albo successivo """

        # creo classe di supporto per i miei dati
        class Albo:
            # numero (int)
            # titolo (string)
            # autori (list)
            # sceneggiatori (list)
            # disegnatori (list)
            # copertinista (string)
            pass

        albo = Albo()
        
        # prelevo dati albo e li visualizzo nel terminale
        nro_albo = builder.get_object( "nro_albo" )
        albo.numero = nro_albo.get_value_as_int()
        titolo = builder.get_object( "titolo" )
        albo.titolo = titolo.get_text()
        print( albo.numero, albo.titolo )
        soggetto = builder.get_object( "soggettisti" )
        soggetto_childrens = soggetto.get_children()
        albo.autori = []
        for item in soggetto_childrens:
            albo.autori.append( item.get_children()[0].get_text() )
        print( *albo.autori, sep=", " )
        sceneggiatura = builder.get_object( "sceneggiatori" )
        sceneggiatura_childrens = sceneggiatura.get_children()
        albo.sceneggiatori = []
        for item in sceneggiatura_childrens:
            albo.sceneggiatori.append( item.get_children()[0].get_text() )
        print( *albo.sceneggiatori, sep=", " )
        disegnatori = builder.get_object( "disegnatori" )
        disegnatori_childrens = disegnatori.get_children()
        albo.disegnatori = []
        for item in disegnatori_childrens:
            albo.disegnatori.append( item.get_children()[0].get_text() )
        print( *albo.disegnatori, sep=", " )
        copertina = builder.get_object( "copertinista" )
        albo.copertinista = copertina.get_text()
        print( albo.copertinista )

        # salvo albo in database

        # vado ad albo successivo
        nro_albo.spin( Gtk.SpinType.STEP_FORWARD, 1 )

        # pulisco le entry principali (meno il copertinista, che solitamente resta uguale)
        for entry in (titolo, sogg_entry, scen_entry, dis_entry):
            entry.set_text( "" )

        # rimuovo le eventuali sotto-entry di soggetto, sceneggiatura, disegni
        for item in soggetto_childrens[1:]:
            self.remove_entry( item.get_children()[1] )
        for item in sceneggiatura_childrens[1:]:
            self.remove_entry( item.get_children()[1] )
        for item in disegnatori_childrens[1:]:
            self.remove_entry( item.get_children()[1] )

        # imposto il focus alla entry del titolo
        titolo.grab_focus()

    def add_entry( self, btn ):
        """ carica un entry aggiuntiva (per autori multipli) """

        vbox = btn.get_parent().get_parent()
        btnbox = Gtk.ButtonBox( orientation=Gtk.Orientation.HORIZONTAL )

        entry = Gtk.Entry()
        btn_remove = Gtk.Button()
        icon_remove = Gtk.Image()
        icon_remove.set_from_icon_name( "list-remove", Gtk.IconSize.BUTTON )

        btn_remove.set_image( icon_remove )
        btn_remove.connect( "clicked", self.remove_entry )

        btnbox.pack_start( entry, True, True, 0 )
        btnbox.pack_end( btn_remove, True, True, 0 )
        btnbox.child_set_property( btn_remove, "non-homogeneous", True )
        btn_remove.set_halign( Gtk.Align.CENTER )

        vbox.pack_start( btnbox, True, True, 0 )
        vbox.show_all()

    def remove_entry( self, btn ):
        """ rimuove l'entry aggiuntiva (per autori multipli) """

        btnbox = btn.get_parent()
        btnbox.destroy()
        window.resize( 1, 1 )

builder = Gtk.Builder()
builder.add_from_file( "./data/ui/data_insertion.ui" )
builder.connect_signals( Handler() )

# creo lista autori/disegnatori/copertinista per autocompletamento
scrittori_store = Gtk.ListStore( str )
disegnatori_store = Gtk.ListStore( str )
copertinista_store = Gtk.ListStore( str )

conn = sqlite3.connect( './data/nn.db' )
with conn:

    # AUTORI (soggettisti e sceneggiatori)
    c = conn.cursor()
    c.execute("""SELECT nome, cognome
                 FROM autori
                 WHERE tipo = 1 OR tipo = 3""") # 3 autore completo

    lista_autori = c.fetchall()

    for autore in lista_autori:
        autore = autore[0] + " " + autore[1]
        iteratore = scrittori_store.append()
        scrittori_store.set( iteratore, 0, autore )

    # DISEGNATORI
    c.execute("""SELECT nome, cognome
                 FROM autori
                 WHERE tipo = 2 OR tipo = 3""") # 3 autore completo

    lista_disegnatori = c.fetchall()

    for disegnatore in lista_disegnatori:
        disegnatore = disegnatore[0] + " " + disegnatore[1]
        iteratore = disegnatori_store.append()
        disegnatori_store.set( iteratore, 0, disegnatore )

    # COPERTINISTI
    lista_copertinisti = ( "Claudio Castellini", "Roberto De Angelis", "Sergio Giardo" )
    for copertinista in lista_copertinisti:
        iteratore = copertinista_store.append()
        copertinista_store.set( iteratore, 0, copertinista )


sogg_entry = builder.get_object( "soggetto" )
scen_entry = builder.get_object( "sceneggiatura" )
dis_entry = builder.get_object( "disegni" )
cop_entry = builder.get_object( "copertinista" )

sogg_completion = Gtk.EntryCompletion()
scen_completion = Gtk.EntryCompletion()
dis_completion = Gtk.EntryCompletion()
cop_completion = Gtk.EntryCompletion()

sogg_entry.set_completion( sogg_completion )
scen_entry.set_completion( scen_completion )
dis_entry.set_completion( dis_completion )
cop_entry.set_completion( cop_completion )

sogg_completion.set_model( scrittori_store )
scen_completion.set_model( scrittori_store )
dis_completion.set_model( disegnatori_store )
cop_completion.set_model( copertinista_store )

sogg_completion.set_text_column( 0 )
scen_completion.set_text_column( 0 )
dis_completion.set_text_column( 0 )
cop_completion.set_text_column( 0 )

window = builder.get_object( "window" )
window.show_all()

Gtk.main()
