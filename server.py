from flask import Flask, render_template, redirect, request, url_for,Request
from flask_login import login_manager
import random
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir('C:/Users/gey/Desktop/development studies/myOwnProjects/tarot-card-main/static/TarotCards') 
if isfile(join('C:/Users/gey/Desktop/development studies/myOwnProjects/tarot-card-main/static/TarotCards', f))]



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
    card = random.choices(onlyfiles, k=4)
    print(card)
    return render_template('user_interface.html', username=email, password=password, cards=card)
if '__main__' == __name__:
    app.run(debug=True)