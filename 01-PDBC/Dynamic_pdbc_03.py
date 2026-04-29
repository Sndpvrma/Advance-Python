import pymysql

def testupdate1():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
    cursor = connection.cursor()
    sql = "UPDATE user SET name = 'Rihanna' WHERE id = 2"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Updated Successfully")

def testupdate2():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "UPDATE user set name = %s WHERE id = %s"
    data = ('Steve', 1)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Updated2 Successfully")

def testupdate3(name, id):
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "UPDATE user set name = %s WHERE id = %s"
    data = (name, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Updated3 Successfully")

def testupdate4(data):
    id = data['id']
    name = data['name']
    last_name = data['last_name']
    salary = data['salary']
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', password = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "UPDATE user set name = %s, lastname = %s, salary = %s, id = %s"
    data = (name, last_name, salary, id)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data Updated4 Successfully")

testupdate1()
testupdate2()
testupdate3('mitchel', 3)
testupdate3('josh', 4)

params = {}
params['id'] = 1
params['name'] = 'Rihanna'
params['last_name'] = 'Steve'
params['salary'] = 100

testupdate4(params)