#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON #to perform web sparql queries
import rdflib                 #to query using the rdflib module
import rdfextras             #to query using the rdflib module
import rdflib.graph as g    #to query using the rdflib module
rdfextras.registerplugins() # so we can Graph.query()
import sys                 #to deal with input args
import fileinput           #to input files
import re                   #to filter files using regex
import unicodedata          #to convert literals to strings
import csv                   #for csv output
import pandas as pd         #for data parsing
########################################################################

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
# change this to the location of the datastore.ttl file
def from_func():
    return 'FROM <../../../datastore.ttl>\n'

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

#change this to the location of the datastore.ttl file
graph.parse('../../../datastore.ttl', format='ttl')

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
    s += '	(group_concat(?value; separator=",") as ?value)\n'
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

out = re.sub('[.]txt', '', str(sys.argv[2]))
out = re.sub('subclasses_of', '', out)

outstring = 'go_envo_data' + out + '.csv'
f = open(outstring, 'w')
for row in results2:
    f.write ("%s,%s\n" % row)

##########################################################################################
#re-read and clean the data. so it can be analyzed in R

aby_data = []
bat_data = []
ner_data = []

with open(outstring, "rb") as f:
    reader = csv.reader(f, delimiter=",")
    for line in reader:
        if "abyssal" in line[0]:
            if 'http://purl.obolibrary.org/obo/' in line[1]:
                aby_list = line
                aby_str = str(line[0])
            else:
                aby_data.append(line)
        if "bathyal" in line[0]:
            if 'http://purl.obolibrary.org/obo/' in line[1]:
                bat_list = line
                bat_str = str(line[0])
            else:
                bat_data.append(line)
        if "neritic" in line[0]:
            if 'http://purl.obolibrary.org/obo/' in line[1]:
                ner_list = line
                ner_str = str(line[0])
            else:
                ner_data.append(line)

aby_list = ['sample' if x==aby_str else x for x in aby_list]
bat_list = ['sample' if x==bat_str else x for x in bat_list]
ner_list = ['sample' if x==ner_str else x for x in ner_list]

aby_df = pd.DataFrame(aby_data, columns=aby_list  )
bat_df = pd.DataFrame(bat_data, columns=bat_list  )
ner_df = pd.DataFrame(ner_data, columns=ner_list  )

i_list = list(set(aby_list).intersection(bat_list))

#merge aby and bat
merged = pd.merge(aby_df,bat_df, on=i_list, how='outer')

m_list = list(merged.columns)
intersection_list = list(set(ner_list).intersection(m_list))

merged2 = pd.merge(merged,ner_df,on=intersection_list, how='outer')
merged2.set_index('sample', inplace=True)
merged2.fillna(0,inplace=True)

merged2.to_csv(outstring, sep=',', encoding='utf-8')
