import pymysql

def testdelete():
    connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='advancepython')
    cursor = connection.cursor()
    sql = "delete from user where id = 9"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data delete successfully")

def testdelete2():
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "delete from user where id = %s"
    data = (2,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data delete2 successfully")

def testdelete3(id):
    connection = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'advancepython')
    cursor = connection.cursor()
    sql = "delete from user where id = %s"
    data = (id,)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()
    print("Data delete3 successfully")

testdelete()
testdelete2()
testdelete3(8)
testdelete3(6)