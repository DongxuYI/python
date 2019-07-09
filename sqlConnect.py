import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='YI.9694482664',
    database='test_mysql',
    charset='utf8'
)
cursor = conn.cursor()
sql = 'select * from users'
res = cursor.execute(sql)
result = cursor.fetchall(sql)
print(res)
print(result)
conn.close()
cursor.close()