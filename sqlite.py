import sqlite3
from sqlite3 import Error

class SQLite():

    def __init__(self, db_name):
        try:
            conn = sqlite3.connect(db_name)
            self.connection = conn
        except Error as e:
            print(e)

    def table_creator(self):

        sql1 = """
        CREATE TABLE IF NOT EXIST user_info (
        id integer PRIMARY KEY,
        user_name text NOT NULL,
        num_tweets integer NOT NULL,
        num_status integer NOT NULL
        );
        """

        sql2 = """
        CREATE TABLE IF NOT EXIST tweets_status (
        id integer PRIMARY KEY,
        user_name text NOT NULL,
        created_at date NOT NULL,
        status_id integer NOT NULL,
        favorite_count integer NOT NULL,
        retweet_count integer NOT NULL,
        message_count integer NOT NULL,
        status_text text NOT NULL
        );
        """
        try:
            c = self.connection
            for command in [sql1,sql2]:
                c.execute(command)
        except Error as e:
            print(e)
