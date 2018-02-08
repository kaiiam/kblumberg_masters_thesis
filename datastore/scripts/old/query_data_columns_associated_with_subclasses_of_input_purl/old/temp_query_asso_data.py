#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys


import fileinput
########################################################################

query = open('temp_fixed.rq', 'r')



#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()
graph.parse('datastore.ttl', format='ttl')
#print graph.serialize(format='ttl')

results = graph.query(query)

for row in results:
   print "%s | %s" % row
