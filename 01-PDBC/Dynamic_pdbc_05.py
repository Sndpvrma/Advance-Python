# Random Table Creation

import pymysql
import random


def test_insert():
    connection = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        db='advancepython'
    )
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS IT_EMPLOYEES (
        id INT PRIMARY KEY,
        name VARCHAR(50),
        position VARCHAR(50),
        company VARCHAR(50),
        salary INT)
        """)

    first_names = ["Rajesh", "Sunil", "Anil", "Megha", "Pooja", "Vikram", "Sanjay", "Kavita", "Ramesh", "Geeta", "Arun"]
    last_names = ["Iyer", "Nayar", "Reddy", "Kulkarni", "Deshmukh", "Pillai", "Chouham", "Saxena", "Malhotra", "Pandey"]
    companies = ["TCS", "Infosys", "Wipro", "HCL Technologies", "Tech Mahindra", "LITMindrtree"]
    positions = ["Frontend Developer", "Backend Developer", "QA Automation Engineer", "Cloud Architect", "Database Admin"]

    data = []
    for i in range (1, 111):
        full_name = random.choice(first_names) + " " + random.choice(last_names)
        pos = random.choice(positions)
        comp = random.choice(companies)
        salary = random.randint(45000, 185000)
        data.append((i, full_name, pos, comp, salary))

    sql = "INSERT INTO IT_EMPLOYEES VALUES(%s, %s, %s, %s, %s)"
    cursor.executemany(sql, data)
    connection.commit()
    connection.close()

    print("Table IT_EMPLOYEES created and " + str(len(data)) + "records inserted successfully")

test_insert()