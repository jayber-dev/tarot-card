
from flask import Flask, render_template, redirect, request, url_for,Request
from flask_login import login_manager
app = Flask(__name__)

# https://www.alittlesparkofjoy.com/tarot-cards-list/

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form.get('email')
        print(data)
        return redirect(url_for('user_interface',email=data))
    return render_template('index.html')

@app.route('/user/<string:email>')
def user_interface(email):
    return render_template('user_interface.html', username=email)
if '__main__' == __name__:
    app.run(debug=True)