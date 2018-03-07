#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import fileinput
import re                   #to filter files using regex
import unicodedata #to convert literals to strings
#import logging  #to avoid any "No handlers" warning
########################################################################
#to avoid any "No handlers" warning
#logging.basicConfig()
#logger = logging.getLogger('my-logger')
#logger.propagate = False

# read in file which was given as the first commandline argument
# the file should be a list of PURLS
in_file = open(str(sys.argv[1]), 'r')

#Create and clean a list of PURLS from the inputfile
in_args = []
in_args += [line.rstrip('\n') for line in in_file]

#second infile list of GO terms
in_file2 = open(str(sys.argv[2]), 'r')

#Create and clean a list of PURLS from the inputfile
in_args2 = []
in_args2 += [line.rstrip('\n') for line in in_file2]

########################################################################
# Put together a sparql query from pieces.

# Put together the PREFIX block:
def prefix_func():
    prefix_list = ['obo: <http://purl.obolibrary.org/obo/>', 'rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 'rdfs: <http://www.w3.org/2000/01/rdf-schema#>', 'owl: <http://www.w3.org/2002/07/owl#>', 'html: <http://tools.ietf.org/html/>']
    insert_prefix = ' \nPREFIX '
    return ('PREFIX ' + insert_prefix.join(prefix_list) + '\n' )

# Put together a select block
#takes the query and a bool for whether or not to add a distinct
def select_func():
    s = 'SELECT DISTINCT ?c \n'
    s += '	(group_concat(DISTINCT ?value; separator=", ") as ?value)\n'
    s += '	?column\n'
    s += '	(group_concat(?x; separator=", ") as ?x)\n'
    return s

# Put together the FROM block
def from_func():
    return 'FROM <../../go_datastore.ttl>\n'

# Put together a VALUES block to filter using a single variable/column
def values_filtering_func(input_list, in_var):
    s = '>)\n(<'
    return 'VALUES (?'+ str(in_var) +') { \n(<' + s.join(input_list) + '>) \n}\n'

# OR stament to access annotations of various property paths:
# starts from: rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom
def query_property_path_func(out_var):
    s = ' (\n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:unionOf/rdf:rest*/rdf:first) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:first/owl:unionOf/rdf:rest*/rdf:first) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:unionOf/rdf:rest*/rdf:first) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:intersectionOf/rdf:rest*/rdf:first/owl:onClass/owl:intersectionOf/rdf:rest*/rdf:first) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:intersectionOf/rdf:rest*/rdf:first/owl:onClass/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first) | \n'
    s += '(rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:intersectionOf/rdf:rest*/rdf:first/owl:onClass/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first/owl:someValuesFrom) \n'
    s += ') ?' + out_var + '.\n'
    return s

def optional_block_func():
    s = 'OPTIONAL {\n'
    s += '?row a ns1:rfc4180Row ;\n'
    s += '  ?c ?x .\n'
    s += '}.\n'
    return s

# Put together a WHERE clause which will only be used to query_associated_data
# using the values_filtering_func which takes in an input PURL list
def where_query_associated_data_func():
    s = 'WHERE {\n'
    s += '?c rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:first obo:OBCS_0000120 ;  \n'
    s += '   rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:onProperty obo:IAO_0000136 ; \n'
    s += query_property_path_func('value')
    s += values_filtering_func(in_args,'value') + '\n'
    s += '#give me the columns of the data matrix\n'
    s += '?column rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:first/owl:onProperty obo:BFO_0000050 ;\n'
    s += '   rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:first/owl:someValuesFrom obo:OBCS_0000120 ;\n'
    s += '   rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:onProperty obo:IAO_0000136 .\n'
    s += '?c obo:BFO_0000051 ?column .\n'
    s += '?row a ns1:rfc4180Row ;\n'
    s += '  ?column ?x .\n'
    s += values_filtering_func(in_args2,'x')
    s += '} GROUP BY ?column \n'
    return s


#Put together a sparql query which will retrieve data from the datastore which
#has columns annotated with any PURLs given as input
def query_associated_data():
    f_list = [prefix_func(), select_func() , from_func(), where_query_associated_data_func() ]
    return''.join(f_list)

#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

graph.parse('../../go_datastore.ttl', format='ttl')

results = graph.query(query_associated_data())

# function to parse the query return object
# unicodedata.normalize is to convert from literals to strings to feed back into a values block.
column = []
for (subj, term, pred, obj) in results:
    column.append(unicodedata.normalize('NFKD', pred.toPython()).encode('ascii','ignore'))

###############################################################
##assemble the second query to fetch the row data

def select_row_func():
    s = 'SELECT ?column \n'
    s += '	(group_concat(DISTINCT ?value; separator=",") as ?value)\n'
    return s

def where_query_row_data_func():
    s = 'WHERE {\n'
    s += '?row a ns1:rfc4180Row ;\n'
    s += '   ?cols ?x .\n'
    s += values_filtering_func(column,'cols') + '\n'
    s += values_filtering_func(in_args2,'x') + '\n'
    s += '?row ?column ?value.\n'
    s += 'FILTER(?value != <http://tools.ietf.org/html/rfc4180Row>)\n'
    s += 'FILTER(?column != <http://tools.ietf.org/html/rfc4180rowPosition>)\n'
    s += '} GROUP BY ?column \n'
    return s

##second query to retrieve the specific GO terms of interest
## including the other data in their rows
def query_row_data():
    f_list = [prefix_func(), select_row_func() , from_func(), where_query_row_data_func() ]
    return''.join(f_list)

results2 = graph.query(query_row_data())

# for row in results2:
#    print "%s,%s" % row

outstring = 'test_output.csv'
f = open(outstring, 'w')
for row in results2:
    f.write ("%s,%s\n" % row)