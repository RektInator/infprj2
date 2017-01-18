import pymysql.cursors  #Importeer PyMySql


connection = pymysql.connect(host='178.62.226.124',      #Setup connectie naar de database
                             user='infprj2',
                             password='banaan',
                             db='opseilen',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def Query(x):
    try:
        with connection.cursor() as cursor:   #Geen idee
            sql = x      #De query zelf ingeput bij de functie
            cursor.execute(sql)
            result = cursor.fetchone()     #Resultaat
            connection.commit()
            return result     #Het resultaat van de query teruggeven

    finally:
        connection.close()
res = Query("SELECT * FROM score")
