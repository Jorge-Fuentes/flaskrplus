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
    
@app.route("/search" , methods=['POST'])
#Searches for words in the app from posts. Definitely looked up what fetchall #
#Definition: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html#
#The method fetches all (or all remaining) rows of a query result set and returns a#
# list of tuples. If no more rows are available, it returns an empty list.#


def search entries():
#Searches term#
	word=request.form['searchterm']
	cur = g.db.execute('select helptext from entries where word - ?' , 
			[word])
	result= [dict(word=row[0], helptext=row[1]) for row in cur.fetchall()]
	return render_template("show-entries.html", entries-entries)
	
@app.route('/entries')
#Allows for entries to be seen#
def show_entries():
	cur=g.db.execute('Select word, helptext from entries order by id desc')
	entries=[dict(word=row[0], helptext=row[1]) for row in cur.fetchall()]
	return render_template("show_entries.html", entries-entries)
	
@app.route('/add', methods=['POST'])
#The “?” is a safe why for sqlite3 to accept text#
#Add a category with the posts#
def addentry():
	g.db.execute ('insert into entries [word, helptext] values (?, ?)'
					[request.form['word'], request.form['helptext']])
	g.db.commit()
	flash('The new entry was successfully posted!')
	return redirect(url_for('show_entries'))
@app.route('/delete', methods=['POST'])
#deletes unwanted post#
def delete_entry():
	g.b.execute('delete from entries where word=?', [request.form['entry_to_delete']])
	g.db.commit()
	flash('The entry was removed! HAHA!')
	return redirect(url_for('show_entries'))
	
if__name__'__main__':
	app.run()
       
