from SPARQLWrapper import SPARQLWrapper, JSON


def queryMovie(namaFilm):
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
            
            FILTER contains(?movieTitle,"Furious 7") .
            FILTER (lang(?comment) = 'en') .
            OPTIONAL {?movie rdfs:label ?movieTitle . 
            FILTER (lang(?movieTitle) = 'en') . 
            }
        }
        """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    # for result in results["results"]["bindings"]:
    #     print(result["label"]["value"])

    return(results)


queryMovie("Furious 7")
# for result in results["results"]["bindings"]:
#     print(result["label"]["value"])
