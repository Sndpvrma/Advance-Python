import pymysql

connection = pymysql.connect(host='localhost', port = 3306, user='root', password='root', db= 'advancepython')
connection.autocommit(False)
cursor = connection.cursor()

try:
    print("Start inserting data...")
    cursor.execute("Insert into IT_EMPLOYEES VALUES(117, 'Sonu', 'Backend Developer', 'TCS', 108700)")

    print("Creating savepoint sp1...")
    cursor.execute("Savepoint sp1")

    try:
        cursor.execute("Insert into IT_EMPLOYEES VALUES(118, 'Vijay', 'Backend Developer', 'Wipro', 106700)")
        print("Creating savepoint sp2...")
        cursor.execute("Savepoint sp2")

    except Exception as e:
        print("Error in second insert, rolling back to savepoint sp1... ")
        cursor.execute("rollback to Savepoint sp1")

    try:
        cursor.execute("Insert into IT_EMPLOYEES VALUES(119, 'Gajendra', 'Cloud Architect', 'HCL Technologies', 121700)")
        print("Second insert successful")
        print("Creating savepoint sp3...")
        cursor.execute("Savepoint sp3")

    except Exception as e:
        print("Error in third insert, rolling back to savepoint sp1... ")
        cursor.execute("rollback to Savepoint sp1")

    print("Committing transaction...")
    connection.commit()
except Exception as e:
    print("Error in transaction:", e)
    connection.rollback()

finally:
    cursor.close()
    connection.close()

pageno = 12
pagesize = 10

if pageno > 0:
    offset = (pageno - 1) * pagesize
    sql = "SELECT * FROM IT_EMPLOYEES LIMIT " + str(offset) + ", " + str(pagesize)
    cursor.execute(sql)
    data = cursor.fetchall()
    print("The data of table IT_EMPLOYEES is:")
    for row in data:
        print(row[0], '\t ', row[1], '\t    ', row[2], '\t    ', row[3], ' \t       ', row[4])
    connection.commit()

connection.close()

