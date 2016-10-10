@app.route('/delete', methods=['POST'])
#deletes unwanted post#
def delete_entry():
	g.b.execute('delete from entries where word=?', [request.form['entry_to_delete']])
	g.db.commit()
	flash('The entry was removed! HAHA!')
	return redirect(url_for('show_entries'))
	
if__name__'__main__':
	app.run()