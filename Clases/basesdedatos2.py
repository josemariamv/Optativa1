import mysql.connector

#Ejemplo de consulta de datos. Base de datos chinook

def buscarTema(connect, tema):
    cursor = connect.cursor()
    sql = "DESCRIBE Artist"
    cursor.execute(sql)

    sql = "SELECT Track.Name, Album.Title, Artist.Name as Artist from Track INNER JOIN Album ON Track.AlbumId = Album.AlbumId INNER JOIN Artist ON Album.ArtistId = Artist.ArtistId WHERE Track.Name = '" + tema + "'"
    # print(sql)
    cursor.execute(sql)
    resultado = cursor.fetchall()
    # print(len(resultado))
    if len(resultado) == 0:
        print("No hay ningún tema con el nombre", tema)
    else:
        print("Álbunes donde aparece el tema ", tema, " y artista que lo interpreta")
        for (tema, album, artista) in resultado:
            print(album, "-", artista)
    cursor.close()

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='chinook')
    print("Conexión a la base de datos realizada correctamente")
    print("################")
    buscarTema(connect, "Let there be rock")
    print("################")
    buscarTema(connect, "La gallina turuleta")
    print("################")
    buscarTema(connect, "Wrathchild")
    connect.close()
except mysql.connector.Error as err:
    print(err)