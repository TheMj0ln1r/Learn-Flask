from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/<name>")
def user(name):	
	return f"<h1>Hello {name}</h1>"

@app.route("/login",methods=["POST","GET"])
def login():
	if request.method == "POST":
		user = request.form['nm']
		return redirect(url_for("user",name=user))
	else:
		return render_template("index4.html")

@app.route("/")
def home():
	return "<b>Enter /login in url to login</b>"

if __name__ == '__main__':
	app.run(debug=True)
