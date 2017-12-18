#!/usr/bin/python

import fileinput
import os
import re
import rdflib
import rdflib.graph as g

##### Script to merge the rdf files into a single datastore.ttl file #####

#remove a previously existing datastore.ttl as not to get any duplicates
os.remove('datastore.ttl')

# list all the files in the directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

#filter for .nt and .ttl files using regex search:
regex = re.compile('.nt|.ttl')
selected_files = filter(regex.search, files)

##combined individual ttl and nt files into a single datastore.ttl file.
#writes out all .nt and .ttl files into single temp_datastore.ttl file (without parsing it)
f = open('temp_datastore.ttl', 'w')
f.write(''.join([line for line in fileinput.input(selected_files)]))
f.close()

#use the rdflib module to parse all the .ttl and .nt files to make a cleaner triple datastore file.
graph = g.ConjunctiveGraph()
graph.parse('temp_datastore.ttl', format='ttl')
output_datastore = graph.serialize(format='ttl')

#write out the datastore
f = open('datastore.ttl', 'w')
f.write(output_datastore)

#remove the temp file
os.remove('temp_datastore.ttl')
