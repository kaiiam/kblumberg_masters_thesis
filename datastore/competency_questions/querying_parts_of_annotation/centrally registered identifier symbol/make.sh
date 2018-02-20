#!/bin/bash

# $1 purl from term to get parts associated with eg sea water http://purl.obolibrary.org/obo/ENVO_00002200

./query_for_parts_associated_with_input_class.py $1

./query_annotation_of_data_files_data_or_columns_about_input_advanced.py parts_associated_with_*.txt
./query_annotation_of_data_files_data_or_columns_about_input_basic.py parts_associated_with_*.txt
./query_annotation_of_data_files_data_or_columns_about_input_complete.py parts_associated_with_*.txt
./query_annotation_of_data_files_data_or_columns_about_input_intermediate.py parts_associated_with_*.txt
