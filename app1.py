from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
	return "<h1>Hello Flask this is <u>Mj0ln1r</u></h1>"

@app.route("/<name>")
def user(name):
	return "Hi "+name

@app.route("/test<par>")
def test(par):
	return "This is parameter "+par

@app.route("/admin")
def admin():
	return redirect(url_for("user",name="Admin!!"))


if __name__ == '__main__':
	app.run()