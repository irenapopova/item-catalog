#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
import psycopg2
# import random
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect(host = "127.0.0.1",
                            port = "6432",
                            user="postgres",
                            password="password123",
                            database="tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute("delete from matches")
    cursor.execute("update player_standings set wins=0,matches=0")
    db_connection.commit()
    db_connection.close()
    
def deletePlayers():
    """Remove all the player records from the database."""
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute("delete from player")
    cursor.execute("delete from player_standings")
    db_connection.commit()
    db_connection.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db_connection = connect()
    cursor = db_connection.cursor()
    cursor.execute("select count(*) from player")
    data = cursor.fetchone()
    db_connection.close()
    return data[0]

def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.
    (Thisshould be handled by your SQL database schema, not in your Python code.)
    Args:
    name: the player's full name (need not be unique).
    """
    db_connection = connect()
    cursor = db_connection.cursor()
    try:
        # since wins and matches are part of functional paramaeter
        # here we are populating with random numbers
        cursor.execute("INSERT INTO player(name) VALUES (%s);",(name,))
        cursor.execute("INSERT INTO player_standings(name,wins,matches) VALUES(%s,%s,%s);",(name,0,0))
    except Exception as error:
        print(error)
    db_connection.commit()
    cursor.close()
    db_connection.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
    A list of tuples, each of which contains (id, name, wins, matches):
    id: the player's unique id (assigned by the database)
    name: the player's full name (as registered)
    wins: the number of matches the player has wonp
    matches: the number of matches the player has played
    """
    db_connection = connect()
    db_cursor = db_connection.cursor()
    query = "SELECT id,name,wins,matches FROM player_standings"
    db_cursor.execute(query)
    standings = db_cursor.fetchall()
    db_connection.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
    winner:  the id number of the player who won
    loser:  the id number of the player who lost
    """
    db_connection = connect()
    db_cursor = db_connection.cursor()
    query = "INSERT INTO matches (winner, loser) values (%s, %s);"
    db_cursor.execute(query, (int(winner), int(loser)))
    # update our matches and wins
    db_cursor.execute("update player_standings set wins=wins+1,matches=matches+1 where id=%s",(winner,))
    db_cursor.execute("update player_standings set matches=matches+1 where id=%s",(loser,))
    db_connection.commit()
    db_connection.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
        Assuming that there are an even number of players registered, each player
        appears exactly once in the pairings.  Each player is paired with another
        player with an equal or nearly-equal win record, that is, a player adjacent
        to him or her in the standings.

        Returns:
        A list of tuples, each of which contains (id1, name1, id2, name2)
            id1: the first player's unique id
            name1: the first player's name
            id2: the second player's unique id
            name2: the second player's name
        """
    db = connect()
    db_cursor = db.cursor()
    query = "SELECT id, name FROM player_standings order by wins desc"
    db_cursor.execute(query)
    standings = db_cursor.fetchall()
    number_of_pairs = len(standings)/2
    pairings = []
    for _ in range(number_of_pairs):
        p1 = standings.pop(0)
        p2 = standings.pop(0)
        pairings.append((p1[0], p1[1], p2[0], p2[1]))
    db.commit()
    db.close()
    return pairings

