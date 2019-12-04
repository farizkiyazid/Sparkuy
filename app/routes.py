from app import app
from flask import render_template, request
import rdflib

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kiki'}
    return render_template('index.html', title='Home', user=user)

@app.route('/search', methods=['POST'])
def handle_data():
    searchKey = request.form['searchKey']

    g=rdflib.Graph()
    g.parse('Movie-RDF.ttl', format="ttl")
    limit = 25
    counter = 0
    out = ""

    for s,p,o in g:
        if searchKey in str(o):
            counter+=1
            out += "Movie Id : " + s + "; Movie Actor : "  + o + "; Movie Title : " + g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasTitle'), None) + "<br>"
        if counter >= limit:
            break

    return out
