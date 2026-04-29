import pymysql

def testread1():
    connection = pymysql.connect(host='localhost', port = 3306, user='root', passwd='root', db='advancepython')
    cursor = connection.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row)
    connection.commit()
    connection.close()
    print("Data Read Successfully")
    print("\n")

def testread2():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "select * from user"
    cursor.execute(sql)
    data = cursor.fetchall()
    columnName = ('id', 'name', 'LastName', 'Salary')
    for x in data:
        print(x)
    connection.commit()
    connection.close()

def testread3():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "select * from user"
    sql = "select * from user where id = 1"
    sql = "select * from user where lastname = 'kumar'"
    sql = "select * from user where name like 'a%' "
    sql = "select * from user where salary = 77000 "

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t')
    connection.commit()
    connection.close()

def testread4(id, name, lastname, salary):
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()

    sql = "select * from user"
    if id != 0:
        sql += " where id " + str(id)
    if name != '':
        sql += " where name like '" + name + "%'"
    if lastname != '':
        sql += " where lastname like '" + lastname + "%'"
    if salary != 0:
        sql += " where salary = " + str(salary)
    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3], '\t')
    connection.commit()
    connection.close()

def testread5(param ={}):
    id = param.get('id', 0)
    name = param.get('name', '')
    lastname = param.get('lastname', '')
    salary = param.get('salary', 0)

    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()

    sql = "select * from user where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if name != '':
        sql += " and name like '" + name + "%'"
    if lastname != '':
        sql += " and lastname like '" + lastname + "%'"
    if salary != 0:
        sql += " and salary = " + str(salary)

    print('sql => ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])
    connection.commit()
    connection.close()

def testread6(param={}):
    id = param.get('id', 0)
    name = param.get('name', '')
    lastname = param.get('lastname', '')
    salary = param.get('salary', 0)
    pageno =param.get('pageno', 0)
    pagesize = param.get('pagesize', 0)

    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()

    sql = "select * from user where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if name != '':
        sql += " and name like '" "%"+ name + "%'"
    if lastname != '':
        sql += " and lastname like '" + lastname + "%'"
    if salary != 0:
        sql += " and salary = " + str(salary)

    # Pagination
    if pagesize > 0:
        offset = (pageno - 1) * pagesize
        sql += " Limit " + str(offset) + ", " + str(pagesize)

    print('sql => ', sql)

    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0], '\t', data[1], '\t', data[2], '\t', data[3])

    connection.commit()
    connection.close()

testread1()
testread2()
testread3()
testread4(0, 'a', '', 0)

param = {'id':0,
         'name': 'a',
         'lastname': '',
         'salary': 0,
         'pageno': 1,
         'pagesize': 3}

testread5(param)
testread6(param)