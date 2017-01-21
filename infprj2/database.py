import pymysql.cursors
import pygame

db = pymysql.connect(host='178.62.226.124',
                             user='infprj2',
                             password='banaan',
                             db='opseilen')

def init():
    pass

# executes a database query and returns the result
def execute_query(sql):
    cur = db.cursor(pymysql.cursors.DictCursor)
    cur.execute(sql)
    db.commit()
    return cur.fetchall()

# closes the database connection when the game quits
def quit():
    db.close()
