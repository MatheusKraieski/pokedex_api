from flask.globals import request
from flask import Flask, render_template
import requests
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

class User(db.model):
    __tablename__ = "users"
    id = Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    emial = db.Column(db.String, unique=True)

    def __repr__(self):
        return "<User %r>" % self.usarname

class Pokemon:
    def __init__(self,nome,foto, tipo1, tipo2, golpes):
        self.nome=nome
        self.foto=foto
        self.tipo1=tipo1
        self.tipo2=tipo2
        self.golpes=golpes



@app.route("/")
def index():
    return render_template('index.html') 



@app.route("/buscar", methods = ["GET", "post"])
def buscar():
    pokemon = Pokemon(request.form["nome"].lower() ,"","","","")
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)
        result = res.get("sprites").get("other").get("official-artwork")
        result = result["front_default"]
        pokemon.foto = result
        pokemon.golpes = []
        for i in range(0, len(res.get("moves"))):
            pokemon.golpes.append(res.get("moves")[i].get("move").get("name"))

        if len(res["types"])==2:
            pokemon.tipo1 = res.get("types")[0].get("type").get("name")
            pokemon.tipo1 = res.get("types")[0].get("type").get("name")
        else:
            pokemon.tipo1 = res.get("types")[0].get("type").get("name")   
    except:
        return "pokemon não encontrado"
    return render_template("index.html", 
    nome = pokemon.nome,
    foto = pokemon.foto,
    tipo1 = pokemon.tipo1,
    tipo2 = pokemon.tipo2,
    golpes = pokemon.golpes

    )


if __name__=="__main__":
    app.run(debug=True)