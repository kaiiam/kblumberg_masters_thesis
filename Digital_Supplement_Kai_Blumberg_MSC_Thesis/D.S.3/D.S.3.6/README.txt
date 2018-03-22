D.S.3.6: Retrieval of classes linked by subclasses and subproperties

This folder contains 3 folders:

full_analysis: to discover classes which are associated with classes which are subclasses of an input class associate via relations which are properties of a subproperty. for example participants in sea ice formation processes. Where the entire workflow is functioning properly. To do this we use query_for_subclasses_of_input_purl.py to get the subclasses, query_for_subproperties_of_input_purl.py
to get the subproperties, query_for_classes_linked_by_input_classes_and_input_properties.py to discover linked classes, and query_annotation_of_data_files_data_or_columns_about_input.py to get the data about the linked classes. 

analysis_lacking_RO: where I test the workflow from the full_analysis minus the query_for_classes_linked_by_input_classes_and_input_properties.py script.

analysis_subclass_hierarchy where I test the workflow from the full_analysis but without the query_for_subclasses_of_input_purl.py script to get subclasses of the input class. 

 
