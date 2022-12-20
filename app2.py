from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def user(name):
	return render_template("index.html",n=name)

@app.route("/")
def home():
	return render_template("index.html",names=["charanu","mj0ln1r"])

if __name__ == '__main__':
	app.run()
