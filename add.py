@app.route('/add', methods=['POST'])
#The “?” is a safe why for sqlite3 to accept text#
#Add a category with the posts#
def addentry():
	g.db.execute ('insert into entries [word, helptext] values (?, ?)'
					[request.form['word'], request.form['helptext']])
	g.db.commit()
	flash('The new entry was successfully posted!')
	return redirect(url_for('show_entries'))