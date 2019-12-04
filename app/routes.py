from app import app
from flask import render_template, request
import rdflib
import re

g=rdflib.Graph()
g.parse('Movie-RDF.ttl', format="ttl")

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kiki'}
    return render_template('index.html', title='Home', user=user)

@app.route('/search', methods=['POST'])
def handle_data():
    searchKey = request.form['searchKey']

    limit = 25
    counter = 0
    out = ""

    for s,p,o in g:
        if re.search(searchKey, str(o), re.IGNORECASE):
            counter+=1
            title = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasTitle'), None)
            actor = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasActor'), None)
            aspectRatio = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasAspectRatio'), None)
            budget = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasBudget'), None)
            duration = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasDuration'), None)
            genres = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasGenres'), None)
            gross = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasGross'), None)
            imdbLink = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasIMDBLink'), None)
            imdbScore = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasIMDBScore'), None)
            lang = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasLanguage'), None)
            origin = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasOrigin'), None)
            plot = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasPlot'), None)
            Rating = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasRating'), None)
            year = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/madeInYear'), None)
            votedBy = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/votedBy'), None)

            out += "Movie Id : " + s + "; Movie Actor : "  + actor + "; Movie Title : " + title + "<br>"
        if counter >= limit:
            break

    return "test"
