#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON

import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()


with open('test_query_for_equivlance_class_about.rq','r') as f_open:
    query_1 = f_open.read()

with open('test_query_for_input_equivalence_class_about.rq','r') as f_open:
    query_2 = f_open.read()

with open('column_query_annotated.rq','r') as f_open:
    query_3 = f_open.read()




#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

#graph.parse('global_chlorophyll_a.nt', format='ntriples')
#graph.parse('global_chlorophyll_a.ttl', format='ttl')



graph.parse('datastore.ttl', format='ttl')

#print graph.serialize(format='ttl')

#print query_3

results = graph.query(query_3)

# for row in results:
#     print "%s" % row

    # for row in results:
    #     print "%s | %s" % row

for row in results:
    print "%s | %s | %s" % row
