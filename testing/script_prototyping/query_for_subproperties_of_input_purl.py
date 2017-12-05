#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import re                   #to filter files using regex

########################################################################
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

# Put together a WHERE clause which will only query for subclasses+ of a given input class
def where_subclass_query_func(input_class):
    return 'WHERE {' + '?s rdfs:subPropertyOf+ <' + str(input_class) + '> . } \n'

#put together a sparql query string which will query for subclasses of a
#given input class
def subclass_query_function(input_class):
    function_list = [prefix_func(), select_func(['s'], 1), where_subclass_query_func(input_class)]
    return ''.join(function_list)

#call the function to query for the subclass of the in_arg
query_for_subclasses = subclass_query_function(in_arg)

########################################################################
# wrap the ontobee SPARQL end-point
endpoint = SPARQLWrapper("http://sparql.hegroup.org/sparql/")
# set the query string
endpoint.setQuery(query_for_subclasses)
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

#make new list of purls from results of query i.e. take only the values.
results_list = []
results_list += [res['s']['value'] for res in results["results"]["bindings"]]

#filter the results_list to only include ontobee purls using regex search
regex = re.compile('http://purl.obolibrary.org/obo/')
results_list = filter(regex.search, results_list)

#save the results to a file with the name of the input purl
namestring = str(sys.argv[1])
#remove the http://purl.obolibrary.org/obo/ from the input file.
namestring = re.sub('http://purl.obolibrary.org/obo/', '', namestring)
#make the file name to write to
outstring = 'subproperties_of_' + namestring + '.txt'

#write out to outfile: query_for_subclasses_of_out.txt
f = open(outstring, 'w')

#write each PURL fetched in query to outfile.
for r in results_list:
    f.write(r + '\n')

#old way of writing out results from their dict datastructure return from sparql query.
# for res in results["results"]["bindings"] :
#     f.write(res['s']['value'] + '\n')
