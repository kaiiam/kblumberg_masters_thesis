#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON

import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import fileinput

##combined individual ttl and nt files into a single datastore.ttl file.
filenames = ['ice_algal_chlorophyll.ttl', 'ice_algal_chlorophyll.nt']

def triple_merge(filenames):
    f = open('datastore.ttl', 'w')
    f.write(''.join([line for line in fileinput.input(filenames)]))

#run this line to merge the rdf files into a single datastore.ttl file
#triple_merge(filenames)


#sparql queries:
#query against ontobee endpoint to get subclasses of sea ice.
# with open('query_for_subclasses.rq','r') as f_open:
#     query_for_subclasses = f_open.read()

with open('query_for_associated_data.rq','r') as f_open:
    query_for_associated_data = f_open.read()



########################################################################
# Put together a sparql query from pieces.

# Put together the PREFIX block:
def prefix_function():
    prefix_list = ['obo: <http://purl.obolibrary.org/obo/>', 'rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 'rdfs: <http://www.w3.org/2000/01/rdf-schema#>', 'owl: <http://www.w3.org/2002/07/owl#>']
    insert_prefix = ' \nPREFIX '
    return ('PREFIX ' + insert_prefix.join(prefix_list) + '\n' )
#print prefix_function()

# Put together the FROM block

def from_function():
    return 'FROM <datastore.ttl>\n'
#print from_function()

# Put together a select block
#takes the query and a bool for whether or not to add a distinct
#or just make two different ones because this will need to take as input
#the output variables from the where clause.

def select_function(variables, distinct):
    insert_p = ' ?'
    if distinct == 1:
        return ('SELECT DISTINCT ?' + insert_p.join(variables) + '\n' )
    else:
        return ('SELECT ?' + insert_p.join(variables) + '\n')
#print select_function( ['s', 'p', 'o'] , 1 )
#print select_function( ['o'] , 0 )

# Put together a WHERE clause
# A first attempt which will only query for subclasses of a given input class

def where_function(input_class):
    return 'WHERE {' + '?s rdfs:subClassOf+ <' + str(input_class) + '> . } \n'

#print where_function('http://purl.obolibrary.org/obo/ENVO_00002200')



#put together a sparql query string which will query for subclasses of a
#given input class
def subclass_query_function(input_class):
    i = input_class
    function_list = [prefix_function(), select_function(['s'], 1), where_function(i)]
    return ''.join(function_list)


query_for_subclasses = subclass_query_function('http://purl.obolibrary.org/obo/ENVO_00002200')

#query_for_subclasses = subclass_query_function('http://purl.obolibrary.org/obo/PCO_0000002')



# wrap the dbpedia SPARQL end-point
#endpoint = SPARQLWrapper("http://dbpedia.org/sparql")
#this one is the test ontobee endpoint and doesn't work for real queries
#endpoint = SPARQLWrapper("http://www.ontobee.org/sparql/")

endpoint = SPARQLWrapper("http://sparql.hegroup.org/sparql/")

# set the query string
endpoint.setQuery(query_for_subclasses)
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

#  make a list of the classes collected from the first query
str_list = []

for res in results["results"]["bindings"] :
   str_list.append(res['s']['value'])

# for r in str_list:
#     print r

# query within local file

#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()

graph.parse('datastore.ttl', format='ttl')


#print graph.serialize(format='ttl')

s = '>)(<'
query_for_associated_data = query_for_associated_data + '(<' + s.join(str_list) + '>)}}'

results = graph.query(query_for_associated_data)

# for row in results:
#     print "%s" % row

for row in results:
   print "%s | %s" % row

# for row in results:
#     print "%s | %s | %s" % row
