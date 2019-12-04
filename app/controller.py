from app import app
import rdflib
import re
from flask import render_template

# variables
limit = 25
g=rdflib.Graph()
g.parse('Movie-RDF.ttl', format="ttl")
style = '''
        <style>
        table {
        font-family: arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        }

        td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
        }

        tr:nth-child(even) {
        background-color: #dddddd;
        }
        </style>
        '''

def searchLocal(searchKey):
    counter = 0
    out = '''
    <table>
        <tr>
            <th>Movie Id</th>
            <th>Movie Actor</th>
            <th>Movie Title</th>
            <th>Link</th>
        </tr>
    '''
    print("MASUK")
    for s,p,o in g:
        if re.search(searchKey, str(o), re.IGNORECASE):
            counter+=1
            title = g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasTitle'), None)
            actors = [None] * 3
            i = 0
            for actor in g.objects(s,rdflib.term.URIRef(u'http://localhost:3333/hasActor')):
                actors[i] = actor
                i+=1
            out += '''
            <tr>
                <td>'''+s+'''</td>
                <td>'''+actors[0]+''', '''+actors[1]+''', '''+actors[2]+'''</td>
                <td>'''+title+'''</td>
                <td>
                    <form action="/detail" method="post">
                        <button type="submit" name="id" value="'''+s+'''">'''+title+'''</button>
                    </form>
                </td>
                
            </tr>
            '''
        if counter >= limit:
            break

    out += '''</table>'''
    return out

def getAttrById(s):
    title = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasTitle'), None)
    actor = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasActor'), None)
    aspectRatio = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasAspectRatio'), None)
    budget = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasBudget'), None)
    duration = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasDuration'), None)
    genres = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasGenres'), None)
    gross = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasGross'), None)
    imdbLink = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasIMDBLink'), None)
    imdbScore = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasIMDBScore'), None)
    lang = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasLanguage'), None)
    origin = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasOrigin'), None)
    plot = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasPlot'), None)
    rating = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasRating'), None)
    year = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/madeInYear'), None)
    votedBy = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/votedBy'), None)
    return render_template('details.html', title='Details', judul=title, actor=actor, aspectRatio=aspectRatio, budget=budget, duration=duration, genres=genres, gross=gross, imdbLink=imdbLink, imdbScore=imdbScore, lang=lang, origin=origin, plot=plot, rating=rating, year=year, votedBy=votedBy)

