D.S.3.2: Interconnecting genomic and environmental data via ontologies

Contained within this folder are the following folders:

analysis: to find and calculate the relative genomic porportions of oxidation-reduction process, transition metal ion binding, transition metal ion transport, vitamin biosynthetic process
 
pcoa_analysis: To produce the PCoA plots for: biological process, cellular amino acid biosynthetic processes and cellular amino acid biosynthetic process from various marine benthic biomes

both of which use the script query_for_subclasses_of_input_purl.py to get subclasses of GO or ENVO terms of interest and feed the results into the query_GO_annotation_of_data_files_csv_annotations_columns.py to get the data which are annotated with the GO and ENVO term lists of interest. 
