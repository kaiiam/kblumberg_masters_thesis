
use the script query_for_subclasses_of_input_purl.py to get subclasses of the classes of interest

for example:
./query_for_subclasses_of_input_purl.py http://purl.obolibrary.org/obo/GO_0008652

use the script query_GO_annotation_of_data_files_csv_annotations_columns.py to get data about the subclasses of the input go terms along with subclasses of marine benthic biome ENVO_01000024

for example

./query_GO_annotation_of_data_files_csv_annotations_columns.py subclasses_of_ENVO_01000024.txt subclasses_of_GO_0009070.txt

do this to get the relative proportions of oxidation-reduction process, transition metal ion binding, transition metal ion transport, vitamin biosynthetic process

use all all_MF_in_example/all_BP_in_example and go_envo_data_all_BP_in_example.csv/go_envo_data_all_MF_in_example.csv as the denominator to standardize the proportions counts. 
