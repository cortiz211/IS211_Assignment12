import sqlite3 as lite
import sys

con = lite.connect('hwdb.db')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS students;")
    cur.execute("DROP TABLE IF EXISTS quizzes;")
    cur.execute("DROP TABLE IF EXISTS results;")

    cur.execute("CREATE TABLE students (s_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT);")
    cur.execute("CREATE TABLE quizzes (q_id INTEGER PRIMARY KEY, q_subject TEXT, num_questions INTEGER, q_date DATE);")
    cur.execute("CREATE TABLE results (r_id INTEGER, s_id INTEGER, q_id INTEGER, score INTEGER);")

    cur.execute("INSERT INTO students VALUES (1, 'John', 'Smith');")
    cur.execute("INSERT INTO quizzes (q_id, q_subject, num_questions, q_date) VALUES (1, 'Python Basics', 5, '2015-05-05');")
    cur.execute("INSERT INTO results (s_id, q_id, score) VALUES (1, 1, 85);")