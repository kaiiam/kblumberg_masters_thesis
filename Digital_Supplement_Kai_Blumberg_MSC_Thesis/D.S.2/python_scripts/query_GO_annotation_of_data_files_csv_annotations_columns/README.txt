Script to query the datastore for any data about an input list of GO terms which belong to any omic data which is about an input list of input purls (such as ENVO terms)

: query_GO_annotation_of_data_files_csv_annotations_columns.py

example run:

./query_GO_annotation_of_data_files_csv_annotations_columns.py subclasses_of_ENVO_00000447.txt subclasses_of_GO_0046914.txt

Can ask questions such as: "Return all genomic annotation data about a given set of molecular functions in any type of X environment." 

takes 2 inputs: 

1) A list of annotation terms by which to search for a csv file in the datastore

2) A list of terms which which individual data points are annotated, for example GO terms. This will return all data from all rows annotated with input terms. For example rows with a GO molecular function will also return the sample's counts data associated with that term. 


