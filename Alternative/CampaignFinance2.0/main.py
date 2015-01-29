'''
Main Python Controller for web page.

What we have and will use:
    index() to generate the index.html template and main.
What we have and don't use (but will):
    Database connectors to sqlite for development purposes.
What we don't have:
    I have no idea, binge coding.
'''
import sqlite3
from flask import Flask, render_template, g

DATABASE = './schema.sql'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
APP = Flask(__name__)
APP.config.from_object(__name__)

def connect_db():
    '''
    Database connector, useless right now.
    '''
    return sqlite3.connect(APP.config['DATABASE'])

@APP.before_request
def before_request():
    '''
    Instructions to execute before a user establishes full connection
    with the website.
    '''
    g.db = connect_db()

@APP.teardown_request
def teardown_request(exception):
    '''
    Instructions to execute after a user leaves the website.
    '''
    print exception
    g.db.close()

@APP.route('/')
@APP.route('/index')
def index():
    '''
    Function returns the index.html file.
    TODO: Add code to update data sets and send the information
          as an argument to render_template().
          Implement jinja in index.html first.
    '''
    return render_template('index.html')

if __name__ == '__main__':
    APP.run(host="10.0.1.12")
