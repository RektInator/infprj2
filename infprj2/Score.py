import pymysql.cursors


connection = pymysql.connect(host='178.62.226.124',
                             user='infprj2',
                             password='banaan',
                             db='opseilen',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def Query(x):
    try:
        with connection.cursor() as cursor:
            sql = str(x)
            cursor.execute(sql)
            result = cursor.fetchone()
            connection.commit()
            return result

    finally:
        connection.close()
