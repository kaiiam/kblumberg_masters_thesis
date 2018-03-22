D.S.3.8: Estimation of predicted-user data-mobilization proficiency

Which contains the folders querying_exclusive_AND_annotations and querying_parts_of_annotation

Both of these folders are have a set of querying simulation cases, which are their subfolders, along with the analysis folder wich contain the R scripts to generate the plots. 

Within each subfolder of the querying_exclusive_AND_annotations there are the following scripts: query_for_subclasses_of_input_purl.py to get the subclasses of the the input class. Then there are the scripts query_for_data_about_exclusive_and_advanced.py, query_for_data_about_exclusive_and_basic.py, query_for_data_about_exclusive_and_complete.py, query_for_data_about_exclusive_and_intermediate.py which are modified version of script py.10: query_for_data_about_exclusive_and.py, which gets data which is annotated as being about an input classes plus its subclasses AND another input class retrieved at different levels of querying proficiency. 

Within the querying_parts_of_annotation subfolders there are the following scripts: query_for_parts_associated_with_input_class.py to get the parts classes associated with the input class. These parts are then passed to the query_annotation_of_data_files_data_or_columns_about_input_advanced.py,
query_annotation_of_data_files_data_or_columns_about_input_basic.py, query_annotation_of_data_files_data_or_columns_about_input_complete.py, query_annotation_of_data_files_data_or_columns_about_input_intermediate.py scripts which are modified version of the py.5: query_annotation_of_data_files_data_or_columns_about_input.py script, to get retrieve data about the parts of input classes retrieved at different levels of querying proficiency. 

For both folders each of their subfolders contain a make.sh file which is used to run the batch of scripts together and the results of running the scripts are written to the advanced, basic, complete, intermediate files. I manually parsed these files to collect the retrieval statistcs.  

To redo this analysis the path to the datastore.ttl file would need to be specified in all the scripts. 


