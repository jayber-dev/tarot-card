from flask import Flask, render_template, redirect, request, url_for,Request, flash
from flask_login import login_manager
from flask_bootstrap import Bootstrap
import random
from os import listdir
from os.path import isfile, join
import json
import datetime as date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

# ------------------------------------------------------------------------
# TODO: make a registration form 
# TODO: make a user panel to show the diary by dates and by cards
# TODO: make login interafce look good
# TODO: add description to each card and make it into a popup
# ------------------------------------------------------------------------



# print(date.datetime.now().date())
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "4589088fea88534aae93198759c57512161ed12c83abfe05197a9e772bbe8fdf"

db = SQLAlchemy(app)

# login_manager.init_app(app)
# login_manager = LoginManager()

# https://www.alittlesparkofjoy.com/tarot-cards-list/
# https://www.biddytarot.com/tarot-card-meanings/minor-arcana/suit-of-pentacles/king-of-pentacles/
# https://labyrinthos.co/blogs/tarot-card-meanings-list

# user_data = {
#     'email':'jayber1@gmail.com',
#     'password':'123',
#     'allowed': True,
# }

# /--------------------------- DATABASE DECLERATION ---------------------/

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    sName = db.Column(db.String(80), unique=False, nullable=False)
    country = db.Column(db.String(80), unique=False, nullable=False)
    creation_date = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    entrys = db.relationship('Diary', backref='user', lazy=True)

class Diary(db.Model):
    __tablename__ = "diary"
    id = db.Column(db.Integer, primary_key=True)
    entry = db.Column(db.Text(500), unique=False, nullable=False)
    date = db.Column(db.String(50), unique=False, nullable=False)
    card_path = db.Column(db.String(500), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

# db.create_all()

# user = User(name="jay",
#             email="jayber1@gmail.com",
#             sName='ber', country='israel',
#             creation_date=date.datetime.now().date(),
#             password='123'
#             )

# entry_post = Diary(entry='wow its the best\n i could never imagine\n',
#             date=date.datetime.now().date(),
#             user_id = 1
#             )

# db.session.add(user)
# db.session.commit()
# db.session.add(entry_post)
# db.session.commit()


# wow = User.query.filter_by(id=1).first()
# print(wow.id)
# entry = Diary.query.filter_by(user_id=wow.id).all()
# print(entry)

# for i in entry:
#     print(i.entry)

# /------------------------ LOGIN INTERFACE AND REGISTRATIN ------------------------/

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('pass')
        try:
            user_database = User.query.filter_by(email=email).first()
            if password == user_database.password:      
                return redirect(url_for('user_interface'))
            else:
                flash('incorrect password')
                return redirect(url_for('login'))
        except:
            if email == "":
                flash('empty email field')
                return redirect(url_for('login'))
            else:
                flash('incorrect email address')
                return redirect(url_for('login'))    
            
    return render_template('login.html',)

# /------------------------------- REGISTER HANDLER ----------------------------------/

@app.route("/register", methods=["GET","POST"])
def reg():
    print('im here')
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        reg_fname = request.form.get('fname')
        reg_lname = request.form.get('lname')
        reg_email =request.form.get('email')
        reg_pass = request.form.get('pass')
        reg_country = request.form.get('country')
        # /---------DATABASE COMMIT --------------/
        db_data = User(name=reg_fname,
                        email=reg_email,
                        sName=reg_lname,
                        country=reg_country,
                        password=reg_pass,
                        creation_date=date.datetime.now().date())
        db.session.add(db_data)
        # db.session.commit()
        print(User)
    return redirect(url_for('login'))


# /------------------------------- CARDS REVEAL PAGE ---------------------------------/

@app.route('/user_interface', methods=['GET','POST'])
def user_interface():
    cards = []

    # generate a randon 5 items array from json data
    with open('data.json') as f:
        cards_from_json = json.load(f)
        
    for i in range(0, 5):
        index = random.randint(0, len(cards_from_json) -1)
        cards.append(cards_from_json[index]) 
        cards_from_json.pop(index)

    if request.method == 'POST':
        print('inside the post method')
        data = request.get_json(force=True)
        print(data)
        print(f"{data['card']}\n")
        print(data['text'])

    
    return render_template('user_interface.html', cards=cards)

# /------------------------------ USER INTERFACE DIARY INFORMATION -------------------------------/

@app.route("/user_panel")
def user_panel():
    user_entrys = User.query.filter_by(id="1").first()
    print(user_entrys.name)
    return render_template('user_panel.html', name=user_entrys.name)


if '__main__' == __name__:
    app.run(debug=True)