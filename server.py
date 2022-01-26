
from flask import Flask, render_template, redirect, request, url_for,Request
from flask_login import login_manager
import random
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('c:/Users/evgenyber/Desktop/development studies/my-projects/tarot-cards/static/TarotCards') 
if isfile(join('c:/Users/evgenyber/Desktop/development studies/my-projects/tarot-cards/static/TarotCards', f))]


card = random.choices(onlyfiles, k=4)
print(card)
app = Flask(__name__)

# https://www.alittlesparkofjoy.com/tarot-cards-list/

user = {
    'email':'jayber1@gmail.com',
    'password':'123',
}

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        if email == user['email'] and user['password'] == password:
            
            return redirect(url_for('user_interface',email=email,password=password))
    return render_template('index.html')

@app.route('/user/<string:email>?<string:password>')
def user_interface(email,password):
    return render_template('user_interface.html', username=email, password=password)
if '__main__' == __name__:
    app.run(debug=True)