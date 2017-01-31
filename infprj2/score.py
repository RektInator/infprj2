import database

# this function updates the highscore of the current player
def update(name, score):
    # check if we should update our score
    scores = database.execute_query("SELECT * from scores WHERE name='{}'".format(name))
    updateScore = True

    # loop through existing rows
    for x in scores:
        if x["score"] > score:
            updateScore = False

    # update score
    if updateScore:
        database.execute_query("REPLACE INTO scores (score,name) VALUES ('{}','{}')".format(score, name))
