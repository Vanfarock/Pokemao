from peewee import *

db = SqliteDatabase("pokedex.db")

class BaseModel(Model):
	class Meta:
		database = db

class Types(BaseModel):
	name = CharField()

class Pokemon(BaseModel):
	name = CharField()
	number = CharField(primary_key = True)
	types = CharField()
