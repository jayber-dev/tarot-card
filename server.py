from flask import Flask, render_template, redirect, request, url_for,Request
from flask_login import login_manager
import random
from os import listdir
from os.path import isfile, join
import json


app = Flask(__name__)

# https://www.alittlesparkofjoy.com/tarot-cards-list/
# https://www.biddytarot.com/tarot-card-meanings/minor-arcana/suit-of-pentacles/king-of-pentacles/
# https://labyrinthos.co/blogs/tarot-card-meanings-list
user = {
    'email':'jayber1@gmail.com',
    'password':'123',
    'allowed': True,
}


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


@app.route('/user/<string:email>?<string:password>')
def user_interface(email,password):
    cards = []

    # to generate a randon 4 items array from json data
    with open('data.json') as f:
        cards_from_json = json.load(f)
        
    for i in range(0, 5):
        index = random.randint(0, len(cards_from_json) -1)
        cards.append(cards_from_json[index]) 
        cards_from_json.pop(index)
    
    print(len(cards))
    return render_template('user_interface.html', username=email, password=password, cards=cards)


if '__main__' == __name__:
    app.run(debug=True)