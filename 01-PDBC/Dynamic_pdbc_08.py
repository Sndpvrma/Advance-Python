import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')

try:
    connection.autocommit(False)
    cursor = connection.cursor()

    sql1 = "INSERT INTO IT_EMPLOYEES VALUES(113, 'Govind', 'Backend Developer', 'Tech Mahindra', 87600)"
    sql2 = "INSERT INTO IT_EMPLOYEES VALUES(114, 'Anand', 'Frontend Developer', 'LTIMindtree', 92000)"
    sql3 = "INSERT INTO IT_EMPLOYEES VALUES(115, 'AJAY', 'Database Admin', 'Wipro', 97500)"

    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)

    connection.commit()

    print("Data inserted successful")

except Exception as e:
    connection.rollback()
    print("Data rolled back due to error", e)



connection.autocommit(True)
cursor = connection.cursor()

pageno = 4
pagesize = 8

if pageno > 0:
    offset = (pageno - 1) * pagesize
    sql = " SELECT * FROM IT_EMPLOYEES LIMIT " + str(offset) + ", " + str(pagesize)

    cursor.execute(sql)
    data = cursor.fetchall()
    print("The data of table IT_EMPLOYEES is:")
    for row in data:
        print(row[0], '\t', row[1], '\t  ', row[2], '\t    ', row[3], '\t  ', row[4])
connection.close()


