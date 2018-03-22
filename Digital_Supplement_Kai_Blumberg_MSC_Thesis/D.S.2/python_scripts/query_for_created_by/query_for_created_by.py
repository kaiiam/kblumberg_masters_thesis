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
# Put together a sparql query from pieces.

# Put together the PREFIX block:
def prefix_func():
    prefix_list = ['obo: <http://purl.obolibrary.org/obo/>', 'rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 'rdfs: <http://www.w3.org/2000/01/rdf-schema#>', 'owl: <http://www.w3.org/2002/07/owl#>', 'html: <http://tools.ietf.org/html/>']
    insert_prefix = ' \nPREFIX '
    return ('PREFIX ' + insert_prefix.join(prefix_list) + '\n' )

# Put together a select block
#takes the query and a bool for whether or not to add a distinct
def select_func():
    return ('SELECT (count(distinct ?s) as ?s)' + '\n' )


def from_func():
    return 'FROM <envoPolarttl.owl>\n'


# Put together a WHERE clause which will only query for subclasses+ of a given input class
def where_subclass_query_func():
    s = 'WHERE {'
    s += '?s rdf:type owl:Class . \n'
    s += 'FILTER regex(str(?s), "ENVO") .  \n'
    s += '?s <http://www.geneontology.org/formats/oboInOwl#created_by> ?term_editor. \n'
    s += ' } \n'
    return s

#put together a sparql query string which will query for subclasses of a
#given input class
def subclass_query_function():
    function_list = [prefix_func(), select_func(),from_func(), where_subclass_query_func()]
    return ''.join(function_list)

#call the function to query for the subclass of the in_arg
query_for_subclasses = subclass_query_function()

graph = g.ConjunctiveGraph()

graph.parse('envoPolarttl.owl', format='ttl')

results = graph.query(query_for_subclasses)

#save the results to a file with the name of the input purl
namestring = 'all_classes_with_created_by.txt'

#write out to outfile: query_for_subclasses_of_out.txt
f = open(namestring, 'w')
for row in results:
   f.write( "%s\n" % row)
