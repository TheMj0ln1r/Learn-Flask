from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/user")
def user():
	return render_template("user3.html")

@app.route("/")
def home():
	return render_template("index3.html")

if __name__ == '__main__':
	app.run(debug=True)
