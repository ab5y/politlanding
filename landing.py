from flask import Flask, request, session, g, redirect, url_for, \
				abort, render_template, flash

# Configuation
USERNAME = 'admin'
PASSWORD = 'default'
# DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def show_landing():
	print 'Reaches here'
	return render_template('show_landing.html')

@app.route('/contact_us', methods=['POST', 'GET'])
def contact_us():
	if request.method == 'POST':
		pass
	return render_template('contact_us.html')

# @app.route('/add_email', methods=['POST'])
# def add_email():
# 	email = request.form['email']
# 	flash('Your email was successfully stolen by the corporate machinery: '+email)
# 	return redirect(url_for('show_landing'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	error = None
# 	if request.method == 'POST':
# 		if request.form['username'] != app.config['USERNAME']:
# 			error = 'Invalid username'
# 		elif request.form['password'] != app.config['PASSWORD']:
# 			error = 'Invalid password'
# 		else:
# 			session['logged_in'] = True
# 			flash('You were logged in')
# 			return redirect(url_for('show_landing'))
# 	return render_template('login.html', error=error)

# @app.route('/logout')
# def logout():
# 	session.pop('logged_in', None)
# 	flash('You were logged out')
# 	return redirect(url_for('show_landing'))

if __name__ == '__main__':
	app.run()