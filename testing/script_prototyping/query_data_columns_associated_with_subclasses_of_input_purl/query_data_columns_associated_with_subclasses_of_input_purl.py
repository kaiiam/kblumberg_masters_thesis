#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import fileinput
import re                   #to filter files using regex

### Script to query a datastore for data with columns about a input list of PURLS ###

########################################################################
# read in file which was given as the first commandline argument
# the file should be a list of PURLS
in_file = open(str(sys.argv[1]), 'r')

#Create and clean a list of PURLS from the inputfile
in_args = []
in_args += [line.rstrip('\n') for line in in_file]

########################################################################
# Put together a sparql query from pieces.

# Put together the PREFIX block:
def prefix_func():
    prefix_list = ['obo: <http://purl.obolibrary.org/obo/>', 'rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 'rdfs: <http://www.w3.org/2000/01/rdf-schema#>', 'owl: <http://www.w3.org/2002/07/owl#>', 'html: <http://tools.ietf.org/html/>']
    insert_prefix = ' \nPREFIX '
    return ('PREFIX ' + insert_prefix.join(prefix_list) + '\n' )

# Put together the FROM block
def from_func():
    return 'FROM <datastore.ttl>\n'

# Put together a select block
#takes the query and a bool for whether or not to add a distinct
def select_func(variables, distinct):
    insert_p = ' ?'
    if distinct == 1:
        return ('SELECT DISTINCT ?' + insert_p.join(variables) + '\n' )
    else:
        return ('SELECT ?' + insert_p.join(variables) + '\n')

# Put together a VALUES block to filter using a single variable/column
def values_filtering_func(input_list):
    s = '>)(<'
    return 'VALUES (?filter) { (<' + s.join(input_list) + '>) }\n'

# Put together a WHERE clause which will only be used to query_associated_data
# using the values_filtering_func which takes in an input PURL list
def where_query_associated_data_func():
    s = 'WHERE {\n'
    s += '?s rdf:type obo:OBCS_0000120 ; \n'
    s += 'html:rfc4180row ?DataItemRows .\n'
    s += '?DataItemRows ?p ?filter ; \n'
    s += '?c ?o . \n'
    s += 'filter (?c != rdf:type && ?o != html:rfc4180Row) \n'
    s += 'filter (?c != html:rfc4180rowPosition) \n'
    s += 'filter (?c != ?p) \n'
    s += values_filtering_func(in_args) + '}'
    return s

#Put together a sparql query which will retrieve data from the datastore which
#has columns annotated with any PURLs given as input
def query_associated_data():
    f_list = [prefix_func(), select_func(['c', 'o'], 0) , from_func(), where_query_associated_data_func() ]
    return''.join(f_list)

# query within local file
#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()
graph.parse('datastore.ttl', format='ttl')

results = graph.query(query_associated_data())

#old code to print results to terminal
# for row in results:
#    print "%s | %s" % row

#save the results to a file with the name of the input purl
namestring = str(sys.argv[1])
#remove the subclasses_of_ from the input file name.
namestring = re.sub('subclasses_of_', '', namestring)
#remove the .txt from the input file name.
namestring = re.sub('.txt', '', namestring)
#make the file name to write to
outstring = 'data_columns_associated_with_subclasses_of_' + namestring + '.csv'

#create output csv file
f = open(outstring, 'w')
#print data to output csv file
for row in results:
   f.write( "%s,%s\n" % row)
