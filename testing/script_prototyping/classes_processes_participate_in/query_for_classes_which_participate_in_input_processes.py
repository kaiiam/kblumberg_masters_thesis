#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import fileinput

### Script to query for all classes which participate in subclasses of a given process ###

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

for r in subproperty_list:
    print r
