# indicizzazione di colonne della tabella.
# contro: non posso avere valori ripetuti nella colonna
# pro: prestazioni migliorate

import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column'
new_column = 'unique_names' # nuova colonna che inseriremo
column_type = 'TEXT'
index_name = 'my_unique_index'

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# aggiungo nuova colonna 'unique_names'
try:    
    c.execute( "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".\
            format(tn=table_name, cn=new_column, ct=column_type) )
except sqlite3.OperationalError as e:
    print( "ERRORE: Colonna già presente nella tabella {}".format(table_name) )
    print( str(e) + "\n" )

# aggiorno l'unica riga della tabella con il valore per 'unique_names'        
c.execute( "UPDATE {tn} SET {cn}='sebastian_r' WHERE {idf}=123456".\
        format(tn=table_name, cn=new_column, idf=id_column) )

# creo l'indicizzazione
c.execute( "CREATE INDEX {ix} ON {tn}({cn})".\
        format(ix=index_name, tn=table_name, cn=new_column) )
        
# Dropping the unique index
# E.g., to avoid future conflicts with update/insert functions (???)
c.execute( "DROP INDEX {ix}".format(ix=index_name) )

conn.commit()
conn.close()
