# aggiornare (o aggiungere se non esiste) una riga nella tabella
# workaround per la mancanza del comando UPSERT in sqlite3

import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
column_name = 'my_2nd_column'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Inserisco riga con ID 123456 (valore my_3rd_column non specificato) 
try:
    c.execute( "INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
            format(tn=table_name, idf=id_column, cn=column_name) )
except sqlite3.IntegrityError:
    # esiste già una riga con quell'ID
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

# B) Come sopra ma in caso di errore lo ignora
c.execute( "INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name) )
        
# C) Updates the newly inserted or pre-existing entry
c.execute( "UPDATE {tn} SET {cn}=('Hi World') WHERE {idf}=(123456)".\
        format(tn=table_name, cn=column_name, idf=id_column) )

conn.commit()
conn.close() 
