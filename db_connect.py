import pyodbc
import pandas as pd
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'tcp:database-server' 
database = 'db-name'
username = 'username'
password = 'password'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
# select 26 rows from SQL table to insert in dataframe.
import sqlalchemy
import pyodbc
import urllib
# urllib.parse.quote_plus for python 3
params = urllib.parse.quote_plus(r'Driver={ODBC Driver 17 for SQL Server};Server=tcp:database-server,1433;Database=db-name;Uid=user@db-name.database.windows.net;Pwd=password;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')#write the DataFrame to a table in the sql database

conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
engine_azure = sqlalchemy.create_engine(conn_str,echo=True)
print('connection is ok')
print(engine_azure.table_names())

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/album.csv')
df.head()

df1 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/artista.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/autor.csv')
df3 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/canciones.csv')
df4 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/disquera.csv')
df5 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/genero.csv')
df6 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/premio.csv')
df7 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/RelAlbumArtista.csv')
df8 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/RelAlbumCancion.csv')
df9 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/RelAlbumPremios.csv')
df10 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/RelArtistaPremios.csv')
df11 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/RelAutorCancion.csv')
df12 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/RelCancionPremio.csv')
df13 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/RelDisqueraAlbum.csv')
df14 = pd.read_csv('https://raw.githubusercontent.com/Isiguenza/db-final/main/RelGeneroAlbum.csv')

df.to_sql('album', engine_azure)
df1.to_sql('artista', engine_azure)
df2.to_sql('autor', engine_azure)
df3.to_sql('canciones', engine_azure)
df4.to_sql('disquera', engine_azure)
df5.to_sql('genero', engine_azure)
df6.to_sql('premio', engine_azure)
df7.to_sql('relalbumartista', engine_azure)
df8.to_sql('relalbumcancion', engine_azure)
df9.to_sql('relalbumpremios', engine_azure)
df10.to_sql('relartistapremios', engine_azure)
df11.to_sql('relautorcancion', engine_azure)
df12.to_sql('relcancionpremio', engine_azure)
df13.to_sql('reldisqueraalbum', engine_azure)
df14.to_sql('relgeneroalbum', engine_azure)



print(engine_azure.table_names())

