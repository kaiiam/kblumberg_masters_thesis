#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import fileinput
import re                   #to filter files using regex

### Script to query for all classes which are linked to by given input lists of classes and properties ###
#for example the input classes could be subclasses of a particular process e.g. 'water ice formation process'
#and the properties could be subproperties of for example 'has participant' or 'overlaps'
#to be able to ask questions such as what entities participate in some process or
#what classes are 'mereotopologically related to' the subclasses of an input class.

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

########################################################################
#sparql query assembly:

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

def from_func():
    return 'FROM <envoPolarttl.owl>\n'


# Put together a VALUES block to filter using a single variable/column, with variable name var_name
def values_filtering_func(input_list, var_name):
    s = '>)\n(<'
    return 'VALUES (?'+ str(var_name) +') { \n(<' + s.join(input_list) + '>) }\n'

# Put together a WHERE clause which will query for classes are related by an input list of properties
#and an input list of classes
def where_query_classes_participate_in_processes():
    s = 'WHERE {\n'
    s += '?participant rdfs:subClassOf ?node . \n'
    s += '?node rdf:type owl:Restriction . \n'
    s += '?node owl:onProperty ?property .  \n'
    s += '{ ?node owl:someValuesFrom ?value . \n'
    s += '?value rdfs:label ?label . } \n'
    s += 'UNION \n'
    s += '{ ?node owl:someValuesFrom ?v . \n'
    s += '?v owl:unionOf/rdf:rest*/rdf:first ?value . } \n'
    s += values_filtering_func(subproperty_list, 'property')
    s += values_filtering_func(subclasses_list, 'participant') + '}'
    return s

#Put together a sparql query which will query for classes which are are related by an
#input list of properties and an input list of classes
def query_associated_data():
    f_list = [prefix_func(), select_func(['participant', 'property', 'value'], 1), from_func(), where_query_classes_participate_in_processes() ]
    return''.join(f_list)

########################################################################
# # wrap the ontobee SPARQL end-point
# endpoint = SPARQLWrapper("http://sparql.hegroup.org/sparql/")
# # set the query string
# endpoint.setQuery(query_associated_data())
# # select the return format (e.g. XML, JSON etc...)
# endpoint.setReturnFormat(JSON)
# # execute the query and convert into Python objects
# # Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
# results = endpoint.query().convert()

graph = g.ConjunctiveGraph()

graph.parse('envoPolarttl.owl', format='ttl')

results = graph.query(query_associated_data())





#save the results to a file with the name of the input purl
input_class_namestr = str(sys.argv[1])
#clean the input_class_namestr
input_class_namestr = re.sub('subclasses_of_', '', input_class_namestr)
input_class_namestr = re.sub('.txt', '', input_class_namestr)
input_class_namestr = re.sub('./', '', input_class_namestr)


input_property_namestr = str(sys.argv[2])
#clean the input_property_namestr
input_property_namestr = re.sub('subproperties_of_', '', input_property_namestr)
input_property_namestr = re.sub('.txt', '', input_property_namestr)

#make the file name to write to
outstring = 'classes_related_by_' + input_class_namestr + '_classes_and_' + input_property_namestr + '_properties.csv'

#create output csv file
f = open(outstring, 'w')
#write headers
f.write('Input Class,Property,Class Related to Input Class by Property\n')
#write results
# for res in results["results"]["bindings"]:
#    f.write( str(res['participant']['value'] + ',' + res['property']['value'] + ',' + res['value']['value'] + '\n' ))
for row in results:
   f.write( "%s,%s,%s\n" % row)



# #old code to print results to terminal
# for row in results:
#    print "%s | %s | %s" % row
