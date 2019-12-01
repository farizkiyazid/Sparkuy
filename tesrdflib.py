import rdflib
g=rdflib.Graph()
g.parse('Movie-RDF.ttl', format="ttl")

dbpedia=rdflib.Graph()
dbpedia.load('http://dbpedia.org/resource/Film')

limit = 25
counter = 0
search = "Robert Downey Jr"
searchdbp = search.replace(" ", "_")
print(searchdbp)

for s,p,o in g:
    if search in str(o):
        counter+=1
        print(s, p, o)

    if counter >= limit:
        break

for s,p,o in dbpedia:
    if searchdbp in str(s):
        counter+=1
        print(s, p, o)

    if counter >= limit:
        break

# for s,p,o in g:
#     counter+=1
#     if p == "hasTitle":
#         print(s, " ", p, " ", o)

#     if counter >= limit:
#         break
# import rdflib

# g = rdflib.Graph()
# result = g.parse("http://www.w3.org/People/Berners-Lee/card")

# print("graph has %s statements." % len(g))
# # prints graph has 79 statements.

# for subj, pred, obj in g:
#    if (subj, pred, obj) not in g:
#        raise Exception("It better be!")

# s = g.serialize(format='n3')