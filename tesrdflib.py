import rdflib
g=rdflib.Graph()
g.parse('Movie-RDF.ttl', format="ttl")

limit = 25
counter = 0
id = "http://localhost:3333/"

for s,p,o in g:
    if str(o) == "James Cameron":
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