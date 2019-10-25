from flask import Flask, request, render_template, redirect, url_for, send_from_directory, jsonify
from playhouse.shortcuts import model_to_dict, dict_to_model
from werkzeug.utils import secure_filename
import peewee
from models import Types, Pokemon, db
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "C:\\Users\\vinic\\Desktop\\Pokemao\\static\\images"

@app.route("/")
def index():
	all_pokemons = Pokemon.select().dicts().get()
	pokemons_json = jsonify(model_to_dict(all_pokemons))
	return render_template("index.html", pokemons=pokemons_json)

@app.route("/add_pokemon", methods=["GET", "POST"])
def add_pokemon():
	name = request.form["name"]
	number = request.form["number"]
	types = request.form["types"]
	
	poke = Pokemon.create(name = name, number = number, types = types)

	if request.method == "POST":
		image = request.files["image"]
		print(image.filename)
		image.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(image.filename)))
		print("File Uploaded")

	print("Name: " + name + " Number: " + number + " Types: " + types + "Filename: " + image.filename)

	return redirect("/")

if __name__ == "__main__":
	try:
		db.connect()
		db.create_tables([Pokemon])
		# db.drop_tables([Pokemon])
	except peewee.OperationalError as e:
		print("Error " + str(e))

	app.run(debug = True, port = 5000)