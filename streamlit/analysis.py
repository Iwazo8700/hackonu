import streamlit as st
import sqlite3
DB_PATH = "db/{}"
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn


conn = create_connection(DB_PATH.format("database.sqlite3"))
cur = conn.cursor()
reports = cur.execute("SELECT report_content FROM report").fetchall()
print(reports)
