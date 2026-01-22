#!/usr/bin/python
import mysql.connector


def modificaEmpleado(connect, cliente, codigo):
    cursor = connect.cursor()
    cliente = cliente.replace("'", "\\'")
    # print(cliente)
    cursor.execute("SELECT salesRepEmployeeNumber FROM customers WHERE customerName = '" + cliente + "'")
    resultado = cursor.fetchall()
    if len(resultado) != 0:
        for fila in resultado:
            if fila[0] is None:
                print("El cliente", cliente, "no tiene asignado ningún empleado")
            else:
                sql1 = "SELECT firstName, lastName FROM employees WHERE employeeNumber = " + str(fila[0])
                cursor.execute(sql1)
                resultado2 = cursor.fetchall()
                print("Empleado Antiguo: ")
                for fila2 in resultado2:
                    print(fila2[0] + " " + fila2[1])
            sql2 = "SELECT firstName, lastName FROM employees WHERE employeeNumber = " + str(codigo)
            cursor.execute(sql2)
            resultado3 = cursor.fetchall()
            if len(resultado3) != 0:
                print("Empleado nuevo:")
                for fila3 in resultado3:
                    print(fila3[0] + " " + fila3[1])
                sql3 = "UPDATE customers SET salesrepEmployeeNumber = " + str(
                    codigo) + " WHERE customerName = '" + cliente + "'"
                # print(sql3)
                cursor.execute(sql3)
                connect.commit()
            else:
                print("No existe el código de empleado", codigo)
    else:
        print("No existe el cliente", cliente)


try:
    connect = mysql.connector.connect(user="examen", password="Qwerty1234+", host="localhost", database="classicmodels")
    print("Conexión a la base de datos realizada correctamente")
    print("################")
    modificaEmpleado(connect, "Morales", 1234)
    print("################")
    modificaEmpleado(connect, "Frau da Collezione", 666)
    print("################")
    modificaEmpleado(connect, "Warburg Exchange", 1370)
    print("################")
    modificaEmpleado(connect, "Kelly's Gift Shop", 1370)
    connect.close()
except mysql.connector.Error as error:
    print(error)
