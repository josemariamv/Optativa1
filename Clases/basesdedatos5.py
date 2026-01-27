import mysql.connector

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()

    sql = "SELECT nombre, peso, altura FROM pokemon WHERE peso > 200"
    cursor.execute(sql)

    for fila in cursor:
        print(fila)

    sql = "UPDATE pokemon SET peso=350 WHERE peso > 250"
    cursor.execute(sql)
    # el metodo rowcount nos devuelve, en updates y deletes, el número de filas involucradas
    # en select no lo hace con 'nonbuffered' cursors que son los que estamos viendo
    # existe la opción de buffered cursors, pero no los vamos a ver
    print("La instrucción involucra a", cursor.rowcount, "filas de la base de datos")
    # si no ejecutamos un commit no se guardan los cambios
    #connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()

    # Podemos parametrizar el select igual que en JDBC
    sql = "SELECT nombre, peso, altura FROM pokemon WHERE peso > %s AND nombre = %s"
    datos = (250,'Snorlax')
    cursor.execute(sql, datos)

    for fila in cursor:
        print(fila)

    # Y lanzar múltiples querys (no válido con SELECT)
    sql = "INSERT INTO pokemon (numero_pokedex, nombre, peso, altura) VALUES (%s, %s, %s, %s)"
    datos = [(200, 'Pepe Potamo', 50, 30), (201, 'Inés Perado', 33, 600), (202,'Benito Camelas', 412, 30)]
    cursor.executemany(sql, datos)
    print("La instrucción involucra a", cursor.rowcount, "filas de la base de datos")

    cursor.execute("SELECT * FROM pokemon WHERE numero_pokedex >=200")
    for fila in cursor:
        print(fila)
    # si no ejecutamos un commit no se guardan los cambios
    #connect.commit()
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()
    # Activamos la posibilidad de ver los warnings
    cursor.get_warnings = True

    sql = "SELECT numero_pokedex, nombre FROM pokemon where numero_pokedex <=10"
    cursor.execute(sql)
    # Con fetchmany podemos indicar cuantas filas leer
    dosFilas = cursor.fetchmany(size=2)
    # y luego leer las restantes
    restantes = cursor.fetchall()
    print(dosFilas)
    print(restantes)

    # volvemos a ejecutar la query
    cursor.execute(sql)
    # y ahora vamos a ver otro método de leer una a una las filas de la query
    fila = cursor.fetchone()
    # sería igual que fila =cursor.fetchmany(size=1)
    # y luego iteramos con un bucle
    while fila is not None:
        print(fila)
        fila = cursor.fetchone()

    # si hubiera warnings los veríamos aquí
    print(cursor._warnings)

    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)
