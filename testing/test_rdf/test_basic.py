#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON

import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()

#sparql queries:

with open('query_1.rq','r') as f_open:
    query_1 = f_open.read()




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

graph.parse('global_chlorophyll_a.nt', format='ntriples')
graph.parse('global_chlorophyll_a.ttl', format='ttl')

print graph.serialize(format='ttl')


#results = graph.query(query_1)

# for row in results:
#     print "%s" % row

#for row in results:
#    print "%s | %s" % row

# for row in results:
#     print "%s | %s | %s" % row
