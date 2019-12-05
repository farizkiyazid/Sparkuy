from app import app
from SPARQLWrapper import SPARQLWrapper, JSON
import json
import rdflib
import re
from flask import render_template
# from query import queryMovie 
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
                <td>'''+actors[0]+'''; '''+actors[1]+'''; '''+actors[2]+'''</td>
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
    return render_template('details.html', title='Details', director=director, judul=title, actor=actors, aspectRatio=aspectRatio, budget=budget, duration=duration, genres=genres, gross=gross, imdbLink=imdbLink, imdbScore=imdbScore, lang=lang, origin=origin, plot=plot, rating=rating, year=year, votedBy=votedBy)



def queryMovie(searchKey):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX res: <http://dbpedia.org/resource/>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?movie ?movieTitle ?thumbnail ?comment
        WHERE {
            ?movie rdf:type dbo:Film .
            ?movie foaf:name ?movieTitle .
            ?movie dbo:thumbnail ?thumbnail .
            ?movie rdfs:comment ?comment
            
            FILTER contains(?movieTitle, "%s") .
            FILTER (lang(?comment) = 'en') .
            OPTIONAL {?movie rdfs:label ?movieTitle . 
            FILTER (lang(?movieTitle) = 'en') . 
            }
        }
        """ % searchKey)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    thumbnail = ""
    comment = ""
    for result in results["results"]["bindings"]:
        # thumbnail =  ' '.join(result["thumbnail"]["value"])
        # comment   =  ' '.join(result["comment"]["value"])
        print(thumbnail)
        print("LALALALALALALALALALALALALALALALA")
        print(comment)

    
    return(thumbnail, comment)