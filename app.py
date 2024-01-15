from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello () :
    return "Hello IRT3"

@app.route('/addition')
def Addition () :
    return "valeur1 + valeur2"

@app.route('/sustraction')
def Soustraction () :
    return "valeur1 - valeur 2"

app.run(port=5000)