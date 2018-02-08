#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import re                   #to filter files using regex

########################################################################
### script to query for classes which are 'part of' a given input class or to which the input class 'has part'
# example run: ./query_for_parts_associated_with_input_class.py http://purl.obolibrary.org/obo/ENVO_00001998

# import from sys
#could later use this to accept a list of input classes to query
#in_args = sys.argv[1:]


in_arg = sys.argv[1]

########################################################################
# Put together a sparql query from pieces.

# Put together the PREFIX block:
def prefix_func():
    prefix_list = ['obo: <http://purl.obolibrary.org/obo/>', 'rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 'rdfs: <http://www.w3.org/2000/01/rdf-schema#>', 'owl: <http://www.w3.org/2002/07/owl#>', 'html: <http://tools.ietf.org/html/>']
    insert_prefix = ' \nPREFIX '
    return ('PREFIX ' + insert_prefix.join(prefix_list) + '\n' )

# Put together a select block
#takes the query and a bool for whether or not to add a distinct
def select_func(variables, distinct):
    insert_p = ' ?'
    if distinct == 1:
        return ('SELECT DISTINCT ?' + insert_p.join(variables) + '\n' )
    else:
        return ('SELECT ?' + insert_p.join(variables) + '\n')

# Put together a WHERE clause which will query for classes which are 'part of' or 'has part' the input term
def where_query_input_for_parts_func(input_class):
    s = 'WHERE {\n<' + str(input_class) + '> rdf:type owl:Class ;\n'
    s += '   rdfs:subClassOf ?s .\n'
    s += '?s owl:onProperty ?p ;\n'
    s += '   (owl:someValuesFrom) | (owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first) ?v\n'
    s += 'VALUES (?p) {\n'
    s += '(<http://purl.obolibrary.org/obo/BFO_0000051>)\n'
    s += '(<http://purl.obolibrary.org/obo/BFO_0000050>)\n'
    s += '}\n'
    s += '}\n'
    return s

# Put together a WHERE clause which will query for 'part of' or 'has part' some input term
def where_query_parts_of_input_func(input_class):
    s = 'WHERE {\n'
    s += '?s rdf:type owl:Class ;\n'
    s += '   rdfs:subClassOf ?subs.\n'
    s += '?subs (owl:someValuesFrom) | (owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first) <' + str(input_class) +'> ;\n'
    s += '   owl:onProperty ?p . \n'
    s += 'VALUES (?p) {\n'
    s += '(<http://purl.obolibrary.org/obo/BFO_0000051>)\n'
    s += '(<http://purl.obolibrary.org/obo/BFO_0000050>)\n'
    s += '}\n'
    s += '}\n'
    return s

#put together a sparql query string which will query for subclasses of a
#given input class
def query_input_for_parts_function(input_class):
    function_list = [prefix_func(), select_func(['v'], 1), where_query_input_for_parts_func(input_class)]
    return ''.join(function_list)

#print query_input_for_parts_function(in_arg)

def query_for_parts_of_input_function(input_class):
    function_list = [prefix_func(), select_func(['s'], 1), where_query_parts_of_input_func(input_class)]
    return ''.join(function_list)

########################################################################
# wrap the ontobee SPARQL end-point
endpoint = SPARQLWrapper("http://sparql.hegroup.org/sparql/")
# set the query string for the first query
endpoint.setQuery(query_input_for_parts_function(in_arg))
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results1 = endpoint.query().convert()
# set the query string for the second query
endpoint.setQuery(query_for_parts_of_input_function(in_arg))
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results2 = endpoint.query().convert()

#save the results to a file with the name of the input purl
namestring = str(sys.argv[1])
#remove the http://purl.obolibrary.org/obo/ from the input file.
namestring = re.sub('http://purl.obolibrary.org/obo/', '', namestring)
namestring = re.sub('http://purl.unep.org/sdg/', '', namestring)
#make the file name to write to
outstring = 'parts_associated_with_' + namestring + '.txt'

#make new list of purls from results of query i.e. take only the values.
results_list = []
results_list += [res['v']['value'] for res in results1["results"]["bindings"]]
results_list += [res['s']['value'] for res in results2["results"]["bindings"]]

#filter the results_list to only include ontobee purls using regex search
regex = re.compile('http://purl.obolibrary.org/obo/')
results_list = filter(regex.search, results_list)

#write out to outfile:
f = open(outstring, 'w')

#write each PURL fetched in query to outfile.
for r in results_list:
    f.write(r + '\n')
