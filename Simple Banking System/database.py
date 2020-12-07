import sqlite3

CREATE_TABLE_CARD = "CREATE TABLE IF NOT EXISTS card(id INTEGER PRIMARY KEY, number TEXT, pin TEXT, balance INTEGER DEFAULT 0);"
INSERT_CARD = "INSERT INTO card(number, pin) VALUES(?, ?);"
DELETE_CARD = "DELETE FROM card WHERE number = ?;"
ADD_BALANCE = "UPDATE card SET BALANCE=? WHERE number=?"
SHOW_BALANCE = "SELECT balance FROM card WHERE number=?;"
LOG_IN = "SELECT number, pin FROM card WHERE number=? AND pin=?;"
FIND_CARD = "SELECT number, balance FROM card where number=?;"


def connect():
    return sqlite3.connect("card.s3db")


def create_table(conn):
    with conn:
        conn.execute(CREATE_TABLE_CARD)


def insert_card(conn, number, pin):
    with conn:
        conn.execute(INSERT_CARD, (number, pin))


def delete_card(conn, number):
    with conn:
        conn.execute(DELETE_CARD, (number,))


def add_balance(conn,balance, number):
    with conn:
        conn.execute(ADD_BALANCE, (balance, number))


def log_in_db(conn, number, pin):
    with conn:
        return conn.execute(LOG_IN, (number, pin)).fetchone()


def show_balance(conn, number):
    with conn:
        return conn.execute(SHOW_BALANCE, (number,)).fetchone()


def find_card(conn, number):
    with conn:
        return conn.execute(FIND_CARD, (number,)).fetchone()
