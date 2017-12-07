#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import fileinput

### Script to query for all classes which participate in subclasses of a given process ###

########################################################################
# read in the first commandline argument file which should be a list of
# PURLS which are subclasses of a given term
subclasses_input = open(str(sys.argv[1]), 'r')
#Create and clean a list of PURLS from the inputfile
subclasses_list = []
subclasses_list += [line.rstrip('\n') for line in subclasses_input]

# read in the second commandline argument file which should be a list of
# PURLS which are subproperties of RO: participates in
subproperties_input = open(str(sys.argv[2]), 'r')
#Create and clean a list of PURLS from the inputfile
subproperty_list = []
subproperty_list += [line.rstrip('\n') for line in subproperties_input]

# for r in subproperty_list:
#     print r

########################################################################
#sparql query assembly:

# get temp sparql query for testing purposes:
with open('test_1.rq','r') as f_open:
    query = f_open.read()

########################################################################
# wrap the ontobee SPARQL end-point
endpoint = SPARQLWrapper("http://sparql.hegroup.org/sparql/")
# set the query string
endpoint.setQuery(query)
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

for res in results["results"]["bindings"] :
    print res['input_purl']['value'], res['property']['value'], res['value']['value']

# #old code to print results to terminal
# for row in results:
#    print "%s | %s | %s" % row
