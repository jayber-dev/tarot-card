from flask import Flask, render_template, redirect, request, url_for,Request, flash
from flask_login import current_user, login_manager, LoginManager, login_required, login_user, UserMixin, logout_user, user_accessed
from flask_bootstrap import Bootstrap
import random
from os import listdir
from os.path import isfile, join
import json
import datetime as date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# ------------------------------------------------------------------------
# TODO: make a random card reverse ability
# TODO: make password hashing
# ------------------------ TO REMEMBER -----------------------------------
# TODO: check venv dir
# ------------------------------------------------------------------------



# print(date.datetime.now().date())
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "4589088fea88534aae93198759c57512161ed12c83abfe05197a9e772bbe8fdf"

db = SQLAlchemy(app)

# ------------------------ USER LOGIN DECLARATIONS --------------------------------------
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# ------------------------ CARDS DATA TO COPY -------------------------------------------

# https://www.alittlesparkofjoy.com/tarot-cards-list/
# https://www.biddytarot.com/tarot-card-meanings/minor-arcana/suit-of-pentacles/king-of-pentacles/
# https://labyrinthos.co/blogs/tarot-card-meanings-list

# /--------------------------- DATABASE DECLERATION ---------------------/

class User(db.Model,UserMixin ):
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
    card_path_1 = db.Column(db.String(500), unique=False, nullable=False)
    card_path_2 = db.Column(db.String(500), unique=False, nullable=False)
    card_path_3 = db.Column(db.String(500), unique=False, nullable=False)
    card_path_4 = db.Column(db.String(500), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

# db.create_all()

# db.session.add(user)
# db.session.commit()
# db.session.add(entry_post)
# db.session.commit()

# wow = User.query.filter_by(id=1).first()
# print(wow.id)
# entry = Diary.query.filter_by(user_id=wow.id).all()
# print(entry)

# /------------------------ LOGIN INTERFACE AND REGISTRATIN ------------------------/

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('pass')
            user_database = User.query.filter_by(email=email).first()
            if check_password_hash(user_database.password, password=password): 
                login_user(user_database)
                print(login_user)
                return redirect(url_for('user_interface'))
            else:
                flash('Incorrect password')
                return redirect(url_for('login'))
        except:
            if email == "":
                flash('Please enter an Email')
                return redirect(url_for('login'))
            else:
                flash('Incorrect email address')
                return redirect(url_for('login'))    
        
    return render_template('login.html',)

# /------------------------------- REGISTER HANDLER ----------------------------------/

@app.route("/register", methods=["GET","POST"])
def reg():
    print('im here')
    try :
        if request.method == "POST":
            data = request.form.to_dict()
            print(data)
            hashed_password = generate_password_hash(data['pass'],
                                                 method='pbkdf2:sha256',
                                                 salt_length=8)
            
            # /---------DATABASE COMMIT --------------/
            db_data = User(name=data['fname'],
                            email=data['email'],
                            sName=data['lname'],
                            country=data['country'],
                            password=hashed_password,
                            creation_date=date.datetime.now().date())
            db.session.add(db_data)
            db.session.commit()
            print(User.id)
        return redirect(url_for('login'))
    except:
        print("Exception raised no DB commit")
        flash("Email already exist's ")
        return redirect(url_for('login'))

# /------------------------------- CARDS REVEAL PAGE ---------------------------------/

@app.route('/', methods=['GET','POST'])
def user_interface():
    cards = []
    print(current_user)
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
        diary_commit = Diary(entry=data['text'],
                            date=date.datetime.now().date(),
                            card_path_1=data['card1'],
                            card_path_2=data['card2'],
                            card_path_3=data['card3'],
                            card_path_4=data['card4'],
                            user_id=current_user.id
                            )
        db.session.add(diary_commit)
        db.session.commit()
        


    
    return render_template('user_interface.html', cards=cards, is_active=current_user.is_active)

# /------------------------------ USER INTERFACE => DIARY INFORMATION -------------------------------/

@app.route("/user_panel", methods=['GET','POST'])
@login_required
def user_panel():
    data_passed_to_client = []
    if request.method == "POST":
        query_date = request.form.get('datequery')
        user_request = Diary.query.filter_by(user_id=current_user.id).all()
        for i in user_request:
            if i.date == query_date:
                data_to_append = {
                   'entry': i.entry,
                   'date': i.date,
                   'card1':i.card_path_1,
                   'card2':i.card_path_2,
                   'card3':i.card_path_3,
                    'card4':i.card_path_4,
               }
                data_passed_to_client.append(data_to_append)
                print(data_passed_to_client)
        return render_template('user_panel.html', entry=data_passed_to_client, is_active=current_user.is_active, is_found=True)
        
    return render_template('user_panel.html', is_active=current_user.is_active)


# /------------------------------- LOGOUT --------------------------------------/

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('user_interface'))


if '__main__' == __name__:
    app.run(debug=True)