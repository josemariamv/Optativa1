# Para instalar el conector con mysql en una ubuntu o derivada:
# sudo apt install python3-mysql.connector
# En un proyecto con un entorno virtual instalamos directamente con el gestor de paquetes y pip
import mysql.connector

#Siempre, al igual que con los ficheros, tenemos que capturar las excepciones
try:
	#conectamos con la base de datos proporcionando usuario, password, máquina donde está el gestor
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost')
    #cursor es un objeto que nos permitirá manipular la conexión que hemos abierto
    cursor = connect.cursor()
    # ejecutamos una query escribiéndola en un string al igual que la lanzaríamos desde consola
    cursor.execute("SHOW DATABASES")
    # Mostramos una a una las filas que nos devuelve el select
    for fila in cursor:
        print(fila)
    # cerramos el cursor primero y la conexión después
    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)

try:
    # añadimos ahora la base de datos en la conexión
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()

    sql = ("SELECT nombre, peso, altura from pokemon")
    # sql = ("SELECT * from pokemon") # así no funcionaría...
    cursor.execute(sql)

    # En esta forma podemos ver solo los campos del select que nos interesen
    for (nombre, peso, altura) in cursor:
        print(nombre, "-", peso, "-", altura)

    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)

try:
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='pokemondb')
    cursor = connect.cursor()
    sql = ("SELECT nombre, peso, altura from pokemon")
    cursor.execute(sql)

    # De esta última forma guardamos el resultado del select completo en una estructura
    tupla = cursor.fetchall()
    print(tupla)

    cursor.close()
    connect.close()
except mysql.connector.Error as err:
    print(err)