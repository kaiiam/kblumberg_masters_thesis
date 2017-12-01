#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import fileinput

########################################################################
##combined individual ttl and nt files into a single datastore.ttl file.
filenames = ['ice_algal_chlorophyll.ttl', 'ice_algal_chlorophyll.nt', 'smog_data.nt', 'first_year_ice.nt']

def triple_merge(filenames):
    f = open('datastore.ttl', 'w')
    f.write(''.join([line for line in fileinput.input(filenames)]))

#run this line to merge the rdf files into a single datastore.ttl file
#triple_merge(filenames)

########################################################################
# Put together a sparql query from pieces.

# Put together the PREFIX block:
def prefix_func():
    prefix_list = ['obo: <http://purl.obolibrary.org/obo/>', 'rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 'rdfs: <http://www.w3.org/2000/01/rdf-schema#>', 'owl: <http://www.w3.org/2002/07/owl#>', 'html: <http://tools.ietf.org/html/>']
    insert_prefix = ' \nPREFIX '
    return ('PREFIX ' + insert_prefix.join(prefix_list) + '\n' )
#print prefix_func()

# Put together the FROM block
def from_func():
    return 'FROM <datastore.ttl>\n'
#print from_function()

# Put together a select block
#takes the query and a bool for whether or not to add a distinct
#or just make two different ones because this will need to take as input
#the output variables from the where clause.
def select_func(variables, distinct):
    insert_p = ' ?'
    if distinct == 1:
        return ('SELECT DISTINCT ?' + insert_p.join(variables) + '\n' )
    else:
        return ('SELECT ?' + insert_p.join(variables) + '\n')
#print select_func( ['s', 'p', 'o'] , 1 )
#print select_func( ['o'] , 0 )

# Put together a WHERE clause
# A first attempt which will only query for subclasses of a given input class
def where_subclass_query_func(input_class):
    return 'WHERE {' + '?s rdfs:subClassOf+ <' + str(input_class) + '> . } \n'

#put together a sparql query string which will query for subclasses of a
#given input class
def subclass_query_function(input_class):
    function_list = [prefix_func(), select_func(['s'], 1), where_subclass_query_func(input_class)]
    return ''.join(function_list)

query_for_subclasses = subclass_query_function('http://purl.obolibrary.org/obo/ENVO_00002200')
#query_for_subclasses = subclass_query_function('http://purl.obolibrary.org/obo/PCO_0000002')

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

#  make a list of the classes collected from the first query
str_list = []
for res in results["results"]["bindings"] :
   str_list.append(res['s']['value'])

# for r in str_list:
#     print r

# Put together a VALUES block to filter using a single variable/column
def values_filtering_func(input_list):
    s = '>)(<'
    return 'VALUES (?filter) { (<' + s.join(input_list) + '>) }\n'

# Put together a WHERE clause
# A second attempt which will only be used to query_associated_data
def where_query_associated_data_func():
    s = 'WHERE {\n'
    s += '?s rdf:type obo:OBCS_0000120 ; \n'
    s += 'html:rfc4180row ?DataItemRows .\n'
    s += '?DataItemRows ?p ?filter ; \n'
    s += '?c ?o . \n'
    s += 'filter (?c != rdf:type && ?o != html:rfc4180Row) \n'
    s += 'filter (?c != html:rfc4180rowPosition) \n'
    s += 'filter (?c != ?p) \n'
    s += values_filtering_func(str_list) + '}'
    return s
#print where_query_associated_data_func()

#Put together a sparql query which will retrieve data from the datastore which
#has columns annotated with any PURLs given as input

def query_associated_data():
    f_list = [prefix_func(), select_func(['c', 'o'], 0) , from_func(), where_query_associated_data_func() ]
    return''.join(f_list)

# query within local file

#initialize the ConjunctiveGraph which will function as the entire datastore
graph = g.ConjunctiveGraph()
graph.parse('datastore.ttl', format='ttl')
#print graph.serialize(format='ttl')

results = graph.query(query_associated_data())

for row in results:
   print "%s | %s" % row




# for row in results:
#     print "%s" % row

# for row in results:
#     print "%s | %s | %s" % row
