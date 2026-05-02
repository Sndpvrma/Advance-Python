# Login Attempt Module

import pymysql
from datetime import datetime

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='module')

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("Drop table if exists Login_attempt")
    sql = """Create Table if not exists Login_attempt(
    attemptID BIGINT PRIMARY KEY,
    attemptCode VARCHAR(100),
    userName VARCHAR(100),
    attemptTime DATETIME,
    status VARCHAR(100)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_data():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "Insert into Login_attempt VALUES (%s, %s, %s, NOW(), %s)"
    data = [
        (1, 'LOG_001', 'amit_sharma', 'Success'),
        (2, 'LOG_002', 'priya_v', 'Failed'),
        (3, 'LOG_003', 'rahul_99', 'Success'),
        (4, 'LOG_004', 'admin_user', 'Blocked'),
        (5, 'LOG_005', 'guest_01', 'Success'),
        (6, 'LOG_006', 'vikas_kumar', 'Failed'),
        (7, 'LOG_007', 'sneh_lata', 'Success'),
        (8, 'LOG_008', 'rohit_mehra', 'Success'),
        (9, 'LOG_009', 'neha_singh', 'Failed'),
        (10, 'LOG_010', 'unknown_bot', 'Blocked')
    ]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully")

def read_table(params = {}):
    attemptID = params.get('attemptID', 0)
    attemptCode = params.get('attemptCode', '')
    userName = params.get('userName', '')
    status = params.get('status', '')
    pageno =params.get('pageno', 0)
    pageSize = params.get('pageSize', 0)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * FROM Login_attempt WHERE 1=1 "
    if attemptID != 0:
        sql += " AND attemptID = " + str(attemptID)
    if attemptCode != '':
        sql += " AND attemptCode like '" + attemptCode + "%'"
    if userName != '':
        sql += " AND userName like '" + userName + "%'"
    if status != '':
        sql += " AND status like '" + status + "'"

    if pageno > 0:
        offset = (pageno - 1) * pageSize
        sql += " LIMIT " + str(offset) + ", " + str(pageSize)

    print("sql=> ", sql)
    cursor.execute(sql)
    print("The data of Login Attempt: ")
    result = cursor.fetchall()
    for row in result:
        print(row[0], '\t', row[1], '\t', row[2], '\t', row[3], '\t', row[4])
    connection.commit()
    connection.close()
    print("Data Read successfully")

def update_table():
    connection = get_connection()
    connection.autocommit(False)
    cursor = connection.cursor()

    try:
        print("Start inserting data...")
        cursor.execute("insert into Login_attempt VALUES(11, 'AB11', 'electron', NOW(), 'Active')")
        print("Creating Savepoint sp1...")
        cursor.execute("Savepoint sp1")
        try:
            cursor.execute("insert into Login_attempt VALUES(12, 'AB12', 'proton', NOW(), 'Active')")
            print("Creating Savepoint sp2...")
            cursor.execute("Savepoint sp2")
            try:
                cursor.execute("insert into Login_attempt VALUES(11, 'AB11', 'proton', NOW(), 'Active')")
                print("Creating Savepoint sp3...")
                cursor.execute("Savepoint sp3")

            except Exception as e:
                print("Error in third insert, rolling back to Savepoint sp2")
                cursor.execute("rollback to Savepoint sp2")
        except Exception as e:
            print("Error in second insert, rolling back to Savepoint sp1")
            cursor.execute("rollback to Savepoint sp1")
        print("Commiting transaction...")
        connection.commit()
    except Exception as e:
        connection.rollback()
        print("Error in transaction", e)
    finally:
        cursor.close()
        connection.close()

def delete_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "Delete from Login_attempt where attemptID = 10"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data Deleted successfully")




create_table()
insert_data()

params = {
    'attemptID' : 1,
    'attemptCode' : '1',
    'userName' : 'admin',
    'attemptTime' : '1',
    'status' : '1',
    'pageno' : 0,
    'pageSize' : 0
}

read_table(params = {})
update_table()
delete_table()