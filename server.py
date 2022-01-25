from flask import Flask, render_template, redirect, request, url_for,Request

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('index.html')

if '__main__' == __name__:
    app.run(debug=True)