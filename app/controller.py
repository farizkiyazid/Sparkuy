from app import app, query
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

        ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #333;
        }

        li {
            float: left;
        }

        li a {
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }

        li a:hover {
            background-color: #111;
        }
        </style>
        '''

def searchLocal(searchKey):
    counter = 0
    flag = None
    out = '''
    <table>
        <tr>
            <th>Movie Id</th>
            <th>Movie Actor</th>
            <th>Movie Title</th>
            <th>Link</th>
        </tr>
    '''
    for s,p,o in g:
        # if re.search(str(s), out, re.IGNORECASE):
        #     continue
        if str(s) not in out and re.search(searchKey, str(o), re.IGNORECASE):
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
                <td>'''+actors[0]+'''; '''+actors[1]+'''; '''+actors[2]+'''</td>
                <td>'''+title+'''</td>
                <td>
                    <form action="/detail" method="post">
                        <button type="submit" name="id" value="'''+s+'''">'''+title+'''</button>
                    </form>
                </td>
                
            </tr>
            '''
        flag = str(s)
        if counter >= limit:
            break

    out += '''</table>'''
    return out

def getAttrById(s):
    # get attributes from local
    title = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/hasTitle'), None)
    director = g.value(rdflib.term.URIRef(s), rdflib.term.URIRef(u'http://localhost:3333/directedBy'), None)
    actors = [None] * 3
    i = 0
    for actor in g.objects(rdflib.term.URIRef(s),rdflib.term.URIRef(u'http://localhost:3333/hasActor')):
        actors[i] = actor
        i+=1
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

    # get attributes from dbpedia
    thumbnail, comment = query.queryMovie(str(title)[0:-1])
    return render_template('details.html', title='Details', thumbnail=thumbnail, director=director, judul=title, actor=actors, comment=comment, aspectRatio=aspectRatio, budget=budget, duration=duration, genres=genres, gross=gross, imdbLink=imdbLink, imdbScore=imdbScore, lang=lang, origin=origin, plot=plot, rating=rating, year=year, votedBy=votedBy)

