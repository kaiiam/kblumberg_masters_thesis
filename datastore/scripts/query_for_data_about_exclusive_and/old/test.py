#!/usr/bin/python

import re

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
#print str.split( )
#print str.split(' ', 1 )

l = []
#l.append('http://purl.obolibrary.org/obo/ENVO_03000073, ub2bL22058C79, http://purl.obolibrary.org/obo/PATO_0000051, ub2bL22057C52')
#l.append('ub2bL21943C79, http://purl.obolibrary.org/obo/PATO_0000146, http://purl.obolibrary.org/obo/ENVO_01000406, ub2bL21942C52, ub2bL21945C72, http://purl.obolibrary.org/obo/ENVO_03000073')

l.append('ub2bL21526C72', 'ub2bL21524C79', 'http://purl.obolibrary.org/obo/PATO_0001595', 'http://purl.obolibrary.org/obo/ENVO_01000406', 'http://purl.obolibrary.org/obo/ENVO_03000071', 'ub2bL21523C52')
l.append('ub2bL21943C79', 'http://purl.obolibrary.org/obo/PATO_0000146', 'ub2bL21942C52', 'http://purl.obolibrary.org/obo/ENVO_01000406', 'ub2bL21945C72', 'http://purl.obolibrary.org/obo/ENVO_03000073')
l.append('ub2bL21974C72', 'ub2bL21972C79', 'ub2bL21971C52', 'http://purl.obolibrary.org/obo/PATO_0001595', 'http://purl.obolibrary.org/obo/ENVO_01000406', 'http://purl.obolibrary.org/obo/ENVO_03000073')
l.append('http://purl.obolibrary.org/obo/ENVO_03000073', 'ub2bL22058C79', 'http://purl.obolibrary.org/obo/PATO_0000051', 'ub2bL22057C52')
l.append('ub2bL21613C52', 'ub2bL21614C78', 'http://purl.obolibrary.org/obo/ENVO_03000071', 'http://purl.obolibrary.org/obo/BFO_0000024')
l.append('http://purl.obolibrary.org/obo/ENVO_03000073', 'ub2bL22019C78', 'http://purl.obolibrary.org/obo/OBI_0000963', 'ub2bL22018C52')
l.append('http://purl.obolibrary.org/obo/ENVO_03000071', 'ub2bL21638C52', 'ub2bL21639C79', 'http://purl.obolibrary.org/obo/PATO_0000051')
l.append('http://purl.obolibrary.org/obo/CHEBI_18230', 'http://purl.obolibrary.org/obo/ENVO_03000073', 'ub2bL2352C52')
l.append('http://purl.obolibrary.org/obo/CHEBI_18230', 'ub2bL2315C52', 'http://purl.obolibrary.org/obo/ENVO_03000071')
l.append('http://purl.obolibrary.org/obo/ENVO_03000071')
l.append('http://purl.obolibrary.org/obo/ENVO_03000071', 'http://purl.obolibrary.org/obo/ENVO_01000406', 'http://purl.obolibrary.org/obo/PATO_0001595', 'ub2bL21552C52', 'ub2bL21553C79', 'ub2bL21555C72')
l.append(ub2bL21570C72', 'ub2bL21567C52', 'http://purl.obolibrary.org/obo/PATO_0001595', 'http://purl.obolibrary.org/obo/ENVO_01000406', 'http://purl.obolibrary.org/obo/ENVO_03000071', 'ub2bL21568C79')
l.append('ub2bL21986C52', 'http://purl.obolibrary.org/obo/PATO_0001595', 'http://purl.obolibrary.org/obo/ENVO_01000406', 'http://purl.obolibrary.org/obo/ENVO_03000073', 'ub2bL21987C79', 'ub2bL21989C72')
l.append('ub2bL22033C78', 'http://purl.obolibrary.org/obo/BFO_0000024', 'http://purl.obolibrary.org/obo/ENVO_03000073', 'ub2bL22032C52')
l.append('ub2bL21927C52', 'http://purl.obolibrary.org/obo/PATO_0001595', 'http://purl.obolibrary.org/obo/ENVO_01000406', 'http://purl.obolibrary.org/obo/ENVO_03000073', 'ub2bL21930C72', 'ub2bL21928C79')
l.append('http://purl.obolibrary.org/obo/OBI_0000963', 'http://purl.obolibrary.org/obo/ENVO_03000071', 'ub2bL21599C52', 'ub2bL21600C78')



column = []
for s in l:
    column.append(s.split(', '))


#this works but perhaps there's a better way not worth investigate how to optimize now. something like s apply in python
for l in column:
    for x in l:
        #print type(x)
        if re.match("^http://purl.obolibrary.org/obo/", x):
            print x
