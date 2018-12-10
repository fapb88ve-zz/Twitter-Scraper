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
        CREATE TABLE IF NOT EXISTS user_info (
        user_name TEXT NOT NULL,
        num_follower INTEGER NOT NULL,
        num_status INTEGER NOT NULL
        );
        """
        sql2 = """
        CREATE TABLE IF NOT EXISTS tweets_status (
        user_name TEXT NOT NULL,
        created_at DATE NOT NULL,
        status_id INTEGER NOT NULL,
        favorite_count INTEGER NOT NULL,
        retweet_count INTEGER NOT NULL,
        message_count INTEGER NOT NULL,
        status_text TEXT NOT NULL,
        FOREIGN KEY (user_name) REFERENCES user_info (user_name)

        );
        """
        try:
            c = self.connection
            for command in [sql1,sql2]:
                c.execute(command)
        except Error as e:
            print(e)

    def table_updater(self, table_name, data):
        if table_name == "user_info":
            sql = """
            INSERT INTO user_info
            VALUES (?,?,?)
            """
        else:
            sql = """
            INSERT INTO user_info (user_name, created_at, status_id,
                                    favorite_count, retweet_count, message_count,
                                    status_text)
            VALUES (?,?,?,?,?,?,?)

            """

        try:
            c = self.connection
            c.execute(sql, data)
            c.commit()
        except Error as e:
            print(e)

if __name__ == "__main__":
    a = SQLite("test.db")

    #print(a.table_creator())

    a.table_updater("user_info", ['PoleoRafael', 698859, 47362])
