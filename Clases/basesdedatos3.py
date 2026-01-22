import mysql.connector

#Ejemplo de borrado de datos. Base de datos chinook

def borrarTracks(connect, artista, album):
    cursor = connect.cursor()
    sql = "SELECT * FROM Artist WHERE Name = '" + artista + "'"
    # print(sql)
    cursor.execute(sql)
    resultado = cursor.fetchall()
    # print(len(resultado))
    if len(resultado) == 0:
        print("El artista", artista, "no existe")
    else:
        # print(resultado[0][0])
        sql = "SELECT * FROM Album WHERE Title = '" + album + "' AND ArtistId = " + str(resultado[0][0]);
        # print(sql)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            print("El album", album, "del artista", artista, "no existe")
        else:
            # print(resultado)
            sql = "SELECT * FROM Track WHERE AlbumId = " + str(resultado[0][0])
            # print(sql)
            cursor.execute(sql)
            resultado = cursor.fetchall()
            if len(resultado) == 0:
                print("Los tracks del album", album, "del artista", artista, "ya estaban borrados")
            else:
                for track in resultado:
                    # print(track)
                    sql = "DELETE FROM InvoiceLine WHERE TrackId = " + str(track[0])
                    # print(sql)
                    cursor.execute(sql)
                    sql = "DELETE FROM PlaylistTrack WHERE TrackId = " + str(track[0])
                    # print(sql)
                    cursor.execute(sql)
                    sql = "DELETE FROM Track WHERE TrackId = " + str(track[0])
                    # print(sql)
                    cursor.execute(sql)
                    print("Borrando Track", track[1], "...")
                # Si no hacemos un COMMIT los cambios no se guardan!
                connect.commit()
    cursor.close()

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='chinook')
    print("Conexión a la base de datos realizada correctamente")
    print("################")
    borrarTracks(connect, "María Jesús y su acordeón", "El baile de los pajaritos y otros grandes éxitos")
    print("################")
    borrarTracks(connect, "Iron Maiden", "Marchas procesionales de Semana Santa")
    print("################")
    borrarTracks(connect, "Iron Maiden", "Powerslave")
    print("################")
    borrarTracks(connect, "Amy Winehouse", "Frank")
    connect.close()
except mysql.connector.Error as err:
    print(err)
