from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/add_pokemon")
def add_pokemon():
	name = request.args.get("name")
	number = request.args.get("number")
	image = request.args.get("image")
	print(name)
	print(number)
	print(image)
	return redirect("/")

app.run(debug = True, port = 5000)
