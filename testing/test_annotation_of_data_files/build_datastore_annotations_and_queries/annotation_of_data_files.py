#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON

import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()

with open('query_annotation_of_data_files_working.rq','r') as f_open:
    query_1 = f_open.read()

#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

#graph.parse('global_chlorophyll_a.ttl', format='ttl')

graph.parse('datastore.ttl', format='ttl')

results = graph.query(query_1)

# for row in results:
#     print "%s" % row

# for row in results:
#     print "%s | %s" % row

for row in results:
    print "%s | %s | %s" % row
