@app.route("/search" , methods=['POST'])
#Searches for words in the app from posts. Definitely looked up what fetchall #
#Definition: https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-fetchall.html#
#The method fetches all (or all remaining) rows of a query result set and returns a#
# list of tuples. If no more rows are available, it returns an empty list.#


def search entries():
	word=request.form['searchterm']
	cur = g.db.execute('select helptext from entries where word - ?' , 
			[word])
	result= [dict(word=row[0], helptext=row[1]) for row in cur.fetchall()]
	return render_template("show-entries.html", entries-entries)
	