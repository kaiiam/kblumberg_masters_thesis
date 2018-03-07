---
title: '\begin{minipage}{\textwidth}\protect\centering
Interconnecting Arctic observatory \\ data through machine-actionable knowledge \\ representation: are ontologies fit for purpose? \\
\end{minipage}'

author: '\begin{minipage}{\textwidth}\protect\centering \textbf{Masters Thesis}\\ submitted by\\ \textbf{Kai Blumberg}\footnote{\url{https://orcid.org/0000-0002-3410-4655}} \end{minipage}'
---

---
toc: True
---


\pagebreak
# Summary


The scientific community is faced with the challenge of managing large quantities of environmental and genomic data. Ontologies represent expert scientific knowledge in human machine readable formats. Ontology terms can be used to annotate interdisciplinary datasets stored in machine-actionable linked open data formats. Such practices allow data to be findable, accessible, interoperable and reusable to both humans and machine agents. Openly published environmental and genomic data often lack machine-focused accessibility, precluding integrated analyses from being performed. Here we show that ontologies are fit for purpose to address data management challenges by interconnecting disparate datasets with interoperable terminology. We demonstrated how datasets annotated with ontology terms can be mobilized via semantic querying to facilitate the assembly of data upon which to perform ecological analyses. We investigated the network properties of an example ontological knowledge graph. Although we found the upper level semantic model BFO provides a well-connected hierarchical structure, a lack of connectivity pervades the majority of ontology terms. This hinders ontology knowledge graphs from guiding users to novel information. Finally, we demonstrated how interoperable ontology terms can be leveraged to generate bioinformatic hypotheses from the comparison of environmentally annotated omics datasets. We anticipate these results will be a starting point for further analysis of how ontology terms can be used to interconnect environmental and genomic data. As well use ontology terms to improve the accessibility and reuse of published data.



\pagebreak
# Abbreviations

**Acronyms**

ANY23 Anything To Triples

AWI Alfred Wegener Institute Helmholtz Centre for Polar and Marine Research

BFO Basic Formal Ontology DOI Digital Object Identifier

ECOCORE Ontology of Core Ecological Entities

ENVO Environment Ontology FRAM FRontiers in Arctic marine Monitoring

IACS International Association of Cryospheric Sciences

IAO Information Artifact Ontology

MIxS Minimum Information about any (x) Sequence NASA National Aeronautics and Space Administration

NOAA National Oceanic and Atmospheric Administration

OBCS Ontology of Biological and Clinical Statistics

OBO Open Biological and Biomedical Ontology

ORCID Open Researcher and Contributor ID

ORF Open Reading Frame

OWL Web Ontology Language

PATO Phenotypic Quality Ontology

PCA Principal Component Analysis

PCoA Principal COordinate Analysis

PCO Population and Community Ontology

RDF Resource Description Framework

RO Relations Ontology SPARQL

SPARQL Protocol and RDF Query Language

SWEET Semantic Web for Earth and Environmental Technology

UNESCO United Nations Educational Scientific and Cultural Organization

URI Uniform Resource Identifier

\pagebreak
**python scripts**

py.1 create_rdf_triples_from_csv_files.py

py.2 histogram_median.py

py.3 merge_triples_to_datastore.py

py.4 network_distribution_stats.py

py.5 query_annotation_of_data_files_data_or_columns_about_input.py

py.6 query_data_set_references.py

py.7 query_for_class.py

py.8 query_for_classes_linked_by_input_classes_and_input_properties.py

py.9 query_for_created_by.py

py.10 query_for_data_about_exclusive_and.py

py.11 query_for_parts_associated_with_input_class.py

py.12 query_for_property.py

py.13 query_for_subclasses_of_input_purl.py

py.14 query_for_subproperties_of_input_purl.py

py.15 query_for_term_editor.py

py.16 query_GO_annotation_of_data_files_csv_annotations_columns.py


**R scripts**

R.1 data_set_references.r

R.2 degree_calculation.r

R.3 pca_analysis.r

R.4 pcoa_analysis.r

R.5 querying_exclusive_AND_annotations.r

R.6 query_parts_of_annotation.r


\pagebreak
# 1. Introduction


Unprecedented quantities of data and information generated as a result of the information revolution have arguably made the world more uncertain complex and ambiguous than less [@Hortal_2015]. As a consequence, challenges we face tend to be dilemmas requiring management, rather than easily defined problems to solve [@johansen2007]. Coming technological advances will further accelerate the rate of ecological data capture [@Hortal_2015]. Lacking well-established repositories or standard protocols for the management of ecological data [@Madin_2007], such influxes of data have the potential to contribute rather than detract from uncertainty about the natural world. The Earth system is facing unprecedented anthropogenic pressures which have the potential to destabilize critical biophysical systems, triggering irreversible environmental changes [@Rockström_2009]. Needed are strategies to store ecological data in a way which captures subtleties of the data’s structure, content and inter-relationships [@Madin_2007]. This holds especially true for vulnerable and rapidly changing environments, such as polar systems which have been predicted to be free ice within 20-50 years [@Wang_2009]. Despite the existence of numerous environmental monitoring efforts such as AtlantOS [@AtlantOS], the Fixed point Open Ocean Observatory network (FixO3) [@fixo3], or the Hausgarten Long-Term Arctic Observatory [@Soltwedel_2005]. The management and integration of generated data remains a major obstacle, precluding integrated analysis from being performed on interdisciplinary data. Working toward the improvement of infrastructure for scholarly data publication, Wilkinson et al. (2016) have proposed the FAIR data guiding principles of data findability, accessibility, interoperability and reusability. These principles aim to promote the publication of data which is accessible to both humans, as well as machines [@Wilkinson_2016]. Although many ecological datasets, such as those generated by observatories, have been published to openly accessible repositories such as PANGAEA [@pangaea] or the Biological and Chemical Oceanography Data Management Office (BCO-DMO) [@bco_dmo]. Data contained within such repositories are typically not machine-readable, or interoperable. In order to make annotated data work interoperably, annotations need to make use of controlled, universally shared, and machine accessible vocabularies. Such annotation terms can be provided by ontologies.

An ontology is a hierarchically structured, machine and human readable representation of the knowledge used by experts to describe entities, and capture the relationships between them [@Smith_2007]. In informatics, ontologies exist in the form of a knowledge graph, where nodes represent entities, and edges represent logical relations linking entities together (i.e. axioms). Ontologies provide a digital semantic infrastructure upon which advanced querying, discovery and analysis of data can occur. Ontologies are typically developed to cover the terminological needs of a particular domain of interest. In order to interconnect ontologies representing scientific knowledge from different domains, as well as coordinate their development, the Open Biological and Biomedical Ontology (OBO) Foundry and Library was created [@Smith_2007]. OBO Foundry ontologies share common upper level semantic models. Notable the Basic Formal Ontology (BFO) [@Arp_2015][@bfo_homepage] providing common hierarchical structures by which to characterize knowledge, and the Relations Ontology (RO) [@obo-relations], to standardize the connections between represented knowledge. Existing OBO ontologies such as the Environment and Gene Ontologies, for the description of environments [@Buttigieg_2013][@Buttigieg_2016] and genetic functions [@Ashburner_2000] are designed to work interoperably. Efforts to use these ontologies in combination, however, have infrequently been attempted [@Henschel_2015].

Ontologies make use of Semantic Web technologies to interconnect information. The Semantic Web is an extension of the World Wide Web, which provide common data formats and exchange protocols on the Web [@tim_berners-lee_world]. The Semantic Web stores data in a format by which the meaning of the data is processable by computers, referred to as machine-readable data [@tim_berners-lee_world]. Data is rendered machine-readable by converting it into a format compliant with the Resource Description Framework (RDF) [@david_beckett_rdf_2014]. Such formatting allows data to be linked to other data, stored in open formats. Linked data can be accessed through semantic queries, performed using the SPARQL Protocol and RDF Query Language (SPARQL) [@steve_harris_sparql_2013].

Within medical domains ontologies have been used to interconnect disparate data and information, enabling computational interrogation of models to reveal underlying relationships. For example, Monarch Initiative uses an ontology-based strategy to integrate genotype–phenotype data from various sources and species, enabling users to explore phenotypic and genotypic relationships across species [@Mungall_2016]. Although ontologies have not yet been utilized to fully integrate environmental and omics data, efforts to such extent are underway [@Stec_2017]. Analogously to what has been done in medical domains, the use of federated ontology semantics have been discussed as having the potential to link data about phenotypes with environment [@Thessen_2015], as well as environmental and genomic datasets [26]. This would allow for users to submit queries of linked data asking questions such as "Which crop varieties are expected to do well in a particular location over the next century?", [@Thessen_2015], or "Can we gather all metagenomes collected from insects found in soil?" [@Walls_2014].

The first steps toward using ontologies to integrate environment and genomic data have been undertaken via the creation of the Earth Microbiome Project application Ontology (EMPO). Built as subset of the Environment Ontology, EMPO provides the semantics by which to map environmental 16S tag sequence data to descriptions of environmental features [@Thompson_2017]. Future work is required to integrate large publicity available genomic sequence datasets with consistently structured accompanying environmental metadata. Examples of such datasets include the TARA Oceans project [@Ainsworth_2013], the Global Ocean Sampling Expedition [@Ledford_2007] and the Hawaii Ocean Time-series (HOT) program [@KARL1996129]. Unfortunately, the data publication formats of such datasets often preclude them from being semantically querable. Efforts to make such environment sequencing data semantically querable are underway by research groups such as the Cyberinfrastructure for Microbial Ecology [@hurwitz_lab], who have developed tools such as the Ocean Cloud Commons (OCC), which allows for researchers to query the Tara Oceans Expedition Data [@ocean_cloud]. With future projects aiming to integrate publicly available genomic and oceanographic data [@planet_microbe]. Such efforts would benefit from the use of well-structured ontology semantics by which to mobilize and interconnect environmental and genomic data.

In as far as integrating environmental observatory data, ontologies such as the Human-Aware Sensor Network Ontology (HASNetO) have been used to support the data management of a number of large-scale ecological monitoring activities [@Pinheiro_2017]. These efforts are relevant to the upcoming United Nations decade of ocean science for sustainable development 2021-2030 [@UN_decade_ocean]. Which will bring an influx of data from proposed earth and ocean monitoring activities. These efforts will employ sensor networks which will generate vast quantities of data of heterogeneous types. Networks of sensors deployed to perform environmental monitoring activities will comprise a future Sensor Web, intended to improve the ability to detect, monitor, and predict weather climate and the onset of natural hazards [@Torres_Martinez_2003]. The ongoing efforts of the Open Geospatial Consortium (OGC) have seen the creation and development of community consensus standards for the Sensor Web [@ogc]. Building upon semantic web technologies, the OGC has created the Sensor Web Enablement (SWE) standards which can be used as building blocks for the Sensor Web [@Broring_2011]. SWE standards enable developers to make all types of sensors, transducers and sensor data repositories discoverable, accessible and usable via the Internet. An example SWE standard is the Sensor Observation Services (SOS), which provides interoperable management of sensor data, allowing users to query the Sensor Web for real-time sensor data [@sos]. Extending the SWE with Semantic Web technologies, is the Semantic Sensor Web (SSW) providing enhanced descriptions and access to sensor data using the Semantic Sensor Network Ontology (SSN) [@Compton_2012]. Ontologies such as the SSN will be important for mobilizing the coming large data generated by sensor networks. Especially if the SSN ontology is made to work interoperably with other ontologies describing environmental phenomena such as the Environment Ontology [@Buttigieg_2013][@Buttigieg_2016] and the suite of Semantic Web for Earth and Environmental Technology (SWEET) ontologies [@sweet_2018].

With future influxes of data from sensor monitoring endeavors along with the ever increasing quantities of genomic data, there is a clear need to find ways to facilitate the management incoming and existing data. This work is motivated by the need to need to overcome barriers preventing the reuse of published data [@Figueiredo_2017], as well as facilitate the publication if data which can be used interoperably.

As well-structured semantics, such as those provided by ontologies benefit the reuse and interoperation of published data, I focused my research on the study of semantics. In semantic research knowledge is treated as the subject of study. In my work, I have applied the scientific method to conduct semantic research. I begin by formulating hypotheses about the representation of knowledge. I have done so by formulating competency questions, as is done in interviews to judge the competence of prospective employees [@calvo2017analysis]. Competency questions are specific and targeted questions which are intended to evaluate how well a person or a system is able to perform certain essential functions. In this work I have created a set of competency questions to judge the fitness for purpose of using ontologies to interconnect interdisciplinary knowledge and data from environmental and genomic domains. Following the scientific method, competency questions are created to serve as testable hypotheses. These competency question based hypotheses can be tested by using ontologies. The results derived from testing competency questions can provide insights by which to formulate and test additional competency question hypotheses. For a description of the adaptation of semantic science and linked open data to facilitate the scientific method, see **Figure S1**.

Ontologies can be used directly to answer competency questions, by searching for relevant knowledge encoded within ontology knowledge graphs. Alternatively, we can test competency questions by using ontologies to gather data and other machine-accessible information from open linked data. This is made possible by setting up linked open data repositories where data is annotated using ontology terms. These open linked ontology annotated data repositories allow for data to be accessed via semantic queries for ontology terms of interest. To be able to ask and answer such competency questions, I have created an example open linked datastore containing environmental and genomic data. For the semantic annotation of such data I made use of ontology terms from the OBO Foundry and Library, which offers a multidisciplinary unified knowledge model spanning various scientific domains [@Walls_2014]. By using the BFO [@Arp_2015] and RO [@obo-relations] upper level semantic models for data annotation, the contents of the datastore can be interconnected via the knowledge represented in the OBO ontology knowledge graph.

To interconnect my example data as well as access information within the OBO knowledge graph, I developed scripts which are able to retrieve classes pertaining to a phenomenon of interest, as well as classes pertaining to connected phenomena. This allows for the interconnections between phenomena encoded into ontologies to be leveraged to interconnect interdisciplinary data, enabling questions to be asked of the interdisciplinary datastore. In this work I employed my semantically-annotated datastore and ontology querying scripts to answer the competency questions I created. These competency questions are intended to assess the fitness for purpose of ontologies to interconnect interdisciplinary environmental and genomic datasets. The following is a description of the competency questions I asked and attempted to answer in the course of this work.

I began by assessing the fitness for purpose of using ontologies to interconnect genomic and environmental data, by asking the following questions:

> "What are the relative abundance frequencies of oxidation-reduction process genes in various types of marine biomes?"

> "What are the relative abundance frequencies of vitamin biosynthetic process genes in various types of marine biomes?"

These questions were aimed to test if ontologies can be used to facilitate the collection of data by which to perform comparative genomic analyses. The results of the second question prompted further analysis leading me to ask the question:

> "What genomic features may help to explain the differences in riboflavin abundances between deep and shallow marine benthic biomes?"

Leveraging the vast quantities of expert knowledge encoded in the GO ontology, I asked the following question:

> "What biological processes differentiate various types of marine benthic biomes?"

Based on the results of this fourth question, and making use of the GO  biological processes hierarchy I asked a more specific question:

> "What cellular amino acid biosynthetic processes differentiate various types of marine benthic biomes?"

Drawing from the results of this question, and again leveraging the GO  biological processes hierarchy I asked an even more specific question:

> "What serine family amino acid biosynthetic processes differentiate various types of marine benthic biomes?"

To assess if ontologies are fit to assemble information upon which to perform an ecology analysis, I asked the following question:

> "What environmental factors have the greatest influence on the dynamics of a sea-ice associated phytoplankton community?"

The following questions address if ontologies are fit for purpose to identify the provenance of knowledge data or other information:

> "How well do the Environment Ontology and the Environment Ontology Polar subset connect authors of terms to the information they helped to encode?"

> "What are all the papers which reference any data set, which is about a part of a marine biome?"

I created the following question to assess the resilience of semantic data annotation models, asking:

> "What percentages of data items discovered to be about participants in sea ice formation processes would be retrievable if we didn’t use the Basic Formal Ontology or Relations Ontology upper level semantic models?"

In the following competency question I addresses if ontologies are fit for purpose to aid scientists to discover data.

> "Is the ontology knowledge graph of the envoPolar subset sufficiently well connected to be able to lead researchers to new knowledge via unstated linkages to identified knowledge?"

The following question addresses the extent to which semantically annotated data is discoverable to general users.

> "What level of querying expertise is required to access the various types of data contained in the example polar datastore?"


Finally, to asses if the process of encoding expert ecological knowledge into an ontology knowledge graph aids to clarify the understanding of ecological phenomena, I asked:

> "Does the inclusion of novel expert knowledge about phenomena relating to plankton ecology into the ENVO knowledge graph aid to better understand the interconnections of such phenomena?



\pagebreak

# 2. Materials and Methods

## 2.1 Model polar datastore creation

I assembled an example polar themed datastore from freely available Alfred Wegener Institute for Polar and Marine Research datasets hosted by the data publisher PANGAEA [@pangaea], as well as data from unpublished metagenomes and metatranscriptomes. I selected data sets primary from the FRAM [@Soltwedel_2013], and Hausgarten [@Soltwedel_2005] observatory projects and programs. I additionally made use of 16S taxonomic and Pfam2GO annotation tables provided courtesy of Josephine Z Rapp, David Probandt, and Matthew Schechter. Such metagenomes and metatranscriptomes samples had previously been processed using the BBDuk tool from the BBTools suite for read quality control [@Bushnell_bbmap], RNA filtered using SortMeRNA [@Kopylova_2012], taxonomically classified for 16S ribosomal RNA with the SINA alignment tool [@Pruesse_2012], ORF-predicted via FragGeneScan tool [@Rho_2010], ORF-annotated with PFAM domains via the Ultra-fast Protein domain Classification tool (UProC) [@Meinicke_2014], and mapped to GO terms using the Pfam2GO annotations page available from http://www.geneontology.org/external2go/pfam2go [@Mitchell_2017]. A list of data sets included in the data store is provided in the appendix **A.2 Model polar datastore creation**. The example datastore was created by converting comma separated value (csv) files into the RDF specification [@richard_cyganiak_rdf_2014] turtle format [@david_beckett_rdf_2014], using the script py.1, which makes use of the Apache Anything To Triples (any23) command line *rover* tool [@any23]. Turtle formatted data along with semantic data annotation files were merged into a single datastore file using the script py.3.

## 2.2 Semantic data annotation

Semantic annotation of the example data was conducted in the RDF serialization turtle facilitate scripting Web Ontology Language (OWL) [@sean_bechhofer_owl_2004] code in RDF. Annotations make use ontology terms from the Open Biomedical Ontologies (OBO) Foundry and Library [@Smith_2007]. Ontology terms were accesses using the [Ontobee](http://www.ontobee.org/) linked data server for ontologies and their terms [@Ong2017]. Ontology term annotation for the example polar datastore made frequent use of ENVO terms from the envoPolar subset which was primarily developed during the *Ecotone* [@pier_luigi_buttigieg_2017_573849], *Polar express* [@chris_mungall_2017_546433], and *Hot tub time machine*
[@chris_mungall_2017_438339] ENVO releases.

**Figure 1** shows an example of the post-compositional data annotation of datasets using ontology terms. The example is of a data column which is about a *chlorophyll a concentration* in *sea water*. Expressed as an ontology axiom, we have a data column: which is BFO:*part of* [BFO_0000050] some OBCS:*data matrix* [OBCS_0000120] and IAO:*is about* [IAO_0000136] some PATO:*concentration of* [PATO_0000033] and RO:*inheres in* [RO_0000052] some CHEBI:*chlorophyll a* [CHEBI_18230] and BFO:*part of* [BFO_0000050] some ENVO:*sea water* [ENVO_00002149].

![**Figure 1** shows the RDF specification turtle code to annotate a data column from a csv file. Item **A** shows the csv file data column is labeled chlorophyll A. Item **B** shows the data column is BFO:*part of* [BFO_0000050] some OBCS:*data matrix* [OBCS_0000120]. Item **C** shows the data matrix column IAO:*is about* [IAO_0000136] more a list of annotation terms. Item **D** shows object is about a PATO:*concentration of* [PATO_0000033]. Item **E** shows the concentration measured is of CHEBI:*chlorophyll a* [CHEBI_18230]. Item **F** shows the *chlorophyll a* is BFO:*part
of* [BFO_0000050] some ENVO:*sea water* [ENVO_00002149]. ](figures/data_annotation_diagram.png)


\pagebreak  
## 2.3 SPARQL querying

Scripts were written in Python (Version 2.7.12) [@python] and make use of the rdflib module (Version: 4.2.2) an RDF parsing python library [@team_rdflib] to parse the example RDF datastore, as well as assemble and execute SPARQL queries against the example datastore, or local RDF turtle serialization versions of local copies of ontologies. Additional SPARQL queries were preformed against the Ontobee programmatic SPARQL endpoint available from http://sparql.hegroup.org/sparql/ [@Ong2017]. A demonstration of the process by which a SPARQL query is executed is shown in **Figure 2**. Item **A** shows a SPARQL query, which is assembled in a python script based on some user input class (shown in green). This query selects some unknown thing called ?X (shown in red), where ?X is a subclass of some input class, and ?X is part of some class Y (shown in orange). Item **B** shows a knowledge graph of ontology terms and the relations connecting them. The knowledge graph could either be a local copy of an ontology such as ENVO or a
web accessible ontology knowledge graph such as the Ontobee programmatic SPARQL endpoint. Item **C** shows
how the SPARQL query navigates the relations in the knowledge graph to find a term which satisfies the input
conditions. Item **D** shows the successful retrieval of the ?X term, which was discovered from the knowledge
graph.

![**Figure 2** Shows a demonstration SPARQL query. In item **A** a SPARQL query is assembled. Item **B** represents a knowledge graph of ontology terms and their interconnecting relations. Item **C** shows the process by which the graph is navigated to find some ?X unknown item which is both a subclass of some input class and part of some Y. Item **D** Shows the end result of the query, returning the ?X class of interest having discovered it from the knowledge graph.](figures/query_illustration_full.jpg){width=80%}

\pagebreak
## 2.4 Interconnecting genomic and environmental data via ontologies

Retrieval of GO relative abundance data from ontology term annotated data was conducted using the script py.16. The script makes use of a list of benthic marine biome subclasses terms and a list of GO terms, which are subclasses of GO term of interest. Both subclasses lists were assembled using the script py.13. The script py.16 queries the local datastore for data matrices about an input list of annotation terms, for columns which annotated with GO terms matching an input list of ontology classes. The script makes use of the python Python Data Analysis Library (pandas) Version: 0.22.0 [@python_pandas]. The script returns a data table with rows corresponding to samples, and columns corresponding to relative abundances of GO terms. Relative abundances of metagenomic and metatranscriptomic samples were calculated by querying for subclasses of a GO term of interest, querying for all GO terms in the corresponding GO hierarchy, GO:*biological process* [GO_0008150] or GO:*molecular function* [GO_0003674], then dividing the relative abundances of individual terms by the sum of the total abundances of biological process or molecular function terms. Principal coordinate analysis (PCoA) on a data matrices of relative GO term abundances in ENVO annotated samples was conducted in R [@R_core] version 3.3.2, in the script R.4, which uses the vegan package [@vegan] version 2.4-3. Prior to PCoA analysis data was standardized using the decostand function making use of a Hellinger tranformation, then converted into a Bray-Curtis dissimilarity matrix using the vegdist function with standard parameters.


## 2.5 Ontology guided data assembly for ecological analysis

Subclasses of ontology terms included in the axioms of the hypothetical ENVO:*environment determined by a phytoplankton community associated with sea-ice* term, were assembled using the py.13 script, and concatenated together. Data annotated as being about this assembled list of subclasses terms was retrieved from the datastore using the py.5 script. In the script R.3 a principal component analysis (PCA) was performed on the retrieved data using the vegan package [@vegan] version 2.4-3. Prior to PCA analysis, data was z-score standardized using the scale function with parameters: *center* and *scale* being set to *TRUE*. The hypothetical term ENVO:*environment determined by a phytoplankton community associated with sea-ice* follows the design pattern of several preexisting terms in the Environment Ontology such as ENVO:*environment determined by a biofilm on a fungal surface* [ENVO_01001035] within the ENVO:*environmental system* [ENVO_01000254] hierarchy.


## 2.6 Connecting ontology term information with term authors

Percentages of ENVO and envoPolar ontology terms annotated with a IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation referencing an ORCID were calculated using the following workflow. Local turtle specification versions of the ENVO and envoPolar ontologies were exported using the standard Protégé [@Musen_2015][@protege] ``export as`` function. Python scrips py.7, py.9 and py.15 were used to SPARQL query the local turtle ontology versions, for total numbers of ENVO terms and numbers of terms annotated with an IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation an ORCID. Percentages of ontology terms with IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] annotations were calculated from retrieved counts.


## 2.7 Connecting datasets and publications about an ontology term

The following was used to retrieve digital object identifiers (DOIs) of publications associated with datasets about parts of a marine biome. The python script py.11 was used to query for ontology classes which are parts of or have parts which are an ENVO:*marine biome* [ENVO_00000447]. The resulting list of ontology terms which are parts associated with ENVO:*marine biome* [ENVO_00000447] were queried against the local datastore for all data from data matrix columns which are annotated with an oboInOwl:*hasDbXref* [hasDbXref] database cross reference using the py.6 python script. Results were processed in script R.1.

## 2.8 Glacial semantics community consultation

I had the opportunity to participate in a working group which was formed to propose visions for future modeling of glacial semantics. The Feb 2, 2018 VoCamp Glacier Ontology Hackathon [@vocamp_2018] was one of many Vocamp Hackathon events, in which working groups attempt to create lightweight vocabularies and ontologies for the semantic web [@vocamp_wiki]. My participation in this event served a means by which I could address the question:

> "To what extent are semantics knowledge models resilient to the addition of new or conflicting expert knowledge?"

While discussing the representation of knowledge about *ablation* processes the working group discovered there to be conflicting definitions. The Hackathon served as a method by which to apply the scientific method to semantic research. This was done through the collaborative efforts of Hackathon participants working to unpack and clarify the semantics of the term *ablation*. Such efforts made use of the conflicting semantics present within the NOAA National Weather Service Glossary 2009 [@nws_internet_services_team_glossary_2009] and Cogley et al. IACS-UNESCO Glacier Mass Balance 2011 [@cogley_glossary_2011] definitions of *ablation*. Where, according to the former definition only melting and evaporation processes contribute to *ablation*. The latter definition referred to all processes which reduce the mass of a glacier, specifically noting the inclusion of calving processes as significantly contributing to ablation processes. Differentia of the conflicting definitions was clarified by the proposal of additional semantics to represent the knowledge discrepancies.

## 2.9 classes linked by subclasses and subproperties

Retrieval of classes participating in subclasses of sea ice formation processes utilizing upper level semantic models was conducted as follows. Subclasses the term ENVO:*sea ice formation process* [ENVO_03000044] were assembled using the py.13 script. Subproperties of RO:*has participant* [RO_0000057] were assembled using the py.14 script. The results of classes which participate in sea ice formation processes, were discovered using the py.8 script with the assembled subclasses of ENVO:*sea ice formation process* [ENVO_03000044] and subproperties of RO:*has participant* [RO_0000057]. This workflow of querying for subclasses, subproperties and using them to search the knowledge graph for new classes of interest is documented in **Figure 3**.


![**Figure 3** Shows a demonstration of the workflow pertaining to script py.8. Item **A** shows an ontology knowledge graph, in this case the merged Ontobee programmatic SPARQL endpoint. In item **B** the py.13 script is executed to retrieve subclasses of an input class. In item **C** the py.14 script is executed to retrieve subproperties of an input property. In item **D** the py.8 script takes the list of subclasses generated in script py.13, the list of subproperties generated by script py.14. Searching the Ontobee knowledge graph script py.8 discovers new classes which are linked to subclasses of interest by the subproperties relations of interest.](figures/query_for_classes_linked_by_classes_and_properties.jpg)

This workflow was used to simulate what would happen if my example datastore didn't use the BFO and RO upper level semantic models. These simulations were evaluated for the extent to which annotated data would be retrieved by querying the example polar datastore in the absence of either BFO or RO. Lacking the RO the script py.13 was used to find subclasses of ENVO:*sea ice formation process* [ENVO_03000044], and the results of which were directly passed to script py.5 to get data about these subclasses, without using script py.8 using RO relations to discover new classes. The simulation for the retrieval of data lacking the BFO upper level semantic model was conducted using the same methods as the main workflow, minus the query for subclasses of ENVO:*sea ice formation process* [ENVO_03000044] with only the term itself passed to the py.8 script. The simulation for the retrieval of data lacking the Relations Ontology upper level semantic model was conducted without the py.8 script. In which the subclasses of ENVO:*sea ice formation process* [ENVO_03000044] from the py.13 script were directly passed to the py.5 script.

## 2.10 EnvoPolar network creation

The following was used to create a network from the ENVO polar subset. The envoPolar subset from the ENVO v2017-08-22 *Planetary ecology* release [@pier_luigi_buttigieg_2017_846451] was used. The envoPolar owl file was exported to the RDF specification turtle using the software Protégé's standard `export as` function [@Musen_2015][@protege]. Python script py.7 was used to query for all classes and python script py.12 was used to query for all property terms in the envoPolar subset. The results of which were used as inputs for the py.8 script to obtain the connections between all classes in the ontology. The resulting output consisting of subject classes, properties linking subject classes to target classes, and target classes, which was used to create a network in the program cytoscape [@Shannon_2003].  

Network parameters of the envoPolar subset of ENVO were calculated using the cytoscape network analyzer, treating the graph as directed. Figures for the distribution of shortest path lengths, average clustering coefficient, in degree distribution, out degree distribution, and betweenness centrality were generated in cytoscape.

Calculations of mean and median values for the in-degree, out-degree and shortest path length distributions were conducted in python the python script py.2 using the statistics library Version: 1.0.3.5 [@python_statistics] from distribution data output by the cytoscape network analysis. Figures of the in-degree, out-degree and shortest path length distributions were created in the R script R.1.

Nodes of highest and lowest in-degree value were extracted manually from the envoPolar network in cytoscape.

## 2.11 Predicted user data mobilization

In this thesis, I lacked the scope to be able to conduct an experiment on a study group of scientists with various proficiencies for performing semantic queries to retrieve data from the example datastore. In its place I estimated the performance of predicted user stories, as is done in agile software development [@user_story]. I created three categories of predicted user stories, for users of various SPARQL querying proficiencies. The predicted users were modeled to have basic, intermediate or advanced querying expertise. I evaluated the performance of these predicted user stories based on the percentage of total data each would be able to retrieve from our example datastore, when performing a variety of queries.

The basic user story was programed to only have a very limited understanding of how to perform SPARQL queries. The basic users were programed not to be able to perform queries of any axiomatic depth. They were limited to direct queries. The three querying cases basic users stores were programmed to execute are for 1) data about a class directly, 2) data about a class **and** other classes, 3) data about a class **or** other classes.

The intermediate user story was programed to be able to have moderate understanding of property path relationships and is  modeled to produce queries with a moderate amount of depth. For example queries about some class and *some property* another class.

The advanced user story was programmed to be able to have a fairly deep understanding of possible query paths.  For example queries about some class 1 and *some property* some class2, and  *another property* some class 3. Although the advanced user story can handle queries of sufficient, they were programmed to only make use of regular pattern. They were not programmed to handle all possible data annotation property path irregularities present in the model datastore.

Two user story experiments were modeled. The first for mobilizing data annotated with an exclusive *and* intersections of two ontology terms was conducted as follows. Eight combinations of terms were used to query for data. For each combination, the py.13 script was used to query for subclasses of the first term in the intersection combination. Modified versions of the py.10 script were run using the list of subclasses generated from the first term in the intersection combination, along with the second term. Retrieving data matrix annotations and columns annotated as being about the intersection of the subclasses of the first term with the second term.

The second user story experiments involved querying for data annotated as being about parts associated with an ontology term, was conducted as follows. Eight terms were queried for data annotated with parts associated therewith. For each term, the py.11 script was used to query for terms corresponding to associated parts of the input term. Modified versions of the py.10 script were run using the list of associated parts derived from the first script. Retrieving data matrices and data points annotated as being about parts associated with the input term.

For both user story experiments, percentages of retrieved data matrix columns, annotations, points and data matrices were calculated compared with the results derived from an unmodified version of the py.10 or py.11 scripts which retrieved 100% of available data. A list of querying cases used to differentiate the levels of querying expertise is available in the mobilizing ontology annotated data supplemental section.

\pagebreak  
# 3. Results

## 3.1 Leveraging interoperable GO and ENVO semantics

Making use of the interoperable Gene and Environment ontology semantics, I mobilized genomic and environmental data comparative analysis of various types of ENVO:*marine biome* [ENVO_00000447] samples.

I began by asking the competency question:

> What are the relative abundance frequencies of oxidation-reduction process genes in various types of marine biomes?

The results of querying the example datastore for the relative genomic and transcriptomic abundance of sequences matching GO:*oxidation-reduction process* [GO_0055114] genes, in various ENVO:*marine biome* [ENVO_00000447], are shown in **Table 1**.

: **Table 1** Shows the results of a query for the relative genomic and transcriptomic abundances of GO:*oxidation-reduction process* [GO_0055114] genes, in various ENVO:*marine biome*s [ENVO_00000447].

| term                                                                          | ENVO:*marine abyssal zone biome* [ENVO_01000027] | ENVO:*marine bathyal zone biome* [ENVO_01000026] | ENVO:*marine neritic benthic zone biome* [ENVO_01000025] |
|:------------------------------------------------------------------------------|:-------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------------|
| GO:*oxidation-reduction process* [GO_0055114]                                 | 18.15                                            | 18.39                                            | 9.36                                                     |
| GO:*aerobic respiration* [GO_0009060]                                         | 0.23                                             | 0.26                                             | 0.87                                                     |
| GO:*methanogenesis* [GO_0015948]                                              | 0.11                                             | 0.12                                             | 0.06                                                     |
| GO:*ATP synthesis coupled electron transport* [GO_0042773]                    | 0.06                                             | 0.06                                             | 0.04                                                     |
| GO:*L-lysine catabolic process to acetate* [GO_0019475]                       | 0.06                                             | 0.07                                             | 0.01                                                     |
| GO:*respiratory electron transport chain* [GO_0022904]                        | 0.03                                             | 0.03                                             | 0.13                                                     |
| GO:*mitochondrial electron transport, NADH to ubiquinone* [GO_0006120]        | 0.02                                             | 0.02                                             | 0.01                                                     |
| GO:*electron transport chain* [GO_0022900]                                    | 0.02                                             | 0.02                                             | 0.05                                                     |
| GO:*fatty acid beta-oxidation using acyl-CoA dehydrogenase* [GO_0033539]      | 0.02                                             | 0.02                                             | 0.01                                                     |
| GO:*anaerobic electron transport chain* [GO_0019645]                          | 0.01                                             | 0.01                                             | 0.00                                                     |
| GO:*glycogen biosynthetic process* [GO_0005978]                               | 0.00                                             | 0.00                                             | 0.01                                                     |
| GO:*aerobic electron transport chain* [GO_0019646]                            | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*methanogenesis, from acetate* [GO_0019385]                                | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*anaerobic glutamate catabolic process* [GO_0019670]                       | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*fatty acid beta-oxidation* [GO_0006635]                                   | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*photosynthetic electron transport in photosystem II* [GO_0009772]         | 0.00                                             | 0.00                                             | 16.08                                                    |
| GO:*heme oxidation* [GO_0006788]                                              | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*photosynthetic electron transport chain* [GO_0009767]                     | 0.00                                             | 0.00                                             | 1.38                                                     |
| GO:*mitochondrial electron transport, ubiquinol to cytochrome c* [GO_0006122] | 0.00                                             | 0.00                                             | 0.00                                                     |


Analysis of these results show deep biome samples ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026], had double the relative abundances of non-specific annotations to general oxidation-reduction reduction processes ~18%, relative to ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples. In contrast, ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples had three fold increases in GO:*aerobic respiration* [GO_0009060] gene abundances relative to the deep samples.

Deep samples had nearly double the GO:*methanogenesis* [GO_0015948] gene abundances than those of neritic samples, while neritic samples had much greater relative GO:*respiratory electron transport chain* [GO_0022904] abundances than deep samples.

Neritic samples had elevated abundances of photosynthetic related genes, 16% GO:*photosynthetic electron transport in photosystem II* [GO_0009772] genes and 1.4% GO:*photosynthetic electron transport chain* [GO_0009767] genes, contrasting with the 0.00% abundances of such genes in the deep benthic samples.  

Comparisons of GO:*vitamin biosynthetic process* [GO_0009110] genes of which are summarized in **Table 2**.

: **Table 2** Shows the relative abundance of GO:*vitamin biosynthetic process* [GO_0009110] genes in various types of ENVO:*marine benthic biomes* [ENVO_01000024].

| term                                                            | ENVO:*marine abyssal zone biome* [ENVO_01000027] | ENVO:*marine bathyal zone biome* [ENVO_01000026] | ENVO:*marine neritic benthic zone biome* [ENVO_01000025] |
|:----------------------------------------------------------------|:-------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------------|
| GO:*riboflavin biosynthetic process* [GO_0009231]               | 0.25                                             | 0.25                                             | 0.07                                                     |
| GO:*cobalamin biosynthetic process* [GO_0009236]                | 0.19                                             | 0.19                                             | 0.03                                                     |
| GO:*pantothenate biosynthetic process* [GO_0015940]             | 0.13                                             | 0.12                                             | 0.04                                                     |
| GO:*thiamine biosynthetic process* [GO_0009228]                 | 0.10                                             | 0.11                                             | 0.04                                                     |
| GO:*pyridoxine biosynthetic process* [GO_0008615]               | 0.10                                             | 0.09                                             | 0.02                                                     |
| GO:*vitamin B6 biosynthetic process* [GO_0042819]               | 0.05                                             | 0.05                                             | 0.02                                                     |
| GO:*pyridoxal phosphate biosynthetic process* [GO_0042823]      | 0.05                                             | 0.05                                             | 0.02                                                     |
| GO:*pyrroloquinoline quinone biosynthetic process* [GO_0018189] | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*anaerobic cobalamin biosynthetic process* [GO_0019251]      | 0.00                                             | 0.00                                             | 0.00                                                     |

From this table I noted that in the deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples, there is a general trend that relative gene abundance of GO:*vitamin biosynthetic process* [GO_0009110] genes are higher than the relative transcriptomic abundance of ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples. For example the relative gene abundance of GO:*riboflavin biosynthetic process* [GO_0009231] genes was approximately 3.5 times greater in deep biome sample genomes than neritic sample transcriptomes.

These results prompted me to ask the question:

> What genomic features may help to explain the differences in riboflavin abundances between deep and shallow marine benthic biomes?

To investigate other genomic features which may help to explain the differences in riboflavin abundance, we investigated GO:*transition metal ion binding* [GO_0046914] and GO:*transition metal ion transport* [GO_0000041] subclasses. As flavins have been implicated as electron donors in the reduction of insoluble ferric to soluble ferrous iron as well as the transport of ferrous to the cytoplasm [@Crossley_2007][@Fuller_2013]. For full results of relative abundances of metal ion binding, and metal ion transport subclasses see **Tables A1** and **A2**. Querying for subclasses of GO:*transition metal ion binding* [GO_0046914] we found that GO:*ferrous iron binding* [GO_0008198] gene abundance is 0.02-0.03% in deep samples vs 0.00% in neretic. Furthermore deep sample GO:*ferrous iron transport* [GO_0015684] gene abundance is double that of neritic sample, 0.04% vs 0.02%.


I next investigated the question of:

> "What biological processes differentiate various types of marine benthic biomes?"

Results of this investigation into GO:biological process [GO_0008150] differentiating marine benthic samples are as follows. A PcoA analysis was conducted on all the subclasses of GO:biological process [GO_0008150] found in various ENVO:*marine benthic biomes* [ENVO_01000024]. The results of which are shown in **Figure 4** which shows the relative gene and transcript abundances of datasets annotated as various types of ENVO:*marine benthic biomes* [ENVO_01000024]. Together PcoA axes explain 97.9% of the total variance, with axis 1 explaining 96.1% and axis 2 explaining 1.8%. From the figure we see a differentiation between ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples from those of ENVO:*marine neritic benthic zone biome*s [ENVO_01000025]. We see deep samples ordinated toward the positive values of PcoA dimension 1, and shallow samples toward negative PcoA dimension 1 values.

![**Figure 4** shows a principal coordinate analyses plot of relative genomic abundance of subclasses of GO:biological process [GO_0008150] terms in various marine benthic biomes. ](figures/all_biological_processes.png){ width=80% }

**Table 3** shows the results of classes contributing the most to positive loadings of PcoA dimension 1. Such classes include GO:*Actinobacterium-type cell wall biogenesis* [GO_0071766], GO:*phosphate ion transmembrane transport* [GO_0035435] and GO:*siderophore biosynthetic process* [GO_0019290] contributed toward positive values of PcoA dimension 1.

: **Table 3** Shows the top ten biological process terms contributing to positive PcoA dimension 1 loadings in ascending order.

| term                                                                 | PcoA dimension 1 loading |
|:---------------------------------------------------------------------|:-------------------------|
| GO:*Actinobacterium-type cell wall biogenesis* [GO_0071766]          | 0.2446046073             |
| GO:*fusion of virus membrane with host plasma membrane* [GO_0019064] | 0.2446046073             |
| GO:*nicotianamine biosynthetic process* [GO_0030418]                 | 0.2446046073             |
| GO:*phosphate ion transmembrane transport* [GO_0035435]              | 0.2439406864             |
| GO:*viral transcription* [GO_0019083]                                | 0.2426128446             |
| GO:*cell wall biogenesis* [GO_0042546]                               | 0.2420637463             |
| GO:*response to auxin* [GO_0009733]                                  | 0.2416976809             |
| GO:*organomercury catabolic process* [GO_0046413]                    | 0.241307236              |
| GO:*regulation of viral transcription* [GO_0046782]                  | 0.2407945711             |
| GO:*carbohydrate utilization* [GO_0009758]                           | 0.2402975311             |
| GO:*siderophore biosynthetic process* [GO_0019290]                   | 0.2401357557             |


**Table 4** Shows the results of classes contributing the most to negative loadings of PcoA dimension 1. Such classes include: GO:*activation of innate immune response* [GO_0002218], GO:*mRNA transport* [GO_0051028], and GO:*mitochondrial respiratory chain complex IV assembly* [GO_0033617].

: **Table 4** Shows the ten lowest contributing terms to PcoA dimension 1 in descending order.

| term                                                                           | PcoA dimension 1 loading |
|:-------------------------------------------------------------------------------|:-------------------------|
| GO:*activation of innate immune response* [GO_0002218]                         | -0.3143688463            |
| GO:*positive regulation of type I interferon production* [GO_0032481]          | -0.3143688463            |
| GO:*endoplasmic reticulum organization* [GO_0007029]                           | -0.3143688463            |
| GO:*macromolecule biosynthetic process* [GO_0009059]                           | -0.3143688463            |
| GO:*mRNA transport* [GO_0051028]                                               | -0.3143688463            |
| GO:*chemical synaptic transmission* [GO_0007268]                               | -0.3143688463            |
| GO:*prosthetic group biosynthetic process* [GO_0051191]                        | -0.3143688463            |
| GO:*porphyrin-containing compound metabolic process* [GO_0006778]              | -0.3143688463            |
| GO:*mitochondrial respiratory chain complex IV assembly* [GO_0033617]          | -0.3143688463            |
| GO:*regulation of microtubule polymerization or depolymerization* [GO_0031110] | -0.3033210212            |



Using the GO biological processes hierarchy, shown in **Figure A2**, to find drill down to a more specific term by which to investigate the differentiation of these environmental omic data I asked the question:

> "What cellular amino acid biosynthetic processes differentiate various types of marine benthic biomes?"

I performed another PcoA analysis this time on the subclasses of GO:*cellular amino acid biosynthetic process* [GO_0008652]. The results of which are shown in **Figure 5**. Here we can more clearly see classes which separate deep and shallow biome samples. Together the first two PcoA axes explain 94.2% or total variance, with axis 1 explaining 81.7 and axis 2 12.5%.

![**Figure 5** Principal coordinate analyses plot of relative genomic abundance of subclasses of GO:*cellular amino acid biosynthetic process*es [GO_0008652] in various ENVO:*marine benthic biomes* [ENVO_01000024]. ](figures/cellular_amino_acid_biosynthetic_process.png){ width=80% }


: **Table 5** Shows the GO classes which contributed positive PcoA dimension 1 loadings to a PcoA analysis conducted on the subclasses of GO:*cellular amino acid biosynthetic process* [GO_0008652].

| term                                                             | PcoA dimension 1 loading |
|:-----------------------------------------------------------------|:-------------------------|
| GO:*alanine biosynthetic process* [GO_0006523]                   | 0.0854066743             |
| GO:*glutamine biosynthetic process* [GO_0006542]                 | 0.0823866518             |
| GO:*branched-chain amino acid biosynthetic process* [GO_0009082] | 0.0542505889             |
| GO:*cysteine biosynthetic process from serine* [GO_0006535]      | 0.0258920233             |

Contributing to positive PcoA dimension 1 loadings were the GO classes for alanine, glutamine, and cysteine biosynthetic processes.


: **Table 6** Shows the GO classes which contributed negative PcoA dimension 1 loadings to a PcoA analysis conducted on the subclasses of GO:*cellular amino acid biosynthetic process* [GO_0008652].

| term                                                                                                              | PcoA dimension 1 loading |
|:------------------------------------------------------------------------------------------------------------------|:-------------------------|
| GO:*methionine biosynthetic process* [GO_0009086]                                                                 | -0.0547399653            |
| GO:*L-phenylalanine biosynthetic process* [GO_0009094]                                                            | -0.0509995711            |
| GO:*L-methionine biosynthetic process from homoserine via O-succinyl-L-homoserine and cystathionine* [GO_0019281] | -0.0446167137            |
| GO:*glycine biosynthetic process* [GO_0006545]                                                                    | -0.0422156338            |
| GO:*lysine biosynthetic process via diaminopimelate* [GO_0009089]                                                 | -0.0395103024            |
| GO:*tyrosine biosynthetic process* [GO_0006571]                                                                   | -0.0353511626            |
| GO:*glutamate biosynthetic process* [GO_0006537]                                                                  | -0.0297865334            |
| GO:*asparagine biosynthetic process* [GO_0006529]                                                                 | -0.0267125372            |
| GO:*histidine biosynthetic process* [GO_0000105]                                                                  | -0.02663144              |
| GO:*aromatic amino acid family biosynthetic process* [GO_0009073]                                                 | -0.024977886             |
| GO:*arginine biosynthetic process* [GO_0006526]                                                                   | -0.020751455             |
| GO:*cellular amino acid biosynthetic process* [GO_0008652]                                                        | -0.0175536448            |
| GO:*leucine biosynthetic process* [GO_0009098]                                                                    | -0.0134594056            |

Contributing to negative PcoA dimension 1 loadings were the GO classes such as those for methionine, phenylalanine and glycine biosynthetic processes.

Examining the GO hierarchy for subclasses of cellular amino acid biosynthetic process, shown in **Figure A2**, we can drill down into even more specific terms further differentiate the benthic biome annotated samples. I noted from this analysis that the term GO:*cysteine biosynthetic process from serine* [GO_0006535], ordinates along the positive side of PcoA axis 1, in close proximity with the ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples.

I further investigated the differences between between subclasses of GO:*serine family amino acid biosynthetic processes* [GO_0009070]. The results of which are shown in **Figure 6**. In this analysis, PcoA axis 1 explains 100% of the variance. From this PcoA analysis of subclasses of GO:*serine family amino acid biosynthetic processes* [GO_0009070] we see a clear differentiation of neritic vs deep benthic biome samples. From this plot we learn that the relative gene abundance of GO:*glycine biosynthetic process*es [GO_0006545] is more abundant in the deep samples, while GO:*cysteine biosynthetic process from serine* [GO_0006535] are more abundant in the neretic samples.

![**Figure 6** shows a principal coordinate analyses of relative genomic abundance of subclasses of GO:*serine family amino acid biosynthetic processes* [GO_0009070] in various ENVO:*marine benthic biomes* [ENVO_01000024]. ](figures/serine_family_amino_acid_biosynthetic_process.png){ width=80% }


\lstset{language=}


\pagebreak

## 3.2 Numerical ecology analysis

To assess if ontologies are fit to assemble information upon which to perform an ecology analysis, I asked the following question:

> What environmental factors have the greatest influence on the dynamics of a sea-ice associated phytoplankton community?"

To demonstrate how the processes of using ontologies to retrieve data about a phenomena of interest would unfold. I first define the hypothetical term ENVO:*environment determined by a phytoplankton community associated with sea-ice*. I defined this term as:

> An environmental system which has its properties and dynamics determined by a phytoplankton community which is associated with sea-ice.

This hypothetical term would include the following subclass axioms: ENVO:*environmental system determined by a community* [URI pending], ENVO:*determined by* [ENVO_2100001] some PCO:*phytoplankton community* [URI pending], RO:*located in* [RO_0001025] some (ENVO:seawater* [ENVO_00002149] and (RO:*part of* [BFO_0000050] some ENVO:*marine water body* [ENVO_00001999])), and finally RO:*adjacent to* [RO_0002220] some ENVO:*sea ice* [ENVO_00002200].

By leveraging data annotated with terms which are included as axioms, I was able to assemble data upon which to perform an ecological analysis. I first assembled a list of all the classes (and subclasses thereof) which are referenced by the axioms of this hypothetical term. Then I queried the example datastore for data about these terms. Note that the following ecological analysis makes use of artificially assembled data, as the data are from different spatiotemporal locations. Next we performed a principal component analysis on this data to investigate which of these many environmental variables have the greatest loading on the analysis. **Figure 7** shows a hypothetical principal component analysis showing the effects of the various environmental variables, assembled due to their inclusion in axioms of the term ENVO:*environment determined by a phytoplankton community associated with sea-ice*. 53.6% of variance was explained in this analysis with PCA axis 1 explaining 34.0% of variance and PCA axis 2 explaining 19.6% of variance.

![**Figure 7** PCA on assembly of data about terms included as axioms of a hypothetical ENVO:*environment determined by a phytoplankton community associated with sea-ice* term.](figures/assemble_data_for_ ecological_analysis.jpeg){ width=90% }

Included in **Figure 7** are the Environment Ontology terms which were were referenced as axioms of the hypothetical ENVO:*environment determined by a phytoplankton community associated with sea-ice* term, and from which annotated data was retrieved. For example *SignalStrength_ENVO_00002200* represents a column which is labeled *Signal Strength* which is about a PATO:*degree of illumination* [PATO_0015013] which RO:*inheres in* [RO_0000052] some ENVO:*sea ice* [ENVO_00002200].

: **Table 7** Shows the loadings from principal components 1 and 2 from the PCA conducted on data assembled due it being annotated with ontology term included in the subclass axioms of a hypothetical ENVO:*environment determined by a phytoplankton community associated with sea ice* ontology term. Terms are ordered in descending order based on PC 1 then PC 2. The interpretation of the first data column is that it is a data column about the PATO:*concentration of* [PATO_0000033] CHEBI:*phosphate* [CHEBI_26020] in ENVO:*sea water* [ENVO_00002149].

| data columns            | annotation term                      | PC1 loading | PC2 loading |
|:------------------------|:-------------------------------------|:------------|:------------|
| phosphate               | ENVO:*sea water* [ENVO_00002149]     | 1.22009153  | 0.09015633  |
| nitrate                 | ENVO:*sea water* [ENVO_00002149]     | 1.21200068  | 0.01720033  |
| ice or snow temperature | ENVO:*multiyear ice* [ENVO_03000073] | 0.58457003  | 0.82623573  |
| sea ice thickness       | ENVO:*sea ice* [ENVO_00002200]       | 0.52555148  | -0.48198612 |
| signal strength         | ENVO:*sea ice* [ENVO_00002200]       | 0.24304142  | -0.80299701 |
| oxygen                  | ENVO:*sea water* [ENVO_00002149]     | -0.01611319 | 0.87287456  |
| salinity                | ENVO:*sea water* [ENVO_00002149]     | -0.70229106 | 0.21544285  |

Example results of this hypothetical analysis are that ENVO:*sea water* [ENVO_00002149] CHEBI:*phosphate* [CHEBI_26020] and CHEBI:*nitrate* [CHEBI_17632] concentrations have positive PC1 loading values. ENVO:*sea water* [ENVO_00002149] CHEBI:*dioxygen* [CHEBI_15379] and CHEBI:*salinity* [URI pending] have negative PC1 loading values. ENVO:*sea ice* [ENVO_00002200] PATO:*thickness* [PATO_0000915], and signal strength PATO:*degree of illumination* [PATO_0015013] which RO:*inheres in* [RO_0000052] some ENVO:*sea ice* [ENVO_00002200] have negative PC2 loading values.


\pagebreak
## 3.3 Identifying term author provenance

The following questions address if ontologies are fit for purpose to identify the provenance of ontology term authors:

> "How well do the Environment Ontology and the Environment Ontology Polar subset connect authors of terms to the information they helped to encode?"

To evaluate such a question, I performed queries to calculate the proportions of ENVO and envoPolar terms which are annotated with an IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation which reference an ORCID. ORCID is a unique identifier for scientific and other academic authors and contributors [@ORCID_2009]. The results of this analysis are summarized in the **Table 8**.

: **Table 8** Shows the percentage of ENVO and envoPolar terms annotated with a "term editor" or "created_by" relation.

| ontology  | % terms with oboInOwl:*created_by* [created_by] | % terms with IAO:*term editor* [IAO_0000117] |
|:----------|:------------------------------------------------|:---------------------------------------------|
| ENVO      | 14.5                                            | 4.2                                          |
| envoPolar | 17.2                                            | 31.4                                         |


Examining these results we find that in the full Environment Ontology only 4.2% of terms have an IAO:*term editor* [IAO_0000117] annotation, contrasting with the 31.4% of terms from the Environment Ontology polar subset.

Terms related by an oboInOwl:*created_by* [created_by] relation only account for 14.5% of ENVO terms, wheres they are found in 17.2% of terms from the envoPolar subset.

Altogether only approximately 20% of Envo terms are annotated with a IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation, contrasting with the nearly 50% referenced terms from the envoPolar subset.

\pagebreak

## 3.4 Retrieving primary literature via nodes in a knowledge graph

Assessing if ontologies could serve to connect users to primary literature associated with datasets annotated with ontology term, I asked the question:

> "What are all the papers which reference any data set, which is about a part of a marine biome?"

The results of this question were as follows. In the example datastore there are two datasets which are annotated with a terms which satisfy the condition of being part of an ENVO:*marine biome* [ENVO_00000447]: *Global chlorophyll "a" concentrations for diatoms, haptophytes and prokaryotes obtained with the Diagnostic Pigment Analysis of HPLC data compiled from several databases and individual cruises.* [@soppa2017gcac][@Losa_2017], and *Influence of snow depth and surface flooding on light transmission through Antarctic pack ice, supplementary data.* [@arndt2017iosd][@Arndt_2017]. Both of which are about an ENVO:*marine water body* [ENVO_00001999]. Returned are the Digital object identifier (DOI) persistent uniform resource locators for the 14 publications which make use of these two example AWI datasets. For a full list see **Table A3**. Selected example results of publications their digital object identifiers as well as the dataset from which the publications were retrieved are shown in **Table 9**. Retrieved publications about variety of ENVO:*marine water body* [ENVO_00001999] related topics, including using chlorophyll pigments to determine phytoplankton taxonomy, plankton ecology, vertical distributions of phytoplankton communities and light transmission through pack-ice.

: **Table 9** Selected examples of digital object identifiers of publications obtained querying for references of datasets which are about BFO:*part of* [BFO_0000050] a ENVO:*marine biome* [ENVO_00000447].  

+---------------+----------------------------+------------------------+
|data set       |reference doi               | reference title        |
+===============+============================+========================+
|global        \|10.1016/j.dsr.2011.01.008   |An evaluation of the application\|
|chlorophyll a \|                            |of CHEMTAX to Antarctic coastal\|
|              \|                            |pigment data [@Kozlowski_2011]\|
+---------------+----------------------------+------------------------+
|               |10.3402/polar.v34.23349     |Summertime plankton ecology\|
|               |                            |in Fram Strait-a compilation\|
|               |                            |of long- and short-term \|
|               |                            |observations [@N_thig_2015] \|
+---------------+----------------------------+------------------------+
|               |10.1029/2005JC003207        |Vertical distribution of \|
|               |                            |phytoplankton communities \|
|               |                            |in open ocean: An assessment\|
|               |                            |based on surface chlorophyll [@Uitz_2006] \|
+---------------+----------------------------+------------------------+
|influence snow\|10.1002/2016JC012325        |Influence of snow depth and \|
|depth         \|                            |surface flooding on light\|
|              \|                            |transmission through Antarctic \|
|               |                            |pack ice [@Arndt_2017] \|
+---------------+----------------------------+------------------------+


## 3.5 Necessity of top level semantic models

We addressed the necessity of using both the Basic Formal Ontology and Relations ontology upper level semantic models in order to interconnect the semantically annotated contents of the example datastore.

Data annotated with unspecified ontology terms were discovered by querying the OBO knowledge graph for classes related to an input class via an input property. In this example, we queried for classes which participate in a sea ice formation process. Shown in **Table 10**, are the results of searching the knowledge graph for subclasses of sea ice formation processes (shown in the first column), related classes (third column), properties linking the subclasses to the related classes (second column), and the number of data items retrieved from the datastore annotated as being about the related class.

: **Table 10** Number of data items in datastore about classes which participate in sea ice formation processes

| input class                                             | property                       | related class                          | number of data items |
|:--------------------------------------------------------|:-------------------------------|:---------------------------------------|:---------------------|
| ENVO:*sea ice formation process* [ENVO_03000044]        | ENVO:*has input* [RO_0002233]  | ENVO:*sea water* [ENVO_01000321]       | 13                   |
| ENVO:*sea ice formation process* [ENVO_03000044]        | ENVO:*has output* [RO_0002234] | ENVO:*sea ice* [ENVO_03000066]         | 6                    |
| ENVO:*nilas formation process* [ENVO_03000058]          | ENVO:*has input* [RO_0002233]  | ENVO:*new ice* [ENVO_03000063]         | 0                    |
| ENVO:*nilas formation process* [ENVO_03000058]          | ENVO:*has output* [RO_0002234] | ENVO:*nilas* [ENVO_03000068]           | 0                    |
| ENVO:*young ice formation process* [ENVO_03000059]      | ENVO:*has output* [RO_0002234] | ENVO:*young ice* [ENVO_03000069]       | 0                    |
| ENVO:*first year ice formation process* [ENVO_03000060] | ENVO:*has output* [RO_0002234] | ENVO:*first year ice* [ENVO_03000071]  | 8                    |
| ENVO:*second year ice formation* [ENVO_03000061]        | ENVO:*has output* [RO_0002234] | ENVO:*second year ice* [ENVO_03000072] | 0                    |
| ENVO:*multiyear ice formation process* [ENVO_03000062]  | ENVO:*has output* [RO_0002234] | ENVO:*multiyear ice* [ENVO_03000073]   | 8                    |

The results of a simulation conducted to evaluate the extent to which the Basic Formal Ontology and Relations Ontology upper level semantic models are necessary in the retrieval of annotated data, are presented in **Table 11**. Lacking the Basic Formal Ontology upper level semantic model, only 54.3% of the data items were retrieved. Lacking the Relations Ontology upper level semantic model 0% of the relevant data could be retrieved.

: **Table 11** Percentages of data items in datastore about classes which participate in sea ice formation processes retrieved when lacking upper level semantic models.

+-----------------------------------+------------------------+
|lacking upper level semantic model |% data items retrieved  |
+===================================+========================+
| Basic Formal Ontology             | 54.3                   |
+-----------------------------------+------------------------+
| Relations Ontology                | 0                      |
+-----------------------------------+------------------------+

## 3.6 Analysis of polar knowledge graph

Treating connectivity within a network created from an ontology knowledge graph as a proxy for the extent to which ontologies connect researchers to new unspecified knowledge. I analyzed the envoPolar subset as a network. The resulting network property statistics are summarized as follows. The average degree, the number of edges corresponding to each node, is 1.517. The distributions of in-degree values, edges pointing into a node, and out-degree, edges leading away from a node are shown in **Figures A3**, and **A4**. The average in-degree distribution shows a positive skew with a median of 0 relative to the mean degree of 1.517, with a very wide range of in-degree values from 0 to 44. The average out-degree distribution also shows a positive skew with a median of 1 relative to the mean degree of 1.517, however, the out-degree values only range from 0 to 5. Additional network parameters are summarized in **Table 12**.

: **Table 12** Network parameters calculated from the graph of the envoPolar subset of ENVO.

+--------------------------------------------+-------+
| network parameter                          | value |
+============================================+=======+
| number of nodes                            | 265   |
+--------------------------------------------+-------+
| number of edges                            | 402   |
+--------------------------------------------+-------+
| average node degree                        | 1.517 |
+--------------------------------------------+-------+
| clustering coefficient                     | 0.047 |
+--------------------------------------------+-------+
| connected components                       | 8     |
+--------------------------------------------+-------+
| network diameter                           | 7     |
+--------------------------------------------+-------+
| mean shortest path length                  | 2.246 |
+--------------------------------------------+-------+
| average connectivity (number of neighbors) | 2.875 |
+--------------------------------------------+-------+
| network density                            | 0.0   |
+--------------------------------------------+-------+
| number of self-loops                       | 0     |
+--------------------------------------------+-------+
| multi-edge node pairs                      | 20    |
+--------------------------------------------+-------+

The graph of the envoPolar subset include 265 classes represented as nodes with a total 402 connections (edges) interconnecting them. It is made up of 8 components, clusters of internally but not externally connected nodes and edges. The network diameter, the maximum distance path between two nodes, is 7. The network density, measuring how densely the network is populated with edges is 0.0. There are no self-loops, nodes with edges connecting back to themselves. There are 20 multi-edge node pairs, which measure how often neighboring nodes are linked by more than one edge.

Analysis of the distribution of shortest path lengths, the expected distance between two connected nodes is as follows. The mean shortest path length, is 2.246, and the distribution of shortest path lengths, **Figure 8**, shows a positive skew with the median shortest path length being 2.0, a value less than that of the mean.  

![**Figure 8** Distribution of shortest path lengths of the envoPolar subset analyzed as a network.](figures/shortest_path_length_distribution.jpeg){ width=80% }

The average connectivity or average number of neighbors, indicating the expected number of vertices that would need to be removed to separate any randomly chosen pair of vertices is 2.875. The clustering coefficient, a measure of the extent to which nodes in a graph tend to cluster together bounded on a scale from 0 to 1, zero being unconnected and 1 being completely connected is 0.047. Plotting the average cluster coefficients as a function of number of neighbors, see **Figure 9**, I observe two distinct clusters of nodes. Nodes either have a high average clustering coefficient and a small number of neighbors, or they have a low clustering coefficient and a large number of neighbors.

![**Figure 9** Average clustering coefficient as a function of number of neighboring nodes in the envoPolar subset analyzed as a network.](figures/average_clustering_coefficient.jpeg){ width=70% }

Finally I analyzed the betweenness centrality of nodes in the envoPolar network, see **Figure A5**. Betweenness centrality of a node is a value ranging between 0 and 1, which reflects the amount of control this node exerts over the interactions of other nodes. Plotting betweenness centrality as a function of number of neighboring nodes we find only 3 nodes with non-zero betweenness centrality values, all of which have only 2 neighboring nodes. The rest of the nodes have a betweenness centrality of near zero, regardless of the number of neighbors.


: **Table 13** Top ten largest in-degree value terms for polar related terminology from the envoPolar subset.

| term                                              | in degree |
|:--------------------------------------------------|:----------|
| ENVO:*water ice* [ENVO_01000277]                  | 24        |
| ENVO:*glacier* [ENVO_00000133]                    | 19        |
| ENVO:*snow* [ENVO_01000406]                       | 10        |
| ENVO:*ice mass* [ENVO_01000293]                   | 10        |
| ENVO:*powdery snow* [ENVO_03000027]               | 6         |
| ENVO:*glacial erosion process* [ENVO_03000006]    | 4         |
| ENVO:*permafrost* [ENVO_00000134]                 | 4         |
| ENVO:*frazil ice* [ENVO_03000046]                 | 4         |
| ENVO:*glacial ice* [ENVO_03000004]                | 3         |
| ENVO:*permafrost thawing process* [ENVO_03000086] | 3         |

From the results presented in **Table 13** and **14** showing the nodes with the highest and lowest in-degree values, I observed that there are very few nodes of substantial in-degree values. The distribution of in-degree drops off very rapidly with only a few nodes such as ENVO:*water ice* [ENVO_01000277], ENVO:*glacier* [ENVO_00000133], and ENVO:*snow* [ENVO_01000406] having high in-connectivity values. Even within the top ten in-degree nodes the value decrease substantially from ENVO:*water ice* with 24 in connections, to ENVO:*permafrost thawing process* [ENVO_03000086] with only 3 interconnections. From **Table 14** we see that many of the nodes have in-degrees of 0.


\pagebreak
: **Table 14** Bottom ten smallest in-degree value terms for polar related terminology from the envoPolar subset.

| term                                            | in degree |
|:------------------------------------------------|:----------|
| ENVO:*ice field* [ENVO_00000299]                | 0         |
| ENVO:*shuga formation process* [ENVO_03000079]  | 0         |
| ENVO:*erosion through nivation* [ENVO_03000121] | 0         |
| ENVO:*pingo* [ENVO_00000413]                    | 0         |
| ENVO:*ice cap dome* [ENVO_00000342]             | 0         |
| ENVO:*ice tongue* [ENVO_00000392]               | 0         |
| ENVO:*sea ice floe* [ENVO_03000066]             | 0         |
| ENVO:*snowpack* [ENVO_03000116]                 | 0         |
| ENVO:*ice cap ridge* [ENVO_00000528]            | 0         |
| ENVO:*perennial snow patch* [ENVO_03000115]     | 0         |

\newpage
## 3.7 Feasible semantic data annotations

Assessing the practicality of retrieving ontology term annotated data from the example data store, we evaluated the relative amount of data which would be retrieved by estimated user stories programmed to estimate users of various levels of querying expertise. Estimating the retrieval rates of data for users of the system with basic, intermediate and advanced querying expertise.

Two estimated user story querying proficiency experiments were conducted, the first queried for data which was about the exclusive *and* intersection of two annotation terms, for example data about *snow and thickness*. The second experiment queried for data which is about a part of an input term, for example, *part of a glacier*. The results of the first experiment, displaying the percentages of annotation terms and data matrix columns retrieved about the intersection of two terms, are presented in **Figure 10**.

![**Figure 10** Analysis of querying expertise required to obtain data matrix columns and annotations when querying for data about subclasses of a term AND another term.](figures/query_and_annotation_columns_number.jpeg){ width=80% }

User stories estimating basic querying expertise were only able to retrieve data and annotations from the *Bacteria and Archaea* case. User stories estimating intermediate querying expertise were only able to retrieve data from 4 out of the 8 cases tested. Excluding the *Bacteria and Archaea* cases which were covered with 100% success by all three expertise classes, the percentage of annotations retrieved by intermediate user stories ranged from 40-66.7%, whereas the percentage of data columns retrieved ranged from 50-80%. Advanced user stories were able to retrieve data columns and annotations from all 8 of the tested querying cases, with successes ranging from 57.1% to 100% of annotations and 66.7% to 100% of data matrix columns.

The results of the second experiment, displaying the percentages of data matrices and data points retrieved from BFO:*part of* [BFO_0000050] input terms are presented in **Figure 11**. Basic user stories were only able to retrieve data matrices from the  *parts of a marine biome* case, as well as data points from the *part of a centrally registered identifier symbol* case. In terms of the success rates of retrieving data matrices about *parts of a marine biome*, the basic user story expertise case retrieved 25%, the intermediate case retrieved 75% and advanced case retrieved 100%. Intermediate expertise user stories were only able to retrieve data points from 4 out of the 8 *parts of cases*. Although advanced user stories were able to retrieve data points from the majority of *parts of* query cases, they were unable to retrieve any from the *parts of a carbon atom* cases, and they were only able to retrieve 82.3% of data which is *part of a glacier*, and 94.9% of data annotated with an ontology term which is *part of an ocean*.

![**Figure 11** Analysis of querying expertise required to obtain data matrices and data points when querying for data about parts associated with  an ontology term.](figures/query_parts_of_stats.jpeg){ width=80% }

\newpage

## 3.8 Identifying phenomenal interconnections

Attempting to build upon the semantic framework proposed as necessary by Stec et al. (2017), for future modeling of plankton ecosystems [@Stec_2017]. Asking the question:

> "Does the inclusion of novel expert knowledge about phenomena relating to plankton ecology into the ENVO knowledge graph aid to better understand the interconnections of such phenomena?"

To answer this question I proposed the following plankton ecology related ontology term to the ENVO [@Buttigieg_2013][@Buttigieg_2016] PATO [@PATO_BioPortal] ECOCORE [@ecocore_2018] and PCO [@PCO__BioPortal] ontologies. A complete description of these potential ontology terms, are available from the following URL: https://github.com/kaiiam/kblumberg_masters_thesis/wiki/plankton-ecology

An example of a term prepared for the Population and Community Ontology is PCO:*phytoplankton bloom process* which I have defined as:

> A plankton bloom process during which at least two of the populations in a community of phytoplankton, in a body of water, undergo rapid growth, resulting in high concentrations of phytoplankton that occur only periodically and briefly in that ecosystem, relative to their concentrations through the majority of the planetary orbital period.

I proposed for this PCO:*phytoplankton bloom process* term to have a variety of subclass axioms, which include other proposed PCO and ECOCORE terms. The subclass axioms I’ve proposed include: PCO:*plankton bloom process* [URI pending], RO:*has participant* [RO_0000057] some PCO:*phytoplankton community* [URI pending], BFO:*part of* [BFO_0000050] some ECOCORE:*surface photoautotrophic biomass formation* [URI pending], BFO:*has part* [BFO_0000051] some PCO:*population bloom* [URI pending], BFO:*occurs in* [BFO_0000066] some ENVO:*water body* [ENVO_00000063], and finally an oboInOwl:*database_cross_reference* [hasDbXref] https://en.wikipedia.org/wiki/Phytoplankton.

An example of a term prepared for the Phenotypic Quality Ontology is PATO:*planktonic*, which I have defined as:

> An organismal quality inhering in a bearer by virtue of the bearer’s inability to sustain directed movement to overcome displacement by physical forces such as currents.

This definition encodes the classic oceanography definition of plankton into the ontology knowledge graph, characterizing planktonic organisms as drifting organisms unable to swim against a current [@lalli1997biological]. I proposed this planktonic class to be a subclass of PATO:*organismal quality* [PATO_0001995], and for it to include the oboInOwl:*database_cross_reference* [hasDbXref] https://en.wikipedia.org/wiki/Phytoplankton.

Another term I propose to be added to PATO is PATO:*ice cover of a planetary surface*, which I define as:

> A physical quality which inheres in a land or water body by virtue of that land or water body having a two dimensional surface layer whose connection to some adjacent atmosphere or outer space is interrupted by ice.

This class has the following proposed subclasses: PATO:*physical quality* [PATO_0001018], RO:*inheres in* [RO_0000052] some ENVO:*planetary surface* [ENVO_01000324] or ENVO:*water body* [ENVO_00000063], BFO:*has part* [BFO_0000051] some ENVO:*surface layer* [ENVO_00010504] and (RO:*adjacent to* [RO_0002220] some ENVO:*atmosphere [ENVO_01000267] or ENVO:*outer space [ENVO_01000637]), RO:*adjacent to* [RO_0002220] some ENVO:*water ice* [ENVO_01000846], finally having oboInOwl:*exact synonym* [hasExactSynonym] *ice cover* and *ice coverage*.

I also prepared many terms for ENVO. For example the term ENVO:*marginal ice zone*, which I defined as:

> An environmental zone in which is the site of the transition between the open ocean and sea ice.

This term includes the subclass axioms: ENVO:*environmental zone* [ENVO_01000408], RO:*has quality* [RO_0000086] some PATO:*ice cover of a planetary surface* [URI pending], RO:*overlaps* [RO_0002131] some (ENVO:*sea ice* [ENVO_03000066] and ENVO:*marine water body* [ENVO_00001999]), RO:*causally upstream of, positive effect* [RO_0002304] some PCO:*phytoplankton bloom process* [URI pending], RO:*causally upstream of, positive effect* [RO_0002304] some ECOCORE:*photoautotrophic biomass formation* [URI pending], oboInOwl:*has related synonym* [hasRelatedSynonym] *sea ice edge*, with oboInOwl:*database_cross_reference*s [hasDbXref] http://www.npolar.no/en/facts/the-marginal-ice-zone.html
and https://doi.org/10.1016/j.jmarsys.2013.11.008 [@Cherkasheva_2014].

For ENVO I also propose the term ENVO:*marine environment determined by a phytoplankton community bloom*, which I define as:

> A marine environmental system which has a phytoplankton community bloom as part, such that the rapid growth of at least two of the populations in a blooming community of phytoplankton, exert a strong causal influence on the function of the marine environmental system, and the removal of the blooming phytoplankton community would cause the marine environmental system to collapse.

This term would include the subclass axioms: ENVO:*marine environment determined by a community bloom* [URI pending], ENVO:*determined by* [ENVO_2100001] some PCO:*phytoplankton bloom process* [URI pending], RO:*causally downstream of, negative effect* [RO_0002305] some ENVO:*marine water body stratification* [URI pending]

I also prosed to encode the ENVO:*marine water body stratification* term in ENVO with the definition:

> A water body stratification process during which water within a marine water body is separated by density into layers which sit atop one another.

This term includes the subclass axioms: ENVO:*water body stratification* [URI pending], BFO:*occurs in* [BFO_0000066] some ENVO:*marine water body* [ENVO_00001999], RO:*results in formation of* [RO_0002297] some ENVO:*stratified marine water body* [URI pending], and finally RO:*results in formation of* [RO_0002297] min 2 ENVO:*marine layer* [ENVO_01000295].

I have also prosed to include the term ENVO:*sea ice melting* in ENVO, defining it as:

> An icemelt process during which meltwater is produced by the melting of sea ice, increasing stratification in the underlying water column, and increasing the amount of electromagnetic radiation absorbed within the site previously occupied by sea ice, which acted as a medium by which to attenuate and reflect incoming electromagnetic radiation.

Describing it with the subclass axioms: ENVO:*ice melt* [ENVO_01000721], RO:*has input* [RO_0002233] some (ENVO:*sea ice* [ENVO_00002200] and (RO:*adjacent to* [RO_0002220] some ENVO:*troposphere* [ENVO_01000540]) and (RO:*adjacent to* [RO_0002220] some ENVO:*marine water body* [ENVO_00001999])) and PATO:*decreased degree of illumination* [PATO_0015015], RO:*has output* [RO_0002234] some (ENVO:*meltwater* [ENVO_01000722] and (RO:*adjacent to* [RO_0002220] some ENVO:*troposphere
[ENVO_01000540]) and (RO:*adjacent to* [RO_0002220] some some ENVO:*marine water body* [ENVO_00001999])) and PATO:*increased degree of illumination* [PATO_0015014], RO:*causally upstream of* [RO_0002411] some
ENVO:*marine water body stratification* [URI pending], finally with oboInOwl:*database_cross_reference*s [hasDbXref] https://doi.org/10.1016/j.jmarsys.2013.11.008 [@Cherkasheva_2014], https://en.wikipedia.org/wiki/Attenuation and
https://en.wikipedia.org/wiki/Optical_properties_of_water_and_ice.

I bring these terms together in the following **Figure 12** as to visualize the interconnecting relationships between them.

![**Figure 12** Diagram indicating relationships interconnecting highlighted subset of ontology term contributions made during the course of this work to encode expert knowledge about plankton ecology. Nodes are proposed ontology classes for the ENVO, PCO and PATO ontologies. Edges are RO relationships.](figures/plankton_ecology.jpeg)

I assessed if ontologies can help us to contextualize the interconnections between encoded phenomena about which we have expert knowledge. **Figure 12** illustrating the relationships interconnecting the various phenomena which effect phytoplankton blooms shows how ontologies help us to understand the interconnections between pieces of expert knowledge. Starting by examining physical processes which have effects on phytoplankton blooms, I assembled and encoded the following expert knowledge. As the onset of phytoplankton blooms have been shown to be dependent on the timing of the retreat of melting sea ice [@Janout_2016], I encoded the knowledge of such a relationship into the potential term sea ice melting, by specifying that it is RO:*causally upstream of* [RO_0002411] some ENVO:*marine water body stratification* [URI pending].

I encoded the concept of the ENVO:*marginal ice zone*, which is described as the transition zone between the open ocean and sea ice [78]. In the ENVO:*marginal ice zone*, melting sea-ice has been shown to promote phytoplankton growth by stratifying the water column [@Cherkasheva_2014]. To encode the knowledge of the process of stratification I created the potential class ENVO:*marine water body stratification*, which RO:*results in formation of* [RO_0002297] at least two ENVO:*marine layer*s [ENVO_01000295]. In the ENVO:*marginal ice zone*, stratification of the water body resulting from melting sea ice has been shown to be the location of maximum chlorophyll [@Cherkasheva_2014], controlling the onset of the seasonal phytoplankton blooms [@Janout_2016]. To encode knowledge about phytoplankton blooms, I created a variety of terms related to population and community blooms. An example of which is the potential term phytoplankton bloom process. To represent the knowledge that phytoplankton blooms tend to occur as a result of sea ice retreat in the marginal ice zone. I have encoded into the ENVO:*marginal ice zone* term an axiom stating that marginal ice zones are RO:*causally upstream of, positive effect* [RO_0002304] some PCO:*phytoplankton bloom process* [URI pending]. As phytoplankton bloom processes have a profound impact on their surrounding environment, I have also created the term ENVO:*marine environment determined by a phytoplankton community bloom*, which I have specified to be related to PCO:*phytoplankton bloom processes* with the axiom ENVO:*determined by* [ENVO_2100001] some PCO: *phytoplankton bloom process* [URI pending]. I have also encoded the connection between an ENVO:*marine environment determined by a phytoplankton community bloom* and ENVO:*marine water body stratification* with the RO:*causally downstream of, negative effect* [RO_0002305] relationship.



\newpage

# 4. Discussion

## 4.1 Comparative environmental genomics

Making use of data annotated with interoperable Gene and Environment Ontology terms, I mobilized data to answer the question:

> "What are the relative abundance frequencies of oxidation-reduction process genes in various types of marine biomes?"

I examined the results of **Table 1**, showing the relative genomic and transcriptomic abundances of GO:*oxidation-reduction process* [GO_0055114] genes, in various ENVO:*marine biome*s [ENVO_00000447], to address the question of whether ontologies are fit for purpose to facilitate genomic comparisons based on environmental annotations. The results indicate as would be biologically expected that neritic samples are relatively enriched in photosynthesis, aerobic respiration and respiratory electron transport chain related genes. Relative to the deep abyssal and bathyal biome samples enriched in undifferentiated oxidation-reduction processes and methanogenesis related genes. This preliminary comparison indicates the feasibility of using ontology term annotations to interlink and compare genomic data differentiated by source environment.

Further exploring the use of interoperable GO and ENVO semantics to compare genomic abundances of samples annotated with different ENVO terms, we asked another question:

> "What are the relative abundance frequencies of vitamin biosynthetic process genes in various types of marine biomes?"

**Table 2**, showing the relative abundance of vitamin biosynthetic process genes in various types of marine benthic biomes, further addresses the use of ontologies to interconnect genomic data. Analyzing the result of finding elevated vitamin biosynthetic genomic capacity in deep samples relative to the lower transcriptomic capacity in neritic samples. I made use of the ontology knowledge graph to search for the relative abundances of other biological processes and molecular functions which may help to explain the differences in vitamin biosynthesis. As flavins have been implicated as electron donors in the reduction of insoluble ferric to soluble ferrous iron as well as the transport of ferrous to the cytoplasm [@Crossley_2007][@Fuller_2013], I investigated transition metal ion binding and transport subclasses, with the aid of the Gene Ontology knowledge hierarchy. The results of elevated ferrous ion binding and transport gene abundance in deep relative to neritic samples, combined with the elevated riboflavin biosynthetic processes suggest a potential ecophysiological connection. Allowing us to hypothesize that riboflavin mediated iron reduction differentiates deep bathyal and abyssal sediments from neritic sediments. This example illustrates how using the interoperable Environment and Gene Ontologies, can be used to facilitate genomic comparisons, enabling more specific ecological questions to be asked of omic data.

As OBO ontologies adopt a realist philosophy, representing what exists in reality as opposed to conceptualizations of reality which are shared by knowledgeable agents [@Arp_2015]. Multiple competing hypotheses can be encoded into the ontology knowledge graph without the presumption of any being the absolute truth.

A hypothesis such as the interconnection between riboflavin production, iron binding and transport genes in deep marine sediments, could be semantically expressed and added to the ontology knowledge graph. This along with other hypotheses about covariation of gene abundances could subsequently be tested over larger collections of genomic data sets. Leveraging the ontology semantics to retrieve data to analyze gene covariation to support or reject batches of genomic hypotheses. The continued development of cyberinfrastructure by which to conduct these types of comparative genomic analysis could be scaled up to a large machine-actionable system the analysis of microbial genomics. Thematically this could build upon previous efforts such as the Community cyberinfrastructure for Advanced Microbial Ecology Research and Analysis (CAMERA), a semantically-annotated environmental genomic data base supporting semantic queries [@Sun_2010].

To further investigate potential knowledge which can be derived from the interconnection of data annotated with GO and ENVO terms, I asked the following question of the example datastore:

> "What biological processes differentiate various types of marine benthic biomes?"

By drilling down into finer levels of granularity within the GO:*biological process* [GO_0008150] hierarchy, see **Figures 4** and **A2**, I was able to pinpoint processes differentiating deep abyssal and bathyal samples from neritic. **Figure 5** an examination of GO:*cellular aminoacid biosynthetic processes* [GO_0008652], a subclass of GO:*biological process* [GO_0008150], shows a much clearer differentiation of samples, than does the higher level class in **Figures 4**. From these results I was able to pinpoint even more specific subclasses to investigate differences between types of marine benthic biomes.

**Figures 5** showing GO:*serine family amino acid biosynthetic processes* [GO_0009070] illustrates a very clear and potentially biologically interesting difference. GO:*glycine biosynthetic process* [GO_0006545], which has as subclass GO:*glycine biosynthetic process from serine* [GO_0019264], is more abundant in the deep ENVO:*marine benthic biomes* [ENVO_01000024] samples, whereas GO:*cysteine biosynthetic process from serine* [GO_0006535] is more abundant in the ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples.

The amino acid serine is precursor in the production of both glycine and cysteine. Therefore, from these finding we can hypothesize that organisms from neritic biomes tend to produce cysteine from serine, whereas organisms from deep bathyal and abyssal biomes tend to produce glycine from serine. A possible explanation is that glycine is an important component in glycine betaine used by microbes as an osmoprotectant, helping to withstand osmotic stress [@Meury1988]. This may help cells to cope with high pressure deep environments.

What is most notable from this finding is that we were able to discover this potential difference based solely on information contained within the gene ontology. Having no preliminary ideas about what amino acid biosynthetic process which could differentiate deep and neritic samples, nor knowledge of amino acids serine is a precursor to. This example shows how ontologies are fit for purpose to interconnect disparate omic datasets and generate working hypotheses therefrom.

## 4.2 Testing hypotheses on open linked data

I have analyzed how ontology terms can be used to facilitate the assembly of relevant knowledge and data about a phenomenon of interest. Demonstrating how ontology terms can be used to guide the assembly of data which can be used to test hypotheses about the represented knowledge in question. In the example scenario, I was able to perform an ecological analysis of data associate with environmental factors which may influence a sea-ice associated phytoplankton community.
I did so by leveraging the subclass axioms of an ontology term to retrieve an assembly of data about its constituents.

Using ontology terms to guide the retrieval of open linked data by which to test hypotheses, I encountered both expected and unexpected data. For example when I retrieved data about environmental factors which may influence sea-ice associated phytoplankton communities, I retrieved some variables I expected to find such as sea ice thickness, multi-year sea ice temperature, degree of illumination of sea ice. Additionally, I also retrieved some unexpected but potentially useful data such as sea water salinity, oxygen, phosphate and nitrate concentrations. In an ideal case the ontology annotations would help us to assemble data which researchers would not have thought to include in the analysis. Sea water salinity data for example, may give an indication of the existence of meltwater released from sea ice melting. Such data coinciding with available nutrient concentrations could indicate the beginning of a phytoplankton bloom.

Despite being able to harness the rich wealth of knowledge encoded within ontologies, my analysis was limited by a lack of open linked data. Hence I would describe the current situation as rich in knowledge but poor in data. In order to be able to apply these types of types of ontology guided data assembly workflows to test a variety of scientific hypotheses, more open linked data is required. Efforts to do so do not need to be overly complicated. Simple improvements toward standardizing the scientific outputs generated by projects such as environmental observatories could go a long way toward providing annotated linked open data for the community to access. Striving toward the long term goal of improved data standardization, could help us to enable data to be used to its full potential. This would allow for future machine-guided meta-analyses to be conducted on large linked open data sets. Using ontologies and linked open data as the source material for future artificial intelligence knowledge representation endeavors may allow us to break through traditional analysis barriers. Enabling deep, expert-knowledge and large-data-informed machine-guided meta-analyses.

## 4.3 Tracking information provenance

Jackson’s (2012) bestiary of ignorance proposes four categories in an overview of knowledge or lack of knowledge about a subject [@Jackson_2012]. The most subtle yet possibly most important of these categories describes unknown known knowledge. Referring to scientific knowledge which has been generated or recorded, but to which easy access is lacking [@Hortal_2015]. Hortal et al. (2015) propose that informatics methods could be employed to facilitate community access to non-easily search-able knowledge collections [@Hortal_2015]. Considering informatics strategies by which to improve community access to unknown known knowledge, I examined various types of information which ontologies could be used to track the provenance of. I discuss ways in which ontology knowledge graphs can help to identify the provenance of primary literature associated with annotated datasets, specimens from a museum or collection, expert knowledge, and finally authors who contribute expert knowledge to ontologies. Mobilizing known unknown information data and knowledge into a greater ontology knowledge graph, is a first step toward overcoming the limitation of known unknown knowledge.  

Evaluating the fitness for purpose of ontologies to connect users to primary literature about datasets annotated with ontology terms, I posed the following question of the example datastore:  

> "What are all the papers which reference any data set, which is about a part of a marine biome?"

The results of which demonstrate the ontology knowledge graph can be used to direct users toward publications associated with datasets annotated with terms discovered from the ontology knowledge graph. For example, by searching for publications about BFO:*part of* [BFO_0000050] a ENVO:*marine biome* [ENVO_00000447] the ontology knowledge graph lead us to papers about a ENVO:*marine water body* [ENVO_00001999]. In some cases this process lead us to publications written about the data set of interest. For example the publication *Influence of snow depth and surface flooding on light transmission through Antarctic pack ice* [@Arndt_2017], about the *Influence of snow depth and surface flooding on light transmission through Antarctic pack ice, supplementary data.* dataset. This publication was retrieved due to the dataset being annotated as being an OBCS:*data matrix* [OBCS_0000120] about some PATO:*physical* quality* [PATO_0001018] and (RO:*inheres in* [RO_0000052] some (ENVO:*marine water body* [ENVO_00001999]) and (RO:*adjacent to* [RO_0002220] some ENVO:*sea ice* [ENVO_00002200]))

In other cases publication less directly related to a dataset about a part of an ENVO:*marine biome* [ENVO_00000447], were retrieved. Such as for example the publication *An evaluation of the application of CHEMTAX to Antarctic coastal pigment data* [@Kozlowski_2011], which made use of a subset of the data from the *Global chlorophyll "a" concentrations for diatoms, haptophytes and prokaryotes obtained with the Diagnostic Pigment Analysis of HPLC data compiled from several databases and individual cruises.* dataset. This publication was retrieved as it is referenced in a dataset annotated as being an OBCS:*data matrix* [OBCS_0000120] about some CHEBI:*chlorophyll a [CHEBI_18230] and (RO:*part of* [BFO_0000050] some ENVO:*marine water body* [ENVO_00001999])

Although these are relatively uninteresting uninteresting examples of retrieving publication referenced in a dataset about a term of interest. They demonstrate proof of concept for the interconnection of datasets and publications annotated using ontology terms. This process could be applied to search for data annotated at a higher level of granularity. For example to search for publications which use datasets about a prokaryotic phytoplankton community bloom occurring in icebergs calved from Antarctic glaciers in the Weddell Sea. Semantically expressed as some: PCO:*phytoplankton community bloom* [URI pending] and (RO:*composed primarily of* [RO_0002473] some *prokaryotic organisms* and (RO:*overlaps* [RO_0002131] some RO:*output of* [RO_0002353] some  ENVO:*iceberg calving process* [ENVO_03000031] and (RO:*located in* [RO_0001025] some GAZ:*Weddell Sea* [GAZ_00004045]))).

A semantic annotation such as this could be realized by using the open source gazetteer GAZ [@gaz_2015], an ontologically-oriented listing of place names. Which could be used to provide the semantic annotation for a specific geographic feature of interest such as the GAZ:*Weddell Sea* [GAZ_00004045]. Terms such as *phytoplankton community bloom* or *prokaryotic organisms* could be provided by the Population and Community Ontology. The objective being to interconnect data sets and publications annotated at a very specific level of granularity. Allowing users to ask questions such as:

> "What publications reference datasets about prokaryotic phytoplankton community bloom occurring in icebergs calved from Antarctic glaciers in the Weddell Sea?"

These same semantic data annotation, querying and retrieval principals could also be used to facilitate the search for information about specimens. For example if natural history collections containing preserved NCBITaxon:*Alveolata* [NCBITaxon_33630] (dinoflagellates), were to encode information about the morphologies of such specimens in queryable formats with ontology term annotations. Providing an specimen annotation such as some: owl:*NamedIndividual* [NamedIndividual] and (rdf:*subClassOf* [subClassOf] some  NCBITaxon:*Alveolata* [NCBITaxon_33630] and (*has role* [RO_0000087] some OBI:*specimen role* [OBI_0000112] and (RO:*has quality* [RO_0000086] some PATO:*morphology* [PATO_0000051]))).

Users would be enabled to ask questions of the query-able natural history specimen collections such as:

> "What are all possible morphologies of Alveolata species for which there are collected specimens?"

This would go a long way toward facilitating the ease of access to knowledge about unconnected parts of the collective scientific knowledge base, helping the scientific community to overcome the challenge of coping with unknown known knowledge.

Ontologies can additionally be used to interconnect and track the provenance of expert information. An example of which was presented during the VoCamp Hackathon session where partially non-overlapping definitions of the term *ablation* which were sourced from the NOAA National Weather Service Glossary 2009 [@nws_internet_services_team_glossary_2009] and Cogley et al. IACS-UNESCO Glacier Mass
Balance 2011 [cogley_glossary_2011] glossaries. As ontologies take an agnostic stance when representing knowledge which has multiple definitions or which pertains to competing hypotheses [@Arp_2015]. A variety of approaches can be taken in parallel to incorporate such definitional discrepancies into the ontology knowledge graph, while tracking the provenance of the information source. A general *ablation* class could be created to include all the possible ice loss processes included in the various definitions of *ablation*. If ontology users are attempting to mobilize data about a specific combination of ice loss process classes, they could post-compose a semantic annotation which includes the specific processes of interest as axioms. A post-compositional annotation describing data specifically about *ablation* due to melting ice and ice calving could for example be: ENVO:*ice loss process* [ENVO_01000915] and (RO:*formed as result of* [RO_0002354] some (ENVO:*icemelt*[ENVO_01000721] or ENVO:*ice calving process* [ENVO_01000917]))

If pre-composition is desired, in for example a case where a combination of specific ablation processes are commonly referred to together as a set, a new term with a descriptive label could be created. A pre-compositional invocation of the example mentioned above would to create a descriptive term such as *calving and icemelt derived ablation*. Having a descriptive human readable label would facilitate the term's use for people such as domain experts or data stewards who are annotating data or describing a specific process. This term could include a oboInOwl:*database_cross_reference* [hasDbXref] to the Cogley et al. IACS-UNESCO Glacier Mass
Balance 2011 glossary [@cogley_glossary_2011] to track the provenance of the information source.
From a linked data perspective, both the pre-compositional and post-compositional annotations of the phenomena in question would make use of the same axiom (above). Hence both the pre and post composed versions of the term would be equivalent in terms of machine-searchability. This would facilitate the interoperation of data annotated both manually for example with a term such as *calving and icemelt derived ablation* and automatically for example by a semi-automated routine for post-compositionally annotating data, making use of existing terms.

Ontologies can also be used to track the provenance of term authors who have contributed expert knowledge to an ontology knowledge graph. There is a need to track the provenance of expert knowledge authorship, as scientific discoveries are increasingly being enabled through Internet based collaboration [@nielsen_2012]. Ontologies are semantic representations of expert knowledge, and thus have the potential to facilitate on-line networking among scientists, allowing users to connect to the authors who have contributed their expert knowledge.

In order for ontologies to facilitate future scientific networking and discoveries, ontologies would benefit from more domain experts recording their knowledge into ontologies. To incentivize such actions, ontologies would benefit from micro-crediting knowledge contributions at the term level. To facilitate scientific networking, authors who contribute knowledge to ontologies should be micro-credited with unambiguous personal identifiers. These identifiers would need to be connected to a living system which is query-able. Allowing for users to query the ontology knowledge for any authors who contributed knowledge related to specific input terminology of interest. Enabling a query such as:

> "Find the contract information for all authors who contributed knowledge to the sea ice terminology hierarchy."

A standard method by which to micro-credit authors within ontologies is to annotate terms with a link to an Open Researcher and Contributor ID (ORCID) [@ORCID_2009]. ORCIDs are persistent digital identifier serving as primary keys to distinguish researchers. ORCID satisfies the requirement of being a permanently maintained persistent living system by which to track author provenance. Being a web service, ORCID also provides an application programming interface by which user contact information can be queried. Authors may change affiliations or contact information multiple times throughout their career; however they would only ever use a single ORCID account. Hence ORCIDs provide a persistent unique identifier fit for the purpose of interconnecting authors of ontology terms to the knowledge they have helped to encode.

In order to evaluate the extent to which ontologies serve to interconnect people who contribute knowledge to the knowledge they have contributed, I asked the following question:

> "How well do the Environment Ontology and the Environment Ontology Polar subset connect authors of terms to the information they helped to encode?"

The results intricate that only 20% and 50% of terms from the Environment Ontology and its polar subset respectably contain a directly querable author annotation. Making it difficult to directly search for the author of a given term. Although ontologies such as ENVO make use of term ranges to identify authors. This information is stored in a separate meta-data owl file, which would be difficult to query for without a priori knowledge of its existence. The practice of using author ID ranges works for ontologies with smaller numbers of contributing authors, but constituents a cumbersome solution for the micro-crediting of many authors who may only ever contribute to a single term. Directly annotating terms with links to contributing author ORCIDs provides a more easily scalable solution for future influxes of contributing authors. Directly annotating ontology terms with links to the ORCIDs of contributing authors would serve to identify term author provenance. As well as facilitate future networking amongst scientists by connecting ontology term authors to OCRIDs, from which current contact information can be pulled.

## 4.4 Ontology guided knowledge discovery

I assessed if ontological knowledge graphs are fit for the purpose of connecting information or data explicitly stated by a researcher to new, unstated but related knowledge or data. Assuming connectivity within the envoPolar knowledge graph is analogous to the facility of researchers searching the network to discover new data and knowledge associated with their stated input knowledge. I created a network out of the Polar subset of the Environment Ontology and assessed its network parameters calculated as a directed graph to attempt to answer the following question:

> "Is the ontology knowledge graph of the envoPolar subset sufficiently well connected to be able to lead researchers to new knowledge via unstated linkages to identified knowledge?"

Our analysis of the properties of the network envoPolar created from the envoPolar subset is as follows. The network has a low number of components, with the vast majority of nodes and edges belonging to the largest components. Therefore the network should be analyzed as a relational based regime as opposed to a competent based regime. This is logical as the network makes use of structured upper level semantic models of the Basic Formal Ontology and the Relations Ontology as has been previous discussed.

I additionally examined the diameter of the network, the longest possible path between connected nodes in a network to gain insight into how well integrated the network is. Longer maximum path lengths equate to less well integrated networks [@labs_network_2016]. In the envoPolar network, the maximum path length is only 7. Examining the distribution of path lengths, see **Figure 5** we observe that the majority of nodes have a path length of 2. This means that the average node in the network is only 2 steps away from most other nodes. Hence the overall network is well connected.

Examining the in-degree distributions of nodes in the network, see supplemental **Figure 10**, I remarked that some nodes have very many connections, while the majority of nodes have only a few (one or two) connections. A network containing very few highly connected nodes and very many poorly connected nodes implies it bears a centralized network structure. This can also be seen in **Figure 6** the graph of average clustering coefficient as a function of number of neighboring nodes, where I observed two distinct clusters of nodes. Nodes higher up in the hierarchy are well connected to a small number of neighbors. While nodes lower down in the hierarchy are poorly connected to a larger number of neighbors. A third network parameters additionally indicating a very centralized network structure is the distribution of betweenness centrality values. Supplemental **Figure 12** shows a distribution where only 3 nodes, each of which only have two neighbors, have elevated betweenness centrality values, reflecting the amount of control these nodes exerts over the interactions of other nodes. Demonstrating that the network is highly centralized, with three very important central nodes which exert control over all other nodes in the network. ENVO:*geographic feature* [ENVO_00000000] is an example of one of these central nodes, having the largest degree of in-connectivity in the envoPolar graph. This is logical as this node is relatively high in the material entity hierarchy. The nodes in-degree value of 44 means there are 44 classes in the envoPolar network which fall underneath the geographic feature hierarchy.

Highly centralized networks are termed scale free or power law networks [@Choroma_ski_2013], which describe an exponential relationship between the degree of connectivity a node has and the frequency of its occurrence. Examining the topology of the envoPolar network I observe a hierarchical and branched tree-like structure. Branching structures are typically much more efficient ways of connecting networks, as the branching structures provide an exponential growth in the number of nodes that can be reached relative to the path length traversed [@Kou_2014]. Allowing for a very short average path length within a very large network, which is what we observe in the envoPolar network.   

In terms of robustness a scale free network won't be dramatically affected by removing or changing low degree nodes, however it would be very affected if the central nodes were removed or changed. If for example the Basic Formal Ontology hierarchy we no longer used and suddenly a very central node such as ENVO:*geographic feature* [ENVO_00000000] were to be removed without replacement, the network would shatter into many unconnected components, rendering it unable to interconnect information. In the current organizational structure the majority of nodes are only  two steps away from highly centralized and well-connected *hub* nodes. Through these highly centralized nodes the network is very highly interconnected. This is due to the hierarchical organizational structure of the ontology.

The majority of nodes, however, are not very well connected to. The results of **Table 13** show that only a handful of nodes with high in-degree values are polar related semantic terms sourced from lower down in the hierarchy. Furthermore the low average in connectivity of nodes in the network implies that most nodes are not well connected to by other nodes. Hence it is my assessment that more work is needed to encode the potential relationships which exist between classes. Building upon the relational connectivity of the envoPolar knowledge graph will be necessary in order for nodes within the graph to be of sufficient in-connectivity to facilitate the discovery of new information based on relationships to stated knowledge.

## 4.5 Practical and resilient systems for linked open data

In **Figure A.1** I propose that ontology terms can serve as the semantic infrastructure for the mobilization of linked open data, serving to gather relevant knowledge to conduct scientific experiments. To address the practicality of using ontologies as the semantic infrastructure for the mobilization of linked open data, I evaluated two main questions. The first question assessed the resilience of open linked data to changes in upper level semantic models. The second question evaluated how practical it is for predicted users to assemble semantically-annotated linked open data.

Evaluating the extent to which linked open data is resilient to potential changes in upper level BFO and RO semantic models used for annotation, I asked the following questions:

> "What percentages data items about participants in sea ice formation processes would we be able to retrieve if we didn't use the Basic Formal Ontology or Relations Ontology upper level semantic models?"

To answer such questions I simulated the effects of not utilizing the Basic Formal Ontology or Relations Ontology upper level semantic models to retrieve data from the example polar datastore. The results of these simulations indicate that the upper level semantic models are crucially important in order to retrieve data about classes participating in a phenomenon of interest. In the simulation, if fundamental changes were made to the Basic Formal Ontology, only 50% of the data would be retrievable. Additionally, if a non-standardized set of relations were to be used in place of the structured Relations Ontology relations, it would not be possible to retrieve data about classes participating in a phenomenon of interest from the model datastore. These results imply that upper level semantic models are crucially important when using ontology terms to mobilize linked data. It is critical that upper level semantic model be standardized and used consistently to annotate linked open data.

Although I am not specifically advocating for the use of the OBO Foundry and Library ontology semantic models to be used to standardize linked open data. Such models would be a reasonable choice for semantic standardization, as they provide a pre-existing, interoperable semantic infrastructure, including the arguably most successful and widely used biomedical ontology, the Gene Ontology [@Ashburner_2000]. Additionally, efforts are underway to align the OBO ontologies, primarily the Environment Ontology with the NASA Semantic Web for Earth and Environmental Technology (SWEET) ontologies [@sweet_2018]. The SWEET ontologies are the *de facto* standards for the formal representation of earth and environmental science domain knowledge [@DiGiuseppe_2014]. Aligned OBO and SWEET semantic hold great potential to aid in the future interconnection of environmental and genomic data.

In order to assess the practicality of retrieving ontology annotated data from our example datastore, which contains data annotated with axiomatic structures of various levels of complexity and non-uniformity. I asked the following question:

> What level of querying expertise is required to access the various types of data contained in the example polar datastore?

Lacking the scope to be able to conduct a proper experiment on a study group of scientists with various proficiencies for performing semantic queries to retrieve data from the example datastore, I evaluated this question by testing the performance of predicted user stores estimating users of various querying proficiencies to retrieve example data.

The results of these predicted user stories indicated that users of basic querying expertise were only able to retrieve a tiny fraction of annotated data, users of intermediate expertise less than half the data and even users advanced users could not fully retrieve all data. Possible reasons for such results may be due to non-uniformities in axiomatic structures used to annotate the example data.

Clearly these outcomes are limited being only user story simulation conducted in place of proper user group analyses. Semantic science advances could be made by creating an open linked data repository with various styles of data annotations of which a user focus group would be tasked with querying. This would serve to inform us as to what axiomatic annotations are readily querable lending themselves to successful data mobilization, and which are not. Additional efforts could make use of Neuro-Linguistic Programming (NLP) knowledge to create data annotations which are intuitive to average users. Additionally, efforts could be undertaken to find better ways of connecting and storing linked data which make use of more natural linguistic patterns, to attempt to make linked data accessible by methods other than cumbersome and technical SPARQL queries.

Next, I discuss the axiomatic data annotation patterns which the predicted user stories were and were not able to query. I first examine an example axiomatic pattern used to annotate data about *snow thickness*. This annotation axiom was successfully queried by user stories of intermediate expertise and makes use of the following axiom: PATO:*thickness* [PATO_0000915] and (RO:*inheres in* [RO_0000052] some ENVO:*snow*[ENVO_01000406])). This example axiomatic annotation structure, about a thickness quality which is realized in the material entity snow is relatively straight forward. Employing the pattern of:

```
class A, relation 1, some class B
```

When creating an axiomatic data annotation there is trade-off between a complete and correct philosophical description of a subject vs. a more pragmatic linked data approach intended to make data easily mobilizable. The example of data about *snow thickness*, presents an axiomatic pattern which is a reasonable comprise between a correct description and an easily mobilizable data annotation.

In order to semantically represent data about a more complicated phenomenon, questions arise about how to address such a trade-off. For example data about *mean snow thickness*, which was not retrieve by the advanced user stories, is annotated with the axiom: OBCS:*expected value* [OBCS_0000083] and IAO:*is about* [IAO_0000136] min 2 (IAO:*data item* [IAO_0000027] and IAO:*is about* [IAO_0000136] some (PATO:*thickness* [PATO_0000915] and [RO:*inheres in* [RO_0000052] some  ENVO:*snow*[ENVO_01000406])). In this example the data is an expected value (a mean) of other data which are about a thickness quality which is realized in some snow. In this example the axiomatic annotation is not as straight forward taking the form:

```
class A, relation 1, cardinality value, class B, relation 2, some class C, relation 3 some class D
```

The non-uniformity of this query, which makes use of a cardinality value as opposed to the general *some* article, prevents general querying patterns from accessing this data. This is due to the different owl syntax for handing restrictions about *some* vs. *min* or *max*. Performing SPARQL queries on axioms which are chained together, as is the case for owl annotated data, requires the use of extended property path within the SPARQL query. An example property path required for a SPARQL query to be able to access owl annotated data is as follows:

```
owl:someValuesFrom/owl:intersectionOf/rdf:rest*/rdf:first
```

Where the ``owl:someValuesFrom`` is the relation to navigate through the *some* article. Due to the constraint of needing to use extended property paths to perform SPARQL queries on owl annotations, individual cases would need to be created to cover every possible case, if for example the article were variable in the property path. This would be a very cumbersome solution impeding the retrieval of annotated data. It is worth considering the utility of expressing the fact that we are describing an expected value about at least two data points, especially if it impedes data mobilization. A compromise solution would be to make use of a more standard annotation pattern, for example of the form:

```
class A and (any relation some class B and (any relation some class C and (...)))
```

A highly uniform and easily expendable pattern such as this would facilitate the retrieval of data, as well as provide sufficient depth to satisfactorily describe a phenomenon of interest, satisfying both the ontology philosopher and the pragmatic mobilizer of data.


\newpage

# 5. Conclusion

In conclusion this work has demonstrated that ontologies are fit for purpose to perform a variety of tasks related to the interconnection and mobilization of interdisciplinary data. Ontologies can be used to represent expert knowledge about environmental phenomena such as plankton ecology with machine-actionable semantics. Ontology terms could additionally serve to track the provenance of information, datasets, specimens and scientific publications, helping to the scientific community to overcome the limitation of known unknown knowledge.

Ontologies can aid to mobilize interdisciplinary datasets, by annotating and querying datasets using ontology terms. Ontology terms through their axiomatic relationships could in principal be used to facilitate the assembly previously unconnected but relevant data to perform ecological analyses.

When using ontology terms to annotate data, uniform and repetitive annotation patterns would aid to mobilize annotated data while providing sufficient depth to adequately represent phenomena of interest. Additionally, it is of crucial importance when utilizing ontology terms to mobilize data, to maintain consistent usage of upper level semantic models such as the Basic Formal Ontology and the Relations Ontology, deviation from which could have serious consequences on the effectiveness of data mobilization.

In order for ontologies to help facilitate future networking amongst creators and users of knowledge captured in ontologies, term author annotation could be implemented at the term level. With direct annotations to pull-able and living author identifying systems such as ORCID, helping to track the provenance of term authors.

Ontological knowledge graphs are highly centralized due to the hierarchical structure provided by the BFO upper level semantic model. Such graphs exert scale free properties as an exponential number of nodes can be reached from a linear increase in path length traversed. The majority of nodes, however, have few connections. Hence more axiomatic relationships are required in order for the networks to facilitate the discovery of new information based on connections to stated information. Due to their centralized nature, ontologies knowledge graphs are robust to changes made to lower level terms, but vulnerable to substantial changes made to higher level terms.

Finally this work has demonstrated that interoperable environmental and genomic semantics provided by the Environment and Gene ontologies can be leveraged to generate bioinformatic hypotheses from the comparison of environmentally annotate omics datasets.

\newpage

# 6. Outlook

As a first outlook form this work, polar related semantics contributed to the envoPolar subset could be aligned with the dpbedia ontology [90] glacial semantics. Disseminating knowledge output from the Alfred Wegener Institute (AWI) to the open source encyclopedia Wikipedia would serve to simultaneously to improve Wikipedia and improve AWI public outreach. Helping to communicate AWI research outputs, as well as educate the public on polar knowledge.

A second outlook to this work which is currently underway is the creation of polar terminology to be used for the annotation of polar genomic sequence data. Such terminology would be detailed in cryosphere extension paper to the Minimum Information about any (x) Sequence (MIxS) genomic sequence submission standards [91].

A third outlook from this work would be to research strategies for effective data annotation and mobilization. The knowledge gained therefrom could be used to develop tools to automate and standardized the annotation of data, datasets, samples and or specimens with ontology terms, aiding to make published data interoperable, mobilizable, and precisely annotated.

A final outlook from this work could involve the creation of an Polar Environmental Observatory Intelligence System. Such a system would be built using knowledge representation, a branch of artificial intelligence. This would involve using the relational knowledge represented by axioms within the Environment and Gene ontologies,
in propositional or first order logic models. These ontologically derived logic models would additionally be given information in the form of ontology term annotated data, allowing for reasoning to be conducted over the knowledge model. Input data from which to seed the model would be sourced from data generated by the AWI HAUSGARTEN and FRAM observatories. Input data could include: AWI autonomous buoy sea ice thickness data, physical and chemical oceanography data, FRAM microbial observatory program genomic data, and NASA earth observatory and National Snow and Ice Data Center satellite chlorophyll and sea ice cover data. Additionally, the Gene, Environment and other related ontologies would be extended to create a rich first order and or propositional logic model. Such a system would be programed to dynamically incorporate new data as it is published, and would be developed to systematically address interdisciplinary questions such as:

> "Does microbial taxon diversity in deep-sea sediments show resilient patterns over seasonal cycles?"

> "What metabolic processes are enriched in the microbial communities of multi-year sea ice?"

> "Which ranges of nutrients result in high taxon turnover in the epipelagic zone?"

> "Which cellular components are enriched during a bloom induced by sea ice retreat?"

\pagebreak
# References

<div id="refs"></div>


\pagebreak
# Appendices

## A.1 Semantic science adaption of scientific method

![**Figure A1** Shows the adaptation of semantic science to the scientific method, facilitate the reuse of published data. Item **A** shows the standard scientific method where problems are defined, hypotheses are generated, experiments are conducted to test hypotheses either generating publishable data or leading to the definition of new problems. Item **B** shows the workflow by which to convert published data to machine-actionable formats, annotate with ontology terms as meta-data. This facilitates the process of asking questions of open linked data and gather data to test hypotheses.  ](figures/semantic_data_lifecycle.jpg)



## A.2 Model polar datastore creation

A Model data store of environmental and genomic data was created during this work. Detailed description of axioms making use of ontology terms used to post-compositionally annotate the example polar datastore are available from: https://github.com/kaiiam/kblumberg_masters_thesis/wiki/complete_datastore

The following datasets were included in the example datastore:

1. Inorganic nutrients measured on water bottle samples at AWI HAUSGARTEN during POLARSTERN cruise MSM29. @bauerfeind2014inmo

2. Physical oceanography and current meter data from mooring TD-2014-LT. @bauerfeind2016poac

3. Chlorophyll a measured on water bottle samples during POLARSTERN cruise ARK-XXIV/2. [@nthig2015camo][@N_thig_2015]

4. Global chlorophyll "a" concentrations for diatoms, haptophytes and prokaryotes obtained with the Diagnostic Pigment Analysis of HPLC data compiled from several databases and individual cruises. [@soppa2017gcac][@Losa_2017]

5. Biogenic particle flux at AWI HAUSGARTEN from mooring FEVI7. [@bauerfeind2009bpfa][@Bauerfeind_2009]

6. Snow height on sea ice and sea ice drift from autonomous measurements from buoy 2015S22, deployed during the Norwegian Young sea ICE cruise N-ICE 2015. [@nicolaus2015shos][@nicolaus2017shaa]

7. Sea ice thickness at Ice Camp 1 on 2013-09-01 (GEM2IceTh_DiveHole_IceStation1). [@ricker2017sita][@Arndt_2017]

8.  Influence of snow depth and surface flooding on light transmission through Antarctic pack ice, supplementary data. [@arndt2017iosd][@Arndt_2017]

9. Ice-algal chlorophyll a and physical properties of multi-year and first-year sea ice of core CASIMBO-CORE-2_11. [@lange2015icaa2][@Lange_2015]

10. Unpublished metagenomic data from deep sea sediments from Hausgarten POLARSTERN Polarstern cruise PS85, encompassing both functional genomic data in the form of preprocessed pfam2go tables as well as 16S taxonomic data, courtesy of Josephine Z. Rapp.

11. Unpublished transcriptomic data from shallow Helgoland Marine Sediments during a spring phytoplankton bloom, encompassing preprocessed pfam2go tables, courtesy of David Probandt, and Matthew Schechter.



\newpage
## A.3 Metagenomic and metatranscriptomic data

Abyssal and Bathyal metagenomic data provided by Jose Rapp consisted of four samples collected from Polarstern cruise PS85, at stations 470, 460, 464, 465. Samples 1 and 2 were collected from depths of 1244m and 2403m which best correspond to ENVO:*marine bathyal zone biome* [ENVO_01000026] Samples 3 and 4 were collected from depths of 3531m and 5525m which best correspond to ENVO:*marine abyssal zone biome* [ENVO_01000027]

Neritic transcriptomic data provided by Dr. David Probandt, were collected from shallow ~8m depth Helgoland Marine Sediments during a spring phytoplankton bloom. Sediments were characterize as being ENVO:*sandy sediment* [ENVO_01000118] from an ENVO:*marine neritic benthic zone biome* [ENVO_01000025]. The first 4 samples: labeled X1-X4 were used.



\newpage

: **Table A1** Results of the relative genomic and transcriptomic abundances of GO:*transition metal ion transport* [GO_0000041] process in various types of ENVO:*marine benthic biome*s [ENVO_01000024], queried for in the example datastore.

| term                                                    | ENVO:*marine abyssal zone biome* [ENVO_01000027] | ENVO:*marine bathyal zone biome* [ENVO_01000026] | ENVO:*marine neritic benthic zone biome* [ENVO_01000025] |
|:--------------------------------------------------------|:-------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------------|
| GO:*ferrous iron transport* [GO_0015684]                | 0.04                                             | 0.04                                             | 0.02                                                     |
| GO:*mercury ion transport* [GO_0015694]                 | 0.01                                             | 0.00                                             | 0.00                                                     |
| GO:*nickel cation transmembrane transport* [GO_0035444] | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*transition metal ion transport* [GO_0000041]        | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*iron ion transmembrane transport* [GO_0034755]      | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*iron ion transport* [GO_0006826]                    | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*copper ion transmembrane transport* [GO_0035434]    | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*cobalt ion transport* [GO_0006824]                  | 0.00                                             | 0.00                                             | 0.00                                                     |
| GO:*copper ion transport* [GO_0006825]                  | 0.00                                             | 0.00                                             | 0.00                                                     |

: **Table A2** Results of the relative genomic and transcriptomic abundances of GO:*transition metal ion binding* [GO_0046914] molecular functions in various types of ENVO:*marine benthic biome*s [ENVO_01000024], queried for in the example datastore.


| term                                           | ENVO:*marine abyssal zone biome* [ENVO_01000027] | ENVO:*marine bathyal zone biome* [ENVO_01000026] | ENVO:*marine neritic benthic zone biome* [ENVO_01000025] |
|:-----------------------------------------------|:-------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------------|
| GO:*transition metal ion binding* [GO_0046914] | 0.70                                             | 0.67                                             | 0.52                                                     |
| GO:*cobalt ion binding* [GO_0050897]           | 0.69                                             | 0.73                                             | 1.07                                                     |
| GO:*ferric iron binding* [GO_0008199]          | 0.22                                             | 0.21                                             | 0.62                                                     |
| GO:*nickel cation binding* [GO_0016151]        | 0.12                                             | 0.13                                             | 0.12                                                     |
| GO:*molybdenum ion binding* [GO_0030151]       | 0.05                                             | 0.05                                             | 0.10                                                     |
| GO:*manganese ion binding* [GO_0030145]        | 0.04                                             | 0.04                                             | 0.02                                                     |
| GO:*iron ion binding* [GO_0005506]             | 0.04                                             | 0.04                                             | 0.03                                                     |
| GO:*zinc ion binding* [GO_0008270]             | 0.03                                             | 0.03                                             | 0.11                                                     |
| GO:*ferrous iron binding* [GO_0008198]         | 0.02                                             | 0.03                                             | 0.00                                                     |
| GO:*copper ion binding* [GO_0005507]           | 0.01                                             | 0.01                                             | 0.02                                                     |
| GO:*copper chaperone activity* [GO_0016531]    | 0.00                                             | 0.00                                             | 0.00                                                     |


\newpage

![**Figure A2** GO:*biological process* [GO_0008150] hierarchy differentiating ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] ENVO:*marine sediments* [ENVO_03000033]. ](figures/supplemental/GO_bio_process_hierarchy.jpeg){ width=80% }

Subclasses of boldfaced terms GO:*biological process* [GO_0008150], GO:*cellular amino acid biosynthetic process* [GO_0008652], and GO*serine family amino acid biosynthetic process* [GO_0009070] are the subjects of the Principal coordinate analyses plots in **Figures 4**, **5** and **6** respectably. GO*serine family amino acid biosynthetic process* [GO_0009070] terms differentiating ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] ENVO:*marine sediments* [ENVO_03000033], shown in **Figure 6**, are GO:*glycine biosynthetic process* [GO_0006545], and GO:*cysteine biosynthetic process from serine* [GO_0006535].



## A.4 Marine biome associated DOIs

: **Table A3** Complete list of digital object identifiers of publications obtained querying for references of datasets which are about BFO:*part of* [BFO_0000050] an ENVO:*marine biome* [ENVO_00000447].

+---------------+----------------------------+------------------------+
|data annotation|reference doi               | reference title        |
+===============+============================+========================+
|global        \|10.1016/j.dsr.2011.01.008   |An evaluation of the application\|
|chlorophyll a \|                            |of CHEMTAX to Antarctic coastal\|
|              \|                            |pigment data [@Kozlowski_2011]\|
|              \|                            |                        |
+---------------+----------------------------+------------------------+
|               |10.1016/j.pocean.2009.07.011|Dimethylsulphide, DMSP-lyase\|
|               |                            |activity and microplankton\|
|               |                            |community structure inside\|
|               |                            |and outside of the Mauritanian\|
|               |                            |upwelling [@Franklin_2009]\|
+---------------+----------------------------+------------------------+
|               |10.5194/bg-9-1041-2012      |Environmental control on the \|
|               |                            |variability of DMS and DMSP\|
|               |                            |in the Mauritanian upwelling \|
|               |                            |region [@Zindler_2012]  \|
+---------------+----------------------------+------------------------+
|               |10.3390/rs61010089          |Global Retrieval of Diatom\|
|               |                            |Abundance Based on Phytoplankton \|
|               |                            |Pigments and Satellite Data [@Soppa_2014]\|
+---------------+----------------------------+------------------------+
|               |10.5194/bgd-10-12115-2013   |Photophysiological state of \|
|               |                            |natural phytoplankton \|
|               |                            |communities in the South \|
|               |                            |China Sea and Sulu Sea [@Cheah_2013]\|
+---------------+----------------------------+------------------------+
|               |10.1016/j.dsr.2014.12.010   |Physiological characteristics\|
|               |                            |of open ocean and coastal\|
|               |                            |phytoplankton communities\|
|               |                            |of Western Antarctic Peninsula\|
|               |                            |and Drake Passage waters [@Trimborn_2015]\|
+---------------+----------------------------+------------------------+
|               |10.1002/2014JC010355        |Retrieving the vertical\|
|               |                            |distribution of chlorophyll\|
|               |                            |a concentration and phytoplankton\|
|               |                            |community composition from in\|
|               |                            |situ fluorescence profiles:\|
|               |                            |A method based on a neural\|
|               |                            |network with potential for\|
|               |                            |global-scale applications [@Sauz_de_2015]\|
+---------------+----------------------------+------------------------+
|               |10.5194/bg-10-3297-2013     |Sulphur compounds,methane, and\|
|               |                            |phytoplankton: Interactions \|
|               |                            | along a north-south transit in \|
|               |                            |the western Pacific Ocean [@Zindler_2013]\|
+---------------+----------------------------+------------------------+
|               |10.3402/polar.v34.23349     |Summertime plankton ecology\|
|               |                            |in Fram Strait-a compilation\|
|               |                            |of long- and short-term \|
|               |                            |observations [@N_thig_2015] \|
+---------------+----------------------------+------------------------+
|               |10.5194/essd-5-109-2013     |The MAREDAT global database \|
|               |                            |of high performance liquid \|
|               |                            |chromatography marine pigment \|
|               |                            |measurements [@Peloquin_2013]\|
+---------------+----------------------------+------------------------+
|               |10.1029/2003EO380001        |Unique data repository \|
|               |                            |facilitates ocean color\|
|               |                            |satellite validation [@Werdell_2003] \|
+---------------+----------------------------+------------------------+
|               |10.5194/os-11-139-2015      |Using empirical orthogonal \|
|               |                            |functions derived from remote-\|
|               |                            |sensing reflectance for the \|
|               |                            | prediction of phytoplankton  \|
|               |                            |pigment concentrations [@Bracher_2015] \|
+---------------+----------------------------+------------------------+
|               |10.1029/2005JC003207        |Vertical distribution of \|
|               |                            |phytoplankton communities \|
|               |                            |in open ocean: An assessment\|
|               |                            |based on surface chlorophyll [@Uitz_2006] \|
+---------------+----------------------------+------------------------+
|influence snow\|10.1002/2016JC012325        |Influence of snow depth and \|
|depth         \|                            |surface flooding on light\|
|              \|                            |transmission through Antarctic \|
|              \|                            |pack ice [@Arndt_2017] \|
+---------------+----------------------------+------------------------+


\newpage

## A.5 Glacial community consultation working group participants

Participants in the Feb 2, 2018 VoCamp Glacier Ontology Hackathon are listed in the following **Table A2**.

: **Table A4** Participants in the Feb 2, 2018 February VoCamp Glacier Ontology Hackathon and community semantic consultation session.

| participant             | affiliation                                                             |
|:------------------------|:------------------------------------------------------------------------|
| Pier Buttigieg          | Alfred Wegener Institute Helmholtz Centre for Polar and Marine Research |
| Brandon Whitehead       | Centre for Agriculture and Biosciences International (London)           |
| Siri Jodha Singh Khalsa | National Snow and Ice Data Center (Czech Republic)                      |
| Kai Blumberg            | Max Plank Institute for Marine Microbiology                             |
| Gary Berg-Cross         | Independent Consultant Potomac, MD                                      |
| Ruth Duerr              | Ronin Institute Boulder Colorado                                        |
| Varanka Dalia           | United States Geological Survey (Rolla Missouri)                        |
| Samantha Arundel        | United States Geological Survey (Rolla Missouri)                        |
| Nancy Wiegand           | University of Wisconsin-Madison                                         |
| Torsten Hahmann         | University of Maine                                                     |
| Brodaric Boyan          | Natural Resources Canada                                                |
| Gaurav Sinha            | Ohio University                                                         |
| Charles F. Vardeman II  | University of Notre Dame                                                |
| Mark Schildhauer        | University of California, Santa Barbara                                 |
| Steven Chong            | University of Arizona                                                   |


\newpage
## A.6 Network analysis supplemental figures

![**Figure A3** In degree distribution of the envoPolar subset analyzed as a network.](figures/supplemental/in_degree_distribution.jpeg){ width=70% }

![**Figure A4** Out degree distribution of the envoPolar subset analyzed as a network.](figures/supplemental/out_degree_distribution.jpeg){ width=70% }

![**Figure A5** Plot of betweenness centrality as a function of number of neighbors of nodes from the envoPolar subset analyzed as a network. ](figures/supplemental/betweenness_centrality.jpeg){ width=70% }


\newpage

## A.7 Estimated user story simulated querying expertise

Estimated user stories were developed to evaluate the proficiencies of users of basic, intermediate or advanced querying expertise for performing semantic queryies of the model datastore.

The predicted users were tested with two mobilization tasks. 1) mobilizing annotated with an exclusive *and* intersection of two ontology terms, 2) mobilizing data annotated as being about parts associated with an ontology term.

Exclusive *and* querying cases used in the first task involved the following pairs of ontology terms: NCBITaxon:*Bacteria* [NCBITaxon_2] and NCBITaxon*Archaea* [NCBITaxon_2157], PATO:*concentration of* [PATO_0000033] and CHEBI*chlorophyll a* [CHEBI_18230], ENVO:*marine current* [ENVO_01000067] and PATO:*velocity* [PATO_0002242], PCO:*microbial community* [PCO_1000004] and PCO:*species diversity* [PCO_0000019], ENVO:sea ice* [ENVO_00002200] and PATO:depth* [PATO_0001595], ENVO:sea ice* [ENVO_00002200] and PATO:*temperature* [PATO_0000146], ENVO:*sea water* [ENVO_00002149] and CHEBI*chlorophyll a* [CHEBI_18230], ENVO:*snow* [ENVO_01000406] and PATO:*thickness* [PATO_0000915].

Data about parts associated with an ontology term querying cases used in the second task involved the following term annotations by which to query for data: ENVO:*brine channel* [ENVO_03000041], CHEBI:*carbon atom* [CHEBI_27594], CHEBI:*cation* [CHEBI_36916], IAO:*centrally registered identifier symbol* [IAO_0000577], ENVO:*glacier* [ENVO_00000133], ENVO:*marine biome* [ENVO_00000447], ENVO:*melt pond* [ENVO_03000040], and finally ENVO:*ocean* [ENVO_00000015].

The predicted user stories were programed to have knowledge of a subset of the turtle data annotation querying case property paths used in the example datastore. The querying cases the various user stories were programed to include are shown in **Table A5**.

: **Table A5** Shows the SPARQL querying cases which were included for each of the predicted user stories of various querying expertise levels.

+---------------+-----------------------------+
|Expertise level|querying cases used          |
+===============+=============================+
| basic         | 1,2,3                       |
+---------------+-----------------------------+
| intermediate  | 1,2,3,6                     |
+---------------+-----------------------------+
| advanced      | 1,2,3,6,7,8,9               |
+---------------+-----------------------------+
| complete model| all                         |
+---------------+-----------------------------+

The following code block shows sudo-code representations of the querying cases which were included in the user story estimating basic querying expertise.

```
X in (X)
X1-Xn in (X1 or X2 or ...)
X1-Xn in (X1 and X2 and ...)
```
The following code block shows sudo-code representations of the querying cases which were included in the user story estimating intermediate querying expertise.

```
X in (X)
X1-Xn in (X1 or X2 or ...)
X1-Xn in (X1 and X2 and ...)
Y in (X1 and X2 ... and ('any property' some Y))
```

The following code block shows sudo-code representations of the querying cases which were included in the user story estimating advanced querying expertise.

```
X in (X)
X1-Xn in (X1 or X2 or ...)
X1-Xn in (X1 and X2 and ...)
Y in (X1 and X2 ... and ('any property' some Y))
Y1-Yn in (X1 and X2 ... and ('any property' some (Y1 and Y2 and ... )))
Y1-Yn in (X1 and X2 ... and ('any property' some (Y1 or Y2 or ... )))
Z in (X1 and X2 ... and ('any property' some (Y1 and Y2 and ... and ('any property' some Z))))
```

\newpage

The following code block shows sudo-code representations of all the querying cases which were included to query for all annotated data included in the  model datastore.

```
X in (X)
X1-Xn in (X1 or X2 or ...)
X1-Xn in (X1 and X2 and ...)
X1-Xn in ((X1 or X2 or ...) and ... )
Y and Z in (X1 and X2 ... and ('any property' some Y and 'any property' some Z))
Y in (X1 and X2 ... and ('any property' some Y))
Y1-Yn in (X1 and X2 ... and ('any property' some (Y1 and Y2 and ... )))
Y1-Yn in (X1 and X2 ... and ('any property' some (Y1 or Y2 or ... )))
Z in (X1 and X2 ... and ('any property' some (Y1 and Y2 and ... and ('any property' some Z))))
Y in (W and ('any property' some ('any property' some X) and ('any property' some (Y and 'any property' some Z))))
Z in (W and ('any property' some ('any property' some X) and ('any property' some (Y and 'any property' some Z))))
X1-n in (W1 and W2 ... and 'any property' min N (X1 and X2 ... and  'any property' some (Y1 and Y2 and ... 'any property' some Z)))
Y1-n in (W1 and W2 ... and 'any property' min N (X1 and X2 ... and  'any property' some (Y1 and Y2 and ... 'any property' some Z)))
Z in (W1 and W2 ... and 'any property' min N (X1 and X2 ... and  'any property' some (Y1 and Y2 and ... 'any property' some Z)))
```

## A.8 github repository

All data used and generated in the course of this work is available from the following github repository available from: https://github.com/kaiiam/kblumberg_masters_thesis/
