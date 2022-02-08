
from unittest import result
from flask import Flask, render_template, redirect, request, url_for,Request
from flask_login import login_manager
from flask_bootstrap import Bootstrap
import random
from os import listdir
from os.path import isfile, join
import sqlite3
from sqlalchemy import create_engine, text
import json
from flask_sqlalchemy import SQLAlchemy

# TODO:
# -- build a DB scheme on paper
# -- add a user table DB
# -- add USER LOGIN with DB and login manager
# -- add a user panel HTML page to view diary

#  ------------------------ app configuration ------------------------
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# https://www.alittlesparkofjoy.com/tarot-cards-list/
# https://www.biddytarot.com/tarot-card-meanings/minor-arcana/suit-of-pentacles/king-of-pentacles/
# https://labyrinthos.co/blogs/tarot-card-meanings-list
user = {
    'email':'jayber1@gmail.com',
    'password':'123',
    'allowed': True,
}



# ----------------------- datebase handling -------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.INTEGER())

db.create_all()


@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        if email == user['email'] and user['password'] == password:    
            return redirect(url_for('user_interface',email=email,password=password))
        else:
            return redirect(url_for('login'))
    return render_template('index.html',)


@app.route('/user/<string:email>?<string:password>', methods=['GET','POST'])
def user_interface(email,password):
    cards = []

    # to generate a randon 4 items array from json data
    with open('data.json') as f:
        cards_from_json = json.load(f)
        
    for i in range(0, 5):
        index = random.randint(0, len(cards_from_json) -1)
        cards.append(cards_from_json[index]) 
        cards_from_json.pop(index)
    if request.method == 'POST':
        data = request.form.get('thoughts')
        print(data)
    print(len(cards))
    return render_template('user_interface.html', username=email, password=password, cards=cards)


if '__main__' == __name__:
    app.run(debug=True)