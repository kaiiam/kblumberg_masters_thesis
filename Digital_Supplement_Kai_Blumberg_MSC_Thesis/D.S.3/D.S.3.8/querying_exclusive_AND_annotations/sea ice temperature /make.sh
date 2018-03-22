#!/bin/bash

# $1 purl from term to get subclasses of eg sea water http://purl.obolibrary.org/obo/ENVO_00002200
# $2 purl for term to perform and eg depth http://purl.obolibrary.org/obo/PATO_0001595

./query_for_subclasses_of_input_purl.py $1

./query_for_data_about_exclusive_and_complete.py subclasses_of_*.txt $2

./query_for_data_about_exclusive_and_advanced.py subclasses_of_*.txt $2

./query_for_data_about_exclusive_and_intermediate.py subclasses_of_*.txt $2

./query_for_data_about_exclusive_and_basic.py subclasses_of_*.txt $2
