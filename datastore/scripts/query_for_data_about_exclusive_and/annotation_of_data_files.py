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

########################################################################
# read in file which was given as the first commandline argument
# the file should be a list of PURLS
in_file = open(str(sys.argv[1]), 'r')
#Create and clean a list of PURLS from the inputfile
in_args = []
in_args += [line.rstrip('\n') for line in in_file]

#The second argument is an additional class with which to constrain the search for data about, using a logical and statment.
in_arg2 = str(sys.argv[2])

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
    s += '	(group_concat(DISTINCT ?annotation; separator=", ") as ?annotation)\n'
    s += '	(group_concat(?x; separator=", ") as ?x)\n'
    return s

# Put together the FROM block
def from_func():
    return 'FROM <../../ice_datastore.ttl>\n'

# Put together a VALUES block to filter using a single variable/column
def values_filtering_func(input_list, in_var):
    s = '>)\n(<'
    return 'VALUES (?'+ str(in_var) +') { \n(<' + s.join(input_list) + '>) \n}\n'

# OR stament to access annotations of various property paths:
# starts from: rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:someValuesFrom
def query_property_path_func(in_var, out_var):
    s = '?' + in_var + ' (\n'
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
    s += '{ #get me some thing which is a data matrix \n'
    s += '?c rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:first obo:OBCS_0000120 ;  \n'
    s += '   rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:onProperty obo:IAO_0000136 ; \n'
    s += '} UNION { \n'
    s += '#get me a something (a column) which is part of some data matrix and is about some value \n'
    s += '?c rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:first/owl:onProperty obo:BFO_0000050 ; \n'
    s += '   rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:first/owl:someValuesFrom obo:OBCS_0000120 ; \n'
    s += '   rdf:type/owl:equivalentClass/owl:intersectionOf/rdf:rest/rdf:first/owl:onProperty obo:IAO_0000136 ; \n'
    s += '} \n'
    s += query_property_path_func('c','value') + '\n'
    s += values_filtering_func(in_args,'value') + '\n'
    s += query_property_path_func('c','annotation') + '\n'
    s += optional_block_func() + '\n'
    s += '} GROUP BY ?c \n'
    return s

#Put together a sparql query which will retrieve data from the datastore which
#has columns annotated with any PURLs given as input
def query_associated_data():
    f_list = [prefix_func(), select_func() , from_func(), where_query_associated_data_func() ]
    return''.join(f_list)

#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

graph.parse('../../ice_datastore.ttl', format='ttl')

results = graph.query(query_associated_data())

subj = []
obj = []
pred = []
for (c, annotation, x) in results:
    subj.append((unicodedata.normalize('NFKD', c.toPython()).encode('ascii','ignore')).split(', '))
    obj.append((unicodedata.normalize('NFKD', annotation.toPython()).encode('ascii','ignore')).split(', '))
    pred.append((unicodedata.normalize('NFKD', x.toPython()).encode('ascii','ignore')).split(', '))

#filter out non obo purls (blank nodes returned from the query)
fobj = []
for l in obj:
    l = [k for k in l if 'http://purl.obolibrary.org/obo/' in k]
    fobj.append(l)

#use a logical and to refine the output data to be only those colunns satisfying a logical AND between
#the list of input classes in the in_args with the AND class submitted as the in_arg2
return_indices = []
for idx, l in enumerate(fobj):
    for k in in_args:
        if (k in l) and (in_arg2 in l):
            #print idx, l
            return_indices.append(idx)

#print only the rows with satisty the AND statment.
for x in return_indices:
    print subj[x], fobj[x], pred[x]
