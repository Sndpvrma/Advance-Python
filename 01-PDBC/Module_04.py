import pymysql

def get_connection():
    return pymysql.connect(host='localhost', port=3306, user='root', password='root', db='module')


def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("Drop Table if exists batch_module")
    sql = """CREATE TABLE batch_module(
    batchID BIGINT PRIMARY KEY,
    batchCode VARCHAR(50),
    totalMessages INT,
    processedCount INT,
    status VARCHAR(50)
    )
    """
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Table created successfully")

def insert_data():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO batch_module VALUES(%s, %s, %s, %s, %s)"
    data = [
        (1, 'OTP_BATCH_01', 1000, 1000, 'COMPLETED'),
        (2, 'PROMO_SUMMER_24', 5000, 2500, 'IN_PROGRESS'),
        (3, 'SYSTEM_ULERT_UX', 150, 0, 'PENDING'),
        (4, 'KYC_REMAINDER_09', 2200, 2200, 'COMPLETED'),
        (5, 'INV_STK_LEVEL', 800, 150, 'IN_PROGRESS'),
        (6, 'BILL_PAY_SEPT', 4500, 0, 'PENDING'),
        (7, 'RECHARGE_OFFER', 3000, 3000, 'COMPLETED'),
        (8, 'PWD_RESET_LOG', 500, 480, 'FAILED'),
        (9, 'NEWSLETTER_OCT', 10000, 1200, 'IN_PROGRESS'),
        (10, 'SECURITY_PATCH_V2', 50, 50, 'COMPLETED')
    ]
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()
    print("Data inserted successfully")

def read_data(params = {}):
    batchID = params.get('batchID', 0)
    batchCode = params.get('batchCode', '')
    totalMessages = params.get('totalMessages', 0)
    processedCount = params.get('processedCount', 0)
    status = params.get('status', '')
    pageno = params.get('pageno', 0)
    pagesize = params.get('pagesize', 0)

    connection = get_connection()
    cursor = connection.cursor()

    sql = "SELECT * FROM batch_module WHERE 1=1"
    if batchID != 0:
        sql += " AND batchID = " + str(batchID)
    if batchCode != '':
        sql += " AND batchCode like '" + batchCode + "%'"
    if totalMessages != '':
        sql += " AND totalMessages = " + str(totalMessages)
    if processedCount != 0:
        sql += " AND processedCount = " + str(processedCount)
    if status != '':
        sql += " AND status like '" + status + "%'"

    if pageno > 0:
        offset = (pageno - 1) * pagesize
        sql += " LIMIT " + str(offset) + ", " + str(pagesize)

    print("sql=>", sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    print("Data of batch module:\n")
    for data in result:
        print(data[0], data[1], data[2], data[3], data[4])
    connection.commit()
    connection.close()

def update_data():
    connection = get_connection()

    try:
        cursor = connection.cursor()
        connection.autocommit(False)

        sql1 = "INSERT INTO batch_module VALUES(11, TRANS_NOTIF_01',250, 0, 'PENDING')"
        sql2 = "INSERT INTO batch_module VALUES(12, 'URGENT_MSG_99', 10, 10, 'COMPLETED')"
        sql3 = "INSERT INTO batch_module VALUES(11, 'FESTIVE_GREET', 1200, 500, 'IN_PROGRESS')"

        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print("Error occurred while updating data", e)

    finally:
        connection.close()



def dalete_data():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "Delete from batch_module where batchID = 4"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    print("Data deleted successfully")

get_connection()
create_table()
insert_data()

param = {
    'batchID' : 1,
    'batchCode' : '',
    'totalMessages' : 0,
    'processedCount' : 0,
    'status' : '',
    'pageno' : 1,
    'pagesize' : 5

}

read_data(param)

update_data()
dalete_data()


