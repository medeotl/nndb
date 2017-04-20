import sqlite3

sqlite_file = 'my_first_db.sqlite'
table_name = 'my_table_2'
id_column = 'my_1st_column' # name of the PRIMARY KEY column
new_column1 = 'my_2nd_column'
new_column2 = 'my_3rd_column'
column_type = 'TEXT'
default_val = 'Hello World' # a default value for the new column

conn = sqlite3.connect( sqlite_file )
c = conn.cursor()

# A) Adding a new column without a row value
try:    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
            .format(tn=table_name, cn=new_column1, ct=column_type) )
except sqlite3.OperationalError as e:
    print( "ERRORE: Colonna già presente nella tabella {}".format(table_name) )
    print( str(e) + "\n" )
        
# B) Adding a new column with a *default* row value
try:    
    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
            .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val) )
except sqlite3.OperationalError as e:
    print( "ERRORE: Colonna già presente nella tabella {}".format(table_name) )
    print( str(e) + "\n" )
        
conn.commit()
conn.close()
