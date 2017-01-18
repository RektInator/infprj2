import pymysql.cursors
connection = pymysql.connect(host='178.62.226.124',
                             user='infprj2',
                             password='banaan',
                             db='opseilen',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        sql = "SELECT * FROM score"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        connection.commit()

finally:
    connection.close()