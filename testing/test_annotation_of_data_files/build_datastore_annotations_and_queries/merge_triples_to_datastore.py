#!/usr/bin/python

import fileinput
import os
import re
import rdflib
import rdflib.graph as g

##### Script to merge the rdf files into a single datastore.ttl file #####

#remove a previously existing datastore.ttl as not to get any duplicates
if os.path.isfile('datastore.ttl') == True :
    os.remove('datastore.ttl')

# list all the files in the directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

#filter for .ttl files using regex search:
regex = re.compile('[.]ttl')
selected_files = filter(regex.search, files)

#use the rdflib module to parse all the .ttl files to make a single datastore triple file datastore.ttl.
graph = g.ConjunctiveGraph()
[graph.parse(str(s), format='ttl') for s in selected_files]
output_datastore = graph.serialize(format='ttl')

#write out the datastore
f = open('datastore.ttl', 'w')
f.write(output_datastore)
