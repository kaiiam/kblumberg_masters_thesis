D.S.3.1: Building the and annotating the datastore

build_datastore: This folder contains all the material by which to build the datastore used in this work. It contains:

.csv data files

annotation.ttl data annoation turtle files

.ttl files the merged turtle versions of the .csv and annotation.ttl files (created during the process of building the datastore)

create_rdf_triples_from_csv_files.py: a script to convert all csv data files in a directory to triple files

merge_triples_to_datastore.py: Script to merge the rdf files into a single datastore.ttl file
