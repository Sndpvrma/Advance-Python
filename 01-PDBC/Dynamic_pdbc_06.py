# use of pagination

import pymysql

def read_table(param = {}):
    id = param.get('id', 0)
    name = param.get('name', '')
    position = param.get('position', '')
    company = param.get('company', '')
    salary = param.get('salary', 0)
    pageno = param.get('pageno', 0)
    pagesize = param.get('pagesize', 0)

    connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='advancepython')
    cursor = connection.cursor()

    sql = "select * from IT_EMPLOYEES where 1=1"
    if id != 0:
        sql += " and id = " + str(id)
    if name != '':
        sql += " and name like '" + name + "%'"
    if position != '':
        sql += " and position like '" + position + "%'"
    if company != '':
        sql += " and company like '" + company + "%'"
    if salary != 0:
        sql += " and salary = " + str(salary)

    if pagesize > 0:
        offset = (pageno - 1) * pagesize
        sql += " Limit " + str(offset) + ", " + str(pagesize)

    print('sql=> ', sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        print(data[0],'\t', data[1],'\t', data[2],'\t     ', data[3],'\t              ', data[4])

    connection.commit()
    connection.close()

param = {'id': 0,
         'name': 'A',
         'position': '',
         'company': '',
         'salary': 0,
         'pageno': 4,
         'pagesize': 7
}

read_table(param)