#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import fileinput
import re                   #to filter files using regex
import csv



#list of all GO mf cc or bp terms
in_file3 = open(str(sys.argv[1]), 'r')

#Create and clean a list of PURLS from the inputfile
in_args3 = []
in_args3 += [line.rstrip('\n') for line in in_file3]



matrix = []

with open("go_envo_data_all_MF_in_example.csv", "rb") as f:
    reader = csv.reader(f, delimiter=",")
    # for i, line in enumerate(reader):
    #     print 'line[{}] = {}'.format(i, line)
    for line in reader:
        matrix.append(line)

#matrix[row][column] using 0 based indexing.

#do need these for now unless I
# abyssal = []
# for x in matrix:
#     if "abyssal" in x[0]:
#         abyssal.append(x)
# bathyal = []
# for x in matrix:
#     #print x[0]
#     if "bathyal" in x[0]:
#         bathyal.append(x)
# neritic = []
# for x in matrix:
#     if "neritic" in x[0]:
#         neritic.append(x)

#list of non headers lines:
data_rows = []
for idx,x in enumerate(matrix):
    #print x[1]
    if 'http://purl.obolibrary.org/obo/' not in x[1]:
        data_rows.append(idx)

ab_data_rows = []
ba_data_rows = []
ne_data_rows = []
abyssal = []
bathyal = []
neritic = []
for idx,x in enumerate(matrix):
    #print x[1]
    if 'http://purl.obolibrary.org/obo/' not in x[1]:
        if "abyssal" in x[0]:
            ab_data_rows.append(idx)
        if "bathyal" in x[0]:
            ba_data_rows.append(idx)
        if "neritic" in x[0]:
            ne_data_rows.append(idx)
    else:
        if "abyssal" in x[0]:
            abyssal.append(x)
        if "bathyal" in x[0]:
            bathyal.append(x)
        if "neritic" in x[0]:
            neritic.append(x)


# print ab_data_rows
# print ba_data_rows
# print ne_data_rows


aby_cols = []
for x in abyssal:
    if 'http://purl.obolibrary.org/obo/' in x[1]:
        for y in x:
            aby_cols.append(y)

bat_cols = []
for x in abyssal:
    if 'http://purl.obolibrary.org/obo/' in x[1]:
        for y in x:
            bat_cols.append(y)

ner_cols = []
for x in neritic:
    if 'http://purl.obolibrary.org/obo/' in x[1]:
        for y in x:
            ner_cols.append(y)


#print ner_cols[1:]

#could try using in_args3 as the master index list of columns to have all other columns map to. that way we get items from both sets. Then could drop columsn which are all 0
#print in_args3

#print len(ner_cols)
#print len(bat_cols)
complete_list = list(set(in_args3))
complete_list.append('sample')
# print len(in_args3)
# print len(set(in_args3))

aby_indices = [complete_list.index(i) for i in aby_cols[1:]]
bat_indices = [complete_list.index(i) for i in bat_cols[1:]]
ner_indices = [complete_list.index(i) for i in ner_cols[1:]]



#print complete_list
#print data_rows

# print len (aby_indices)
# print len (bat_indices)
# print len (ner_indices)
# print len(complete_list)
# #
# print aby_indices
# print bat_indices
# print ner_indices



test_list =[]
for x in xrange(0,len(complete_list)):
    test_list.append(0)

# complete_matrix = []
# for x in xrange(0,len(data_rows)):
#     complete_matrix.append(test_list)
#
# for idx, x in enumerate(complete_matrix[0]):
#     x = complete_list[(idx-1)]
#     print x
aby_list=[]
for x in xrange(0,len(complete_list)):
    for y in aby_indices:
        if y = x :
            print aby_indices[y]


#######
#try if the aby_indices this x th's position match y for all z in aby_indices then print that aby_indices value?




#build complete_matrix iteratively by row
complete_matrix = []
complete_matrix.append(complete_list)

#print complete_matrix

# #using ner as the template column ordering
# bat_return_indices = []
# for x in aby_cols:
#     #print x
#     for idx, y in enumerate(bat_cols):
#         if x == y:
#             bat_return_indices.append(idx)
#
# print len( bat_return_indices)
#
#
# ner_return_indices = []
# for x in aby_cols:
#     #print x
#     for idx, y in enumerate(ner_cols):
#         if x == y:
#             ner_return_indices.append(idx)
#
#
# print len(ner_return_indices)
#


# return_indices = []
# for idx, l in enumerate(fobj):
#     for k in in_args:
#         if (k in l) and (in_arg2 in l):
#             #print idx, l
#             return_indices.append(idx)

#print aby_cols

# for x in xrange(0,len(abyssal)):
#     print abyssal[x][0]
