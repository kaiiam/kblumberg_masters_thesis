#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON

import rdflib
import rdfextras
rdfextras.registerplugins() # so we can Graph.query()


# wrap the dbpedia SPARQL end-point
endpoint = SPARQLWrapper("http://dbpedia.org/sparql")

query_1 = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbpr: <http://dbpedia.org/resource/>
SELECT ?label
WHERE { dbpr:Asturias rdfs:label ?label }
"""

query_2 = """
PREFIX d: <http://dbpedia.org/ontology/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX crg: <http://dbpedia.org/resource/Category:>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?guitarist ?birthdate
WHERE {
?guitarist dcterms:subject crg:Canadian_rock_guitarists  .
?guitarist d:birthDate ?birthdate .
FILTER ( datatype(?birthdate) = xsd:date)
FILTER (xsd:date(?birthdate) >= "1970-01-01"^^xsd:date && xsd:date(?birthdate) <= "1990-01-01"^^xsd:date )
}
"""

# set the query string
endpoint.setQuery(query_2)


# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)

# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

##interpret the results:
# for res in results["results"]["bindings"] :
#    print res['label']['value']

# for res in results["results"]["bindings"] :
#    print res['guitarist']['value'], res['birthdate']['value']

# query within local file instead of http://dbpedia.org/resource?
import rdflib.graph as g

query_3 = """
PREFIX file: <file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/testing/test_basic.csv>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX ietf: <http://tools.ietf.org/html/>
SELECT ?s ?v
FROM <test_basic.nt>
WHERE
{
?label <http://www.w3.org/2000/01/rdf-schema#label> "Nitrate" .
?s ?label ?v
}
"""

#store = plugin.get('IOMemory', Store)()
#graph = g.Graph()
graph = rdflib.graph.ConjunctiveGraph()
graph.parse('test_basic.nt', format='ntriples')
# #print graph.serialize(format='pretty-xml')
# #print graph.serialize(format='ttl')
# print graph.serialize(format='ntriples')

results = graph.query(query_3)
# results is of <class 'rdflib.plugins.sparql.processor.SPARQLResult'>
# I need to convert this to JSON for the for loop to work
# for res in results["results"]["bindings"] :
#     print res['s']['value'], res['v']['value']
# or alternatively I don't need JSON format here and can just access via
#in a regular python way //todo but for now this is proof that the thing is working!

for row in results:
    print row





# #query the rdflib.graph.Graph()
# #filename = "path/to/fileneme" #replace with something interesting
# #uri = "uri_of_interest" #replace with something interesting
# uri = "http://tools.ietf.org/html/"
# g=rdflib.Graph()
# #g.parse(filename)
# graph.parse('test_basic.ttl', format='ttl')
# results = g.query("""
# SELECT ?p ?o
# WHERE {
# ?s ?p ?o.
# }
# ORDER BY (?p)
# """) #get every predicate and object about the uri
#
# results = endpoint.query().convert()
#
# # interpret the results:
# #for res in results["results"]["bindings"] :
# #    print res['label']['value']
