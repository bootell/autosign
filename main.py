#imports
import sqlite3
from flask import Flask, request, session, url_for, redirect, render_template
from contextlib import closing

#configuration
DATABASE =  '/tmp/autosign.db'
DEBUG = True
USERNAME = 'admin'
PASSWORD = 'admin'

app = Flask(__name__)
app.config.from_object(__name__)

# database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode = 'r') as f:
            db.cursor().executescript(f.read())
        do.commit()

@app.before_request
def before_request():
    #check login
    if  'username' in session or request.path == '/login' or request.path == '/static/sign.css':
        pass
    else:
        return redirect(url_for('login'))

#main page
@app.route('/')
def index():
    return redirect(url_for('dashboard'))

#login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return 'wrong'
    else:
        return render_template('login.html')

#logout page
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

#dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

app.secret_key = 'autosign-by-bootell'
if __name__ == '__main__':
    app.debug = DEBUG
    app.run()