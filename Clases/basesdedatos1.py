# Para instalar el conector con mysql en una ubuntu o derivada:
# sudo apt install python3-mysql.connector
import mysql.connector

# Otro conector (que no he probado...) Y existen mas
# sudo apt install python3-pymsql
# import pymysql

#Siempre, al igual que con los ficheros, tenemos que capturar las excepciones
try:
	#conectamos con la base de datos proporcionando usuario, password, máquina donde está el gestor y nombre de la base de datos
    connect = mysql.connector.connect(user='josemaria', password='abc123', host='localhost', database='world')
    #cursor es un objeto que nos permitirá manipular la conexión que hemos abierto
    cursor = connect.cursor()
    sql = ("SELECT Name, District FROM City")
    #ejecutamos una query escribiéndola en un string al igual que la lanzaríamos desde consola
    cursor.execute(sql)

# Tres formas de ver los resultados del select (dos de ellas están comentadas)
# Pruébalas de forma alternativa y no todas a la vez
# En esta primera forma vemos solo dos campos del selecte
    for (nombre, distrito) in cursor:
        print(nombre, "-", distrito)

#	En esta segunda forma mostramos una a una las filas completas que nos devuelve el select
#	for fila in cursor:
#        print(fila)

# Por último en la tercera forma guardamos el resultado del select completo en una estructura
#	tupla = cursor.fetchall()
#    print(tupla)

except mysql.connector.Error as err:
    print(err)
else:
	# Cerramos el cursor y la conexión a la base de datos.
    cursor.close()
    connect.close()