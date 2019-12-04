import rdflib
g=rdflib.Graph()
g.parse('Movie-RDF.ttl', format="ttl")

# dbpedia=rdflib.Graph()
# dbpedia.load('http://dbpedia.org/resource/Film')

limit = 25
counter = 0
search = "Robert Downey Jr"
searchdbp = search.replace(" ", "_")

for s,p,o in g:
    if search in str(o):
        counter+=1
        print(g.value(s, rdflib.term.URIRef(u'http://localhost:3333/hasTitle'), None))
        print(s, p, o)        

    if counter >= limit:
        break

# for s,p,o in dbpedia:
#     if searchdbp in str(s):
#         counter+=1
#         print(s, p, o)

#     if counter >= limit:
#         break
