import database

# this function updates the highscore of the current player
def update(name, score):
    # check if we should update our score
    scores = database.execute_query("SELECT * from scores WHERE name='{}'".format(name))
    updateScore = True

    if not len(scores):
        database.execute_query("INSERT INTO scores (name,score,wins,loses) VALUES ('{}','0','0','0')".format(name, 0, 0, 0))

    # loop through existing rows
    for x in scores:
        if x["score"] > score:
            updateScore = False

    # update score
    if updateScore:
        database.execute_query("UPDATE scores SET score='{}' WHERE name='{}'".format(score, name))

# this gets a value from the scores table
def get_value(col, name):
    scores = database.execute_query("SELECT * FROM scores WHERE name='{}'".format(name))

    for x in scores:
        return int(x[col])

    return 0

# this increments the amount of wins a player has
def increment_wins(name):
    wins = get_value("wins", name) + 1
    database.execute_query("UPDATE scores SET wins='{}' WHERE name='{}'".format(wins, name))

# this increments the amount of loses a player has
def increment_loses(name):
    loses = get_value("loses", name) + 1
    database.execute_query("UPDATE scores SET loses='{}' WHERE name='{}'".format(loses, name))
