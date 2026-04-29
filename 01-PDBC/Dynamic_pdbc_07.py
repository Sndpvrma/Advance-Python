import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='advancepython')
connection.autocommit(True)
cursor = connection.cursor()

sql1 = "insert into IT_EMPLOYEES values(111, 'Rajesh', 'Backend Developer', 'TCS', 120000)"
sql2 = "insert into IT_EMPLOYEES values(112, 'Shyam', 'Frontend Developer', 'Wipro', 119000)"
sql3 = "Insert into IT_EMPLOYEES values(111, 'Mohan', 'Cloud Architect', 'Infosys', 135000)"

cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
connection.close()

print("Data inserted successfully")