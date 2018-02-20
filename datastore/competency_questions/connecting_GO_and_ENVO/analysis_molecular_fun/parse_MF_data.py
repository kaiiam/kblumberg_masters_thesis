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
import pandas as pd

in_arg = str(sys.argv[1])

aby_data = []
bat_data = []
ner_data = []

with open(in_arg, "rb") as f:
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

print aby_str

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

in_arg = re.sub('[.]csv', '', in_arg)
outstring =  in_arg + '_cleaned.csv'

merged2.to_csv(outstring, sep=',', encoding='utf-8')
