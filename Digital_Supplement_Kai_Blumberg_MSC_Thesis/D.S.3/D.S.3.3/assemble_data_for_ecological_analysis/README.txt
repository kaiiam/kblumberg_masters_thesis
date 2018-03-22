# get subclasses of chlorophyll a
./query_for_subclasses_of_input_purl.py http://purl.obolibrary.org/obo/CHEBI_18230

# get subclasses of seawater
./query_for_subclasses_of_input_purl.py http://purl.obolibrary.org/obo/ENVO_00002149

# get subclasses of marine water body
./query_for_subclasses_of_input_purl.py http://purl.obolibrary.org/obo/ENVO_00001999

# get subclasses of sea ice
./query_for_subclasses_of_input_purl.py http://purl.obolibrary.org/obo/ENVO_00002200

# join all the subclass results into the file:
cat subclasses_of_* > joined_semantics_list.txt

# get data about all the classes referenced in **environment determined by a phytoplankton community associated with sea-ice** along with their subclasses 
./query_annotation_of_data_columns_about_input.py joined_semantics_list.txt

#open the csv file in libreoffice/excel to fix the commas, on to the R script
