from flask import Flask, redirect, url_for, render_template, request,session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "mj0ln1r"
app.permanent_session_lifetime = timedelta(minutes=5)
@app.route("/user")
def user():	
	if "user" in session:
		usr = session["user"]
		return f"<h1>Hello {usr}</h1>"
	else:
		return redirect(url_for("home"))
@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form['nm']
		session["user"] = user
		return redirect(url_for("user"))
	else:
		if "user" in session:
			return redirect(url_for("user"))
		return render_template("index4.html")
@app.route("/logout")
def logout():
	if "user" in session:
		session.pop("user",None)
		return redirect(url_for("home"))
	else:
		return redirect(url_for("home"))
@app.route("/")
def home():
	return "<b>Enter /login in url to login</b>"

if __name__ == '__main__':
	app.run(debug=True)
