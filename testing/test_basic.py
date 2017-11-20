#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON

import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()

#sparql queries:
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
}"""

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
}"""

with open('test_basic_2.rq','r') as f_open:
    query_4 = f_open.read()

with open('test_basic_3.rq','r') as f_open:
    query_5 = f_open.read()



# # wrap the dbpedia SPARQL end-point
# endpoint = SPARQLWrapper("http://dbpedia.org/sparql")
# # set the query string
# endpoint.setQuery(query_2)
# # select the return format (e.g. XML, JSON etc...)
# endpoint.setReturnFormat(JSON)
# # execute the query and convert into Python objects
# # Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
# results = endpoint.query().convert()

##interpret the results for dbpedia query in JSON format:
# for res in results["results"]["bindings"] :
#    print res['label']['value']

# for res in results["results"]["bindings"] :
#    print res['guitarist']['value'], res['birthdate']['value']

# query within local file instead of http://dbpedia.org/resource?

#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

#graph.parse('test_basic.nt', format='ntriples')
graph.parse('test_basic.ttl', format='ttl')

graph.parse('test_basic_supplemental_3.ttl', format='ttl')



# #print graph.serialize(format='pretty-xml')
# #print graph.serialize(format='ntriples')

print graph.serialize(format='ttl')


results = graph.query(query_5)

# for row in results:
#     print "%s" % row

for row in results:
    print "%s | %s" % row

# for row in results:
#     print "%s | %s | %s" % row
