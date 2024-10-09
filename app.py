from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)
db = Database('database.db')


@app.route('/')
def list_ews():
    ews = db.get_ews()
    
    return render_template("list.html", rows=ews)

@app.route('/add', methods=['POST'])
def add_ew():
    task = request.form["task"]
    subject = request.form["subject"]
    beak = request.form["beak"]
    date = request.form["date"]
    db.create_ew(task, subject, beak, date)
    return redirect('/')


# EXTRA CREDIT
@app.route('/<int:id>')
def view_ew(id):
    """
    TO IMPLEMENT
    """
    pass