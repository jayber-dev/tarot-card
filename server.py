
from flask import Flask, render_template, redirect, request, url_for,Request

app = Flask(__name__)

# https://www.alittlesparkofjoy.com/tarot-cards-list/

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        data = request.args
        print(data)
        return redirect(url_for('user_interface'))
    return render_template('index.html')

@app.route('/user')
def user_interface():
    return render_template('user_interface.html')
if '__main__' == __name__:
    app.run(debug=True)