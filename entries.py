@app.route('/entries')
#Allows for entries to be seen#
def show_entries():
	cur=g.db.execute('Select word, helptext from entries order by id desc')
	entries=[dict(word=row[0], helptext=row[1]) for row in cur.fetchall()]
	return render_template("show_entries.html", entries-entries)
	