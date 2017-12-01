#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON

import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()

#sparql queries:
#query against ontobee endpoint to get subclasses of sea ice.
with open('query_for_subclasses.rq','r') as f_open:
    query_for_subclasses = f_open.read()
#an intermediate query to be able to retrieve data based on having the term
#multiyear ice
# with open('query_2.rq','r') as f_open:
#     query_2 = f_open.read()
#query contains most of the code from query_2 but missing the values
#section which will be populated from the results of query_1
with open('query_for_associated_data.rq','r') as f_open:
    query_for_associated_data = f_open.read()

# wrap the dbpedia SPARQL end-point
#endpoint = SPARQLWrapper("http://dbpedia.org/sparql")
#this one is the test ontobee endpoint and doesn't work for real queries
#endpoint = SPARQLWrapper("http://www.ontobee.org/sparql/")

endpoint = SPARQLWrapper("http://sparql.hegroup.org/sparql/")

# set the query string
endpoint.setQuery(query_for_subclasses)
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

#  make a list of the classes collected from the first query
str_list = []

for res in results["results"]["bindings"] :
   str_list.append(res['s']['value'])

# query within local file

#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

graph.parse('ice_algal_chlorophyll.nt', format='ntriples')
graph.parse('ice_algal_chlorophyll.ttl', format='ttl')

graph.parse('first_year_ice.nt', format='nt')
graph.parse('smog_data.nt', format='nt')


#print graph.serialize(format='ttl')

#query_3 = query_3 + '(<http://purl.obolibrary.org/obo/ENVO_03000073>)}}'

s = '>)(<'
#print s.join(str_list)
query_for_associated_data = query_for_associated_data + '(<' + s.join(str_list) + '>)}}'
#print query_3

results = graph.query(query_for_associated_data)

# for row in results:
#     print "%s" % row

for row in results:
    print "%s | %s" % row

# for row in results:
#     print "%s | %s | %s" % row
