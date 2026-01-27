
import mysql.connector

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()

    sql = ("SELECT nombre, peso, altura from pokemon where peso > 250")
    cursor.execute(sql)

    for fila in cursor:
        print(fila)

    sql = ("UPDATE pokemon SET peso=350 WHERE peso > 250")
    cursor.execute(sql)
    # el metodo rowcount nos devuelve, en updates y deletes, el número de filas involucradas
    print("La instrucción involucra a", cursor.rowcount, "filas de la base de datos")
    # si no ejecutamos un commit no se guardan los cambios
    #connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)

