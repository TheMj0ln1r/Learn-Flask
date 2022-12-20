from flask import Flask, redirect, url_for, render_template, request,session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "mj0ln1r"
app.permanent_session_lifetime = timedelta(minutes=5)
@app.route("/user")
def user():	
	if "user" in session:
		usr = session["user"]
		return render_template("user6.html",u=usr)
	else:
		return redirect(url_for("home"))
@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		session.permanent = True
		user = request.form['nm']
		session["user"] = user
		flash("You are logged in ","info")
		return redirect(url_for("user"))
	else:
		if "user" in session:
			flash("Already logged in!","info")
			return redirect(url_for("user"))
		return render_template("index6.html")
@app.route("/logout")
def logout():
	session.pop("user",None)
	flash("You have been logged out!","info")
	return redirect(url_for("login"))
@app.route("/")
def home():
	return "<b>Enter /login in url to login</b>"

if __name__ == '__main__':
	app.run(debug=True)
