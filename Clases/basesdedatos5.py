
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

'''
insert_stmt = (
  "INSERT INTO employees (emp_no, first_name, last_name, hire_date) "
  "VALUES (%s, %s, %s, %s)"
)
data = (2, 'Jane', 'Doe', datetime.date(2012, 3, 23))
cursor.execute(insert_stmt, data)

select_stmt = "SELECT * FROM employees WHERE emp_no = %(emp_no)s"
cursor.execute(select_stmt, { 'emp_no': 2 })

data = [
  ('Jane', date(2005, 2, 12)),
  ('Joe', date(2006, 5, 23)),
  ('John', date(2010, 10, 3)),
]
stmt = "INSERT INTO employees (first_name, hire_date) VALUES (%s, %s)"
cursor.executemany(stmt, data)

>>> cursor.execute("SELECT * FROM employees ORDER BY emp_no")
>>> head_rows = cursor.fetchmany(size=2)
>>> remaining_rows = cursor.fetchall()

# Using a while loop
cursor.execute("SELECT * FROM employees")
row = cursor.fetchone()
while row is not None:
  print(row)
  row = cursor.fetchone()

# Using the cursor as iterator
cursor.execute("SELECT * FROM employees")
for row in cursor:
  print(row)

>>> cnx.get_warnings = True
>>> cursor.execute("SELECT 'a'+1")
>>> cursor.fetchall()
[(1.0,)]
>>> print(cursor.warnings)
[(u'Warning', 1292, u"Truncated incorrect DOUBLE value: 'a'")]

cnx = mysql.connector.connect(user='scott', database='test')
cursor = cnx.cursor()
operation = 'SELECT 1; UPDATE t1 SET c1 = 2; SELECT 2'
for result in cursor.execute(operation):
  if result.with_rows:
    result.fetchall()
  else:
    print("Number of affected rows: {}".format(result.rowcount))

'''