from flask import Flask, render_template, session, redirect, request 
import random
app = Flask(__name__)
app.secret_key = "secretKeyChippers"

@app.route('/')
def index():
	answer = " "
	if "winNum" not in session:
		session["winNum"] = random.randrange(1,101)
	if 'user_input' not in session:
		answer = " "
	else:
		if int(session["winNum"]) < int(session['user_input']):
			answer = "Too Big!"
		if int(session["winNum"]) > int(session["user_input"]):
			answer = "Too Small!!"
		if int(session["winNum"]) == int(session["user_input"]):
			answer = "You WIN!!!!"

	return render_template('index.html', answer=answer)

@app.route('/guess', methods=["POST"])
def guess():
	session['user_input'] = request.form['user_input']
	return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
	session.clear()
	return redirect('/')
app.run(debug=True)

