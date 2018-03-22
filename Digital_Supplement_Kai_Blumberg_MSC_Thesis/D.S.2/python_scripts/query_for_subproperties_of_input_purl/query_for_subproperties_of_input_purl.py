#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import re                   #to filter files using regex

########################################################################

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
def where_subproperty_query_func(input_class):
    return 'WHERE {' + '?s rdfs:subPropertyOf+ <' + str(input_class) + '> . } \n'

#Put together a where clause which searches for the inverse of an input class
def where_inverse_of_query_func(input_class):
    return 'WHERE {' + '?s owl:inverseOf <' + str(input_class) + '> . } \n'

#put together a sparql query string which will query for subclasses of a
#given input class
def subproperty_query_function(input_class):
    function_list = [prefix_func(), select_func(['s'], 1), where_subproperty_query_func(input_class)]
    return ''.join(function_list)

def inverse_of_query_func(input_class):
    function_list = [prefix_func(), select_func(['s'], 1), where_inverse_of_query_func(input_class)]
    return ''.join(function_list)

########################################################################
# wrap the ontobee SPARQL end-point
endpoint = SPARQLWrapper("http://sparql.hegroup.org/sparql/")

#call the function to query for the class which is the inverse of the input class
query_for_inverse_of = inverse_of_query_func(in_arg)

# set the query string to query for the query_for_inverse_of
endpoint.setQuery(query_for_inverse_of)
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
inverse_of_results = endpoint.query().convert()
#get the result from the query as inverse_of_in_arg
inverse_list = []
inverse_list += [res['s']['value'] for res in inverse_of_results["results"]["bindings"]]

#make new list of purls from results of query i.e. take only the values.
results_list = []

#if we have an inverse query for it's subproperties
if len(inverse_list)>=1:
    #get the PURL which is the inverse of the input PURL
    inverse_of_in_arg = inverse_list[0]
    #call the function to query for the subclass of the inverse of the input class
    query_for_subproperty = subproperty_query_function(inverse_of_in_arg)
    # set the query string to query_for_subproperty
    endpoint.setQuery(query_for_subproperty)
    # select the return format (e.g. XML, JSON etc...)
    endpoint.setReturnFormat(JSON)
    # execute the query and convert into Python objects
    # Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
    inverse_results = endpoint.query().convert()
    #put the subproperties of the inverse property into the list of results
    results_list += [res['s']['value'] for res in inverse_results["results"]["bindings"]]

#call the function to query for the subclass of the input class
query_for_subproperty = subproperty_query_function(in_arg)
# set the query string to query_for_subproperty
endpoint.setQuery(query_for_subproperty)
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()
#append the subproperties_of the original input to the list of purls.
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

#write out to outfile:
f = open(outstring, 'w')

#write each PURL fetched in query to outfile.
for r in results_list:
    f.write(r + '\n')
