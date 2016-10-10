#Had a bit of help from https://realpython.com/blog/python/python-web-applications-with-flask-part-ii/#
#uses flaskr Tutorial#
#Used this site for Flask responses as reference#
#http://rallion.bitbucket.org/explorations/flask_tutorial/api/flask.Response.html#
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv
    
	export FLASK_APP=flaskr
	export FLASK_DEBUG=1
	flask run

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'
def get_db():
	if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
    
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


 @app.route('/')
def show_entries():
#Shows entries#
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)
    

	g.b.execute('delete from entries where word=?', [request.form['entry_to_delete']])
	g.db.commit()
	flash('The entry was removed! HAHA!')
	return redirect(url_for('show_entries'))
	
if__name__'__main__':
	app.run()
       
