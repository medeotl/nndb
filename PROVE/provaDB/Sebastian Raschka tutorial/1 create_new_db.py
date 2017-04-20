# Creo due tabelle
# my_table_1 --> |my_1st_column| integer
# my_table_2 --> |my_1st_column| integer PRIMARY KEY

import sqlite3

sqlite_file = 'my_first_db.sqlite' # name of the sqlite database file
table_name1 = 'my_table_1' # name of the table to be created
table_name2 = 'my_table_2' # name of the table to be created
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER' # column data type

# Connecting to the database file (se non esiste lo crea)
conn = sqlite3.connect( sqlite_file )
c = conn.cursor()

# Creating a new SQLite table with 1 column
try:
    c.execute( "CREATE TABLE {tn} ({nf} {ft})"\
            .format(tn=table_name1, nf=new_field, ft=field_type) )
except sqlite3.OperationalError as e:
    print( "ERRORE: Tabella già presente nel DB" )
    print( str(e) + "\n" )
    
# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!

try:
    c.execute( "CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)"\
            .format(tn=table_name2, nf=new_field, ft=field_type) )
except sqlite3.OperationalError as e:
    print( "ERRORE: Tabella già presente nel DB" )
    print( str(e) + "\n" )

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()        
