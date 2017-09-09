"""
App
----
"""
import sqlite3
from flask import Flask, g, request, session, abort
from contextlib import closing
from flask_jsglue import JSGlue

# config (which should be in another file for larger apps)
DATABASE = '/tmp/zeus.db'
"""SQLite database file. Schema can be found in schema.sql"""
DEBUG = True
"""For dev purposes."""
SECRET_KEY = 'aza manotany eh'

CSRF_ENABLED = True

app = Flask(__name__)

jsglue = JSGlue(app)

app.config.from_object(__name__)


# import other necessary modules
import pegasus.views
import pegasus.errorhandlers

def connect_db():
    """Connect to the SQLite database."""
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    """Initialize the SQLite database. Used in init_db.py."""
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()



# database requests
@app.before_request
def before_request():
    """Before database requests, connect, and turn on foreign keys."""
    g.db = connect_db()
    g.db.execute('PRAGMA foreign_keys = ON')

@app.before_request
def csrf_protect():
    if request.method == 'POST' and app.config['CSRF_ENABLED']: # GET/ajax protection can be defined in their respective functions
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(400) 

@app.teardown_request
def teardown_request(exception):
    """If there's a database connection, close it."""
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()



