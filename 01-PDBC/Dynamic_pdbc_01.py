import pymysql

def testinsert():
    connection =  pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO USER VALUES(4, 'Ramesh', 'shar,a', 81000)"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Inserted Successfully")

def testinsert1():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO USER VALUES(%s, %s, %s, %s)"
    data = [
    (5, 'Rahul', 'Sharma', 85000),
    (6, 'Anjali', 'Verma', 90000),
    (7, 'Amit', 'Singh', 72000)
]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted Successfully")

def testinsert2(id, Name, LastName, Salary):
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO USER VALUES(%s, %s, %s, %s)"
    data = (id, Name, LastName, Salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted Successfully")

def testinsert3(id, name, LastName, Salary):
    connection = pymysql.connect(host='localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO user VALUES (%s, %s, %s, %s)"
    data = (id, name, LastName, Salary)
    cursor.execute(sql, data)
    connection.commit()
    cursor.close()
    print("Data Inserted Successfully")

def testinsert4(data ={}):
    id = data['id']
    name = data['name']
    last_name = data['last_name']
    salary = data['salary']
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "INSERT INTO user VALUES(%s, %s, %s, %s)"
    data = (id, name, last_name, salary)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Inserted Successfully")

testinsert3(9, 'raja', 'sahu', 91000)
testinsert3(10, 'rani', 'kushwah', 7700)


testinsert()
testinsert1()
testinsert2(8, 'raju', 'yadav', 88000)
testinsert4({'id': 10,
             'Name': 'raja',
             'Last_name': 'yadav',
             'Salary': 77000})
