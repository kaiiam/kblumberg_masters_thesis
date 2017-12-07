#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON

import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()

#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

#graph.parse('test_basic.nt', format='ntriples')
graph.parse('envo_rdf.owl', format='ttl')

#print graph.serialize(format='ttl')
# #print graph.serialize(format='pretty-xml')

#print graph.serialize(format='ntriples')


f = open('envo_owl.nt', 'w')
f.write(graph.serialize(format='ntriples'))
