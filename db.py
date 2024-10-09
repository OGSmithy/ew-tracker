import sqlite3
from flask import Flask, render_template, request, redirect

class Database:
    def __init__(self, url):
        with sqlite3.connect(url) as db:
            cursor = db.cursor()
            sql = """
            CREATE TABLE IF NOT EXISTS ew (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                subject TEXT NOT NULL,
                beak TEXT NOT NULL,
                date DATE NOT NULL
            );
            """
            cursor.execute(sql)

            sql_insert = """
            INSERT INTO ew (task, subject, beak, date) VALUES (?, ?, ?, ?);
            """
            cursor.execute(sql_insert, ('Database','Compsci','MC','2000-24-00'))
            db.commit()


    def get_ews(self):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            sql = """
            SELECT id, task, subject, beak, date FROM ew
            """
            cursor.execute(sql)

            return cursor.fetchall()
        
        

    def create_ew(self,task,subject,beak,date):
        
        #task = request.form['task']
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            sql = """
            INSERT INTO ew (task, subject, beak, date)
            VALUES (?, ?, ?, ?)
            """
            return cursor.execute(sql, (task, subject, beak, date))
        
        



    # EXTRA CREDIT
    def get_ew(self, id):
        """
        TO IMPLEMENT
        """
        pass