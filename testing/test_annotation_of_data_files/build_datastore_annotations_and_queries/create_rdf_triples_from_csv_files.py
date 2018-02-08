#!/usr/bin/python

import fileinput            #to parse inputfile line by line
import os                   #to get files in working directory
import re                   #to filter files using regex
import rdflib               #to parse rdf data
import rdflib.graph as g    #to create ConjunctiveGraph to hold the datastore
import subprocess           #to send a bash command out to the command line

##### Script to convert all csv data files in a directory to triple files #####
#requires any23 to be installed

# list all the files in the directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

#filter for .csv files using regex search:
regex = re.compile('[.]csv')
selected_files = filter(regex.search, files)

#remove the .csv extension from the file names.
file_names = []
file_names += [re.sub('[.]csv', '', f) for f in selected_files]

# function to send a bash command out to the commandline
def run(command):
    output = subprocess.check_output(command, shell=True)
    return output

#run any23 rover for all csv files
for f in file_names :
    run('any23 rover -t -p -f turtle -o %s.ttl %s.csv' % (f, f))
