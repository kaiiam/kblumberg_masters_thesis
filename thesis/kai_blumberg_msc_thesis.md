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

The scientific community is faced with the challenge of managing ever increasing quantities of environmental and genomic data which are often published with ambiguous or unstated relationships between data types. Ontologies represent expert scientific knowledge in human- and machine-readable formats. Such expert knowledge can be used to annotate data, giving it context to be linked to other data, as well as be understood by machine agents tasked with retrieving such data. Coming are massive quantities of interdisciplinary environmental and genomic data which left unmanaged, will likely lack the capacity to be analyzed in combination. Here I address questions about what can be done to prepare such interdisciplinary data to be interconnected using ontologies to in order to facilitate future computer-automated processing of such data. In this work I demonstrate that ontologies can be used to perform a variety of tasks related to the interconnection of information data and knowledge, I demonstrate how environmental and genomic ontology knowledge can be used to interconnect and analyze environmentally-annotated genomic data. I also analyze how ontologies can be used to facilitate the discovery and retrieval information and data about a phenomenon of interest. Additionally, I show that ontologies can be used to track the provenance of information and knowledge such as authors contributing to ontology terms. Furthermore, I show that uniform and repetitive annotation patterns can aid in the mobilization of data annotated with ontology terms. Finally, in terms of limitations, I show that more knowledge is required to be input into an example polar knowledge ontology in order for that ontology to be better able to lead researchers to new information based on input information. Overall my results indicate that ontologies are fit for the purpose of annotating and interconnecting interdisciplinary data. A potential scope for future work could involve interfacing the environmental and genomic ontologies with future environmental sensor networks, allowing for sensor outputs to directly answer questions relevant to the field of marine microbiology.


\pagebreak
# Abbreviations

**Acronyms**

ANY23: Anything To Triples

AWI: Alfred Wegener Institute Helmholtz Centre for Polar and Marine Research

BFO: Basic Formal Ontology

DOI: Digital Object Identifier

ECOCORE: Ontology of Core Ecological Entities

ENVO: Environment Ontology

FRAM: FRontiers in Arctic marine Monitoring

FAIR: Findable Accessible Interoperable and Reusable

IACS: International Association of Cryospheric Sciences

IAO: Information Artifact Ontology

NASA: National Aeronautics and Space Administration

NOAA: National Oceanic and Atmospheric Administration

OBCS: Ontology of Biological and Clinical Statistics

OBO: Open Biological and Biomedical Ontology

ORCID: Open Researcher and Contributor ID

ORF: Open Reading Frame

OWL: Web Ontology Language

PATO: Phenotypic Quality Ontology

PCA: Principal Component Analysis

PCoA: Principal Coordinate Analysis

PCO: Population and Community Ontology

RDF: Resource Description Framework

RO: Relations Ontology

SPARQL: SPARQL Protocol and RDF Query Language

SWEET: Semantic Web for Earth and Environmental Technology

URI: Uniform Resource Identifier

\pagebreak

**Python scripts**

In this document these scripts are referred to by their abbreviated version names e.g. py.x, and are provided in D.S.2.

py.1: create_rdf_triples_from_csv_files.py

py.2: histogram_median.py

py.3: merge_triples_to_datastore.py

py.4: network_distribution_stats.py

py.5: query_annotation_of_data_files_data_or_columns_about_input.py

py.6: query_data_set_references.py

py.7: query_for_class.py

py.8: query_for_classes_linked_by_input_classes_and_input_properties.py

py.9: query_for_created_by.py

py.10: query_for_data_about_exclusive_and.py

py.11: query_for_parts_associated_with_input_class.py

py.12: query_for_property.py

py.13: query_for_subclasses_of_input_purl.py

py.14: query_for_subproperties_of_input_purl.py

py.15: query_for_term_editor.py

py.16: query_GO_annotation_of_data_files_csv_annotations_columns.py


**R scripts**

In this document these scripts are referred to by their abbreviated version names e.g. R.x, and are provided in D.S.2.

R.1: data_set_references.r

R.2: degree_calculation.r

R.3: pca_analysis.r

R.4: pcoa_analysis.r

R.5: querying_exclusive_AND_annotations.r

R.6: query_parts_of_annotation.r


\pagebreak
# 1. Introduction

The Earth system is facing unprecedented anthropogenic pressures which have the potential to destabilize critical biophysical systems, triggering irreversible environmental changes [@Rockström_2009]. To address the broad scope of climate change interdisciplinary scientific action is required of the scientific community [@Lenhard_2006], unfortunately interdisciplinarity is not a prominent feature of climate research [@Bjurstr_m_2011]. Hence, strategies to link complex and differentially structured data generated from interdisciplinary sources are needed [@Madin_2007]. This will only become more important as it has been predicted that more scientific data will be created in the next decade then has been in the entire course of human history [@cox]. For example the upcoming United Nations decade of ocean science for sustainable development 2021-2030 [@UN_decade_ocean] will likely bring an influx of heterogeneous environmental observatory data collected from sensor networks [@Broring_2011]. In order to prevent these large quantities of information and data from contributing to uncertainty rather than reducing it [@Hortal_2015], strategies are needed to store environmental data in a way which captures subtleties of the data’s structure, content and inter-relationships [@Madin_2007].

Currently scientific knowledge, information and data about environmental systems are published in wide variety of heterogeneous formats [@Horsburgh_2009], often with ambiguous or unstated relationships between data types. Published scientific data could be metaphorically described as a wild and untamed wilderness of knowledge, information and data which are commonly not interoperable, i.e. lacking the capacity to be used in combination with one another [@Wilkinson_2016]. Interoperability is a crucial component in the FAIR guiding principles for scientific data management and stewardship, and is required to make published data reusable to both human and machine agents [@Wilkinson_2016]. Facing the oncoming deluge of large data, this work addresses the question of what can be done to integrate and prepare interdisciplinary earth systems knowledge, information and data to be machine-actionable, i.e. processable by computational systems in an automated and interoperable fashion [@Rauber].

Semantics, i.e. the meanings of words or digital objects [@Wilkinson_2016], are needed to make knowledge, information and data work interoperably at a machine-accessible level. Interoperable semantics can be used by machine agents to retrieve and analyze data relevant to a task of study [@Wilkinson_2016], facilitating the process of knowledge synthesis. Knowledge representation a field of artificial intelligence makes use of machine-actionable knowledge, information and data, by integrating it into computer system intended to solve complicated tasks [@brachman1985readings]. Knowledge representation systems have been successful used in medical domains to perform tasks such as computer-aided diagnosis of medical conditions [@Takahashi_2017]. Knowledge representation models can be constructed from expert knowledge which is represented in ontologies.

An ontology is a hierarchically structured, machine and human readable semantic representation of the knowledge used by experts to describe entities in the universe, and capture the relationships between them [@Smith_2007]. In informatics, ontologies exist in the form of a knowledge graph, where nodes represent entities, and edges represent logical relations linking entities together (i.e. axioms). In medical domains, ontologies have been used to interconnect disparate data and information, to enable computational interrogation of models to reveal underlying relationships. For example the Monarch Initiative uses an ontology-based strategy to integrate genotype–phenotype data from various sources and species, enabling users to explore phenotypic and genotypic relationships across species [@Mungall_2016].

Analogously to what has been done in medical domains, the use of federated ontology semantics have been discussed as having the potential to link data about phenotypes with environments [@Thessen_2015], as well as environmental and genomic datasets [@Walls_2014]. This would allow for users to leverage knowledge, information and data connected by ontologies to ask questions such as "Which crop varieties are expected to do well in a particular location over the next century?" [@Thessen_2015], or "Can we gather all metagenomes collected from insects found in soil?" [@Walls_2014].

Working toward the objective of using ontologies to interlink environmental knowledge, information and data to conduct future machine-focused ecological analyses, I evaluated the fitness for purpose of using ontologies to integrate interdisciplinary data. In order to do this I created a model datastore consisting of various types of interdisciplinary polar and microbial omics data. The data in this datastore is annotated with ontology semantics and stored in a machine-accessible format to simulate a linked open data environment, i.e. a collection of data which can be accessed by machine agents. I made use of Polar data as the subject of the interdisciplinary data integration analysis, as polar systems are particularly vulnerable to the effects of climate change [@Wang_2009]. Polar regions are subject to the effects of polar amplification, in which the effects of global warming produce larger temperature changes at the poles than elsewhere on the planet [@Lee_2014]. Resulting from such effects polar regions are predicted to be free of ice within the next 20 to 50 years [@Wang_2009]. In addition to the polar environmental data I also included environmental microbial omics data in my analysis to test of ontology knowledge-representation artifacts are fit for purpose to integrate interdisciplinary data.

To explore how ontology knowledge representations can fill the niche of improving informatics interactions in the wilderness of scientific data, I developed methods to test if ontologies are fit to interconnect interdisciplinary knowledge, information and data. Following the scientific method to conduct semantic research, see **A.1**, I make observations about existing knowledge and information. I gather such knowledge and information and semantically *capture* it i.e. encoded into an ontology so it can be formally represented to both humans and machine agents. Next I make hypotheses as to whether ontology-encoded knowledge can be used to gather other information and data. I then formalize these hypotheses as competency questions which are analogous to the questions asked by employers during job interviews to judge the competence of prospective employees [@calvo2017analysis]. These competency questions are specific, targeted and directed questions intended to evaluate how well ontology knowledge representation systems performs essential knowledge-representation and data-mobilization related tasks. In this work I refer to the competency questions I have created with the abbreviation CQ followed by the question number in parenthesis. Next I develop methods centered around answering competency questions to test the interaction of ontology knowledge graphs and datasets. In this work the process of data collection involves both the collection of datasets from my datastore, as well as, the collection of knowledge from an ontology knowledge graph. My data analysis involves analyzing the interactions between the collected data and knowledge. Finally I draw conclusions from the results of analyzing the interactions between the collected data and knowledge.

In this work, I follow the ontology term labeling convention set by Buttigieg et al. (2013) [@Buttigieg_2013]. I refer to ontology terms (also known as classes) by writing them in italics with a prefix denoting the ontology namespace from which the term was sourced. Proceeding the italicized label, I write the unique identifier of each term’s Uniform Resource Identifier in brackets. For example the Environment Ontology term *sea ice formation process* is referred to as 'ENVO:*sea ice formation process* [ENVO_03000044]'.

The first and possibly most important task for which I tested ontologies for their competency to perform, was to see if they could be used to interconnect environmental and omics data. Linking environmental and omics data to uncover interactions between genomes and environments is a topical challenge in genomic and medical disciplines [@Fave_2018]. In a recent study linking environmental and omics data, Favé et al. (2018) were able to determine that environmental factors such as air pollution were responsible for disease risk phenotype outcomes rather than ancestral genotypes [@Fave_2018].

Within environmental domains, ontology-interconnected genomic and environmental data would allow for machine agents to act upon large environmental genomic datasets such as the TARA Oceans project [@Ainsworth_2013], the Global Ocean Sampling Expedition [@Ledford_2007] and the Hawaii Ocean Time-series program [@KARL1996129]. Systematic machine operation over such a wealth of knowledge has the potential to help answer future ecological questions.

In principal ontologies should be able to interconnect environmental and genomic data. One of the most widely used ontologies in biomedical domains is the Gene Ontology (GO), which provides semantic representations describing the roles of genes and gene products [@Ashburner_2000]. The Gene Ontology along with other ontologies are part of the Open Biological and Biomedical Ontology (OBO) Foundry and Library [@Smith_2007]. These ontologies use common upper level semantic models and shared relations so they can work interoperably, creating a unified multidisciplinary knowledge representation model [@Walls_2014]. One such OBO ontology the Environment Ontology (ENVO) provides semantic descriptions of environments [@Buttigieg_2013][@Buttigieg_2016]. Although ENVO and GO make use of interoperable semantics, efforts to use these ontologies in combination, have infrequently been attempted [@Henschel_2015]. Assessing if ontologies can be used to interconnect environmental and genomic data in order to compare genetic differences between environments, I formulated my first competency question:

> "What are the relative proportions of oxidation-reduction process genes in various types of marine biomes?"
$$CQ (1)$$

This question evaluates a variety of ontology competencies. First it tests if it is possible to use ontologies to interconnect genomic and environmental data, retrieving data which is about a GO:*oxidation-reduction process* [GO_0055114 as well as an ENVO:*marine biome* [ENVO_00000447]. The question doesn't just test if there is a specific type of GO data about ENVO:*marine biome*s [ENVO_00000447], but it tests if the knowledge contained in the knowledge hierarchy about different types of ENVO:*marine biome*s [ENVO_00000447] can be leveraged to determine if any of those subclass have information about this specific GO term. Simulating the kinds of questions a microbial ecologist would ask about genes which differentiate various ENVO:*marine biome*s [ENVO_00000447] I asked:

> "What are the relative proportions of vitamin biosynthetic process genes in various types of marine biomes?"
$$CQ (2)$$

This question is intended to further explore if ontologies can be used to facilitate the collection of data by which to perform comparative genomic analyses. The results of the second question prompted further analysis leading me to ask:

> "What genomic features may help to explain the differences in riboflavin proportions between deep and shallow marine benthic biomes?"
$$CQ (3)$$

To answer this I explored terms from higher level GO hierarchies of GO*molecular_function*s [GO_0003674] and GO:*biological_process* [GO_0008150] to find information relevant to transition metal binding and transport functions.

Next, I wanted to test what other kinds of expert knowledge were present in the higher level GO ontology GO:*biological_process* [GO_0008150] hierarchy which may help to differentiate ENVO:*marine biome*s [ENVO_00000447] samples. Hence I created a competency question asking:

> "What biological processes differentiate various types of marine benthic biomes?"
$$CQ (4)$$

As there are very many terms which are subclasses of the upper level GO:*biological_process* [GO_0008150] term, I used the GO:*biological_process* [GO_0008150] hierarchy see **Figure A2**, to find a more specific term to investigate, to see if it could help to differentiate ENVO:*marine biome*s [ENVO_00000447] samples. Testing if GO:*cellular amino acid biosynthetic process* [GO_0008652] subclasses might be different in the various biomes, I asked:

> "What cellular amino acid biosynthetic processes differentiate various types of marine benthic biomes?"
$$CQ (5)$$

Drawing from the results of CQ (5) to further leverage the GO biological processes hierarchy to see if specific GO terms could be found which are are completely different in ENVO:*marine biome*s [ENVO_00000447] samples, I asked:

> "What serine family amino acid biosynthetic processes differentiate various types of marine benthic biomes?"
$$CQ (6)$$

Although the interconnection of genomic and environmental data is an important competency by which to assess ontologies for their ability to interconnect interdisciplinary data, it is far from being the only use case for ontologies to interconnect knowledge, information and data. I created the following question to assess the fitness of ontologies to be able to navigate machine-accessible information to discover data relevant to a phenomena of interest. I tested this with the competency question asking:

> What data about environmental factors with the potential to influence the dynamics of a sea-ice associated phytoplankton community could be collected using an ontology?
$$CQ (7)$$

Discovery of data is an important task for ontologies to be able to perform, similarity I wanted to assess if ontologies can also be used by scientists to discover new knowledge from a knowledge graph which is related to stated input knowledge. Operating on the envoPolar subset of ENVO I asked:

> "Is the ontology knowledge graph of the envoPolar subset sufficiently well connected to be able to lead researchers to new knowledge via unstated linkages to identified knowledge?"
$$CQ (8)$$

Using ontologies to guide the discovery of knowledge is an important competency by which to assess the fitness for purpose of ontologies to interconnect interdisciplinary knowledge. To take this a step further, I wanted to investigate if ontologies could be used more generally to identify and track the provenance of scientific knowledge, data, or other information, such as ontology term authors. To test if ontologies could be used to track information about scientific knowledge, specifically if they could be used to connect users to primary literature associated with datasets annotated with ontology terms, I asked the following question:

> "What are all the papers which reference any data set, which is about a part of a marine biome?"
$$CQ (9)$$

Showing that it is possible to use ontologies to link datasets and publication, I wanted to further evaluate the potential for ontologies to link term authors to the knowledge they helped to generate to facilitate future scientific networking endeavors. To evaluate this I asked the question:

> "How well do the Environment Ontology and the Environment Ontology Polar subset connect authors of terms to the information they helped to encode?"
$$CQ (10)$$

Tracking the provenance of knowledge, data and information are important tasks for ontologies to be able to facilitate. If in the future ontologies were to be used to track the provenance of larger scale knowledge, information and data it is important to address how robust such ontology-enabled systems would be toward semantic-challenges such as the inclusion of potentially conflicting expert knowledge, or changes made to their underlying semantic models. Addressing the former, I evaluated the question of:

> "Are ontology knowledge representations resilient to the input of new information which may contain definitional discrepancies?"
$$CQ (11)$$

To address the latter concern, I evaluated ontologies for potential susceptibilities to changes in their underlying semantic models, by asking the question:

> "What percentages of data items discovered to be about participants in sea ice formation processes would be retrievable if changes were to be made to the underlying semantic models used by OBO ontologies, such as not using hierarchical subclass structures to represent knowledge, or not using structured relations from the Relations Ontology?"
$$CQ (12)$$

Susceptibility to changes in semantic models constitute theoretical concerns, which I discuss in this work can be avoided through the use of well-established and well-structured semantic models. To evaluate how practical it would be for users of different levels of querying expertise to retrieve ontology-annotated machine-accessible data, I asked the following question:

> "What level of querying expertise is required to access the various types of data contained in the example polar datastore?"
$$CQ (13)$$

Finally, to assess if the process of encoding expert ecological knowledge into an ontology knowledge graph aids to clarify the understanding of ecological phenomena, I asked the question:

> "Does the inclusion of novel expert knowledge about phenomena relating to plankton ecology into the ENVO knowledge graph aid to better understand the interconnections of such phenomena?
$$CQ (14)$$


\pagebreak

# 2. Materials and Methods

## 2.1 Creating an RDF datastore for polar environmental genomics

For this work I created a polar-themed RDF datastore of machine-accessible and ontology-annotated environmental and genomic datasets. See appendix **A.2** for the details of the employed datasets. The first 9 datasets were generated by working groups at the AWI, many of which are sourced from the FRAM [@Soltwedel_2013], and Hausgarten [@Soltwedel_2005] observatory programs, which are about: inorganic nutrients, physical oceanography measurements, seawater chlorophyll, organismal chlorophyll, biogenic particle flux, sea ice snow height, sea ice thickness, snow depth and surface light transmission, and ice-algae chlorophyll. The last two datasets are processed outputs from omics data sets, the first of which consists of 16S taxonomic and Pfam2GO annotation tables generated from unpublished sediment metagenomes provided by Josephine Z Rapp, the second consists of Pfam2GO annotation tables generated from unpublished sediment metatranscriptomes provided by David Probandt, and Matthew Schechter.

The 16S taxonomic and Pfam2GO annotation tables used, had previously been processed from raw genomic and transcriptomic data using the following tools: BBDuk (Version 35.68 for metagenomes, Version 36.92 for metatranscriptomes) from the BBTools suite [@Bushnell_bbmap] for read quality control, SortMeRNA (Version 2.0, 29/11/2014) [@Kopylova_2012] for ribosomal RNA filtering, the SINA alignment tool (Version 1.2.11, revision 21227) [@Pruesse_2012] for 16S ribosomal RNA taxonomic classification, FragGeneScan (Version 1.20) [@Rho_2010] for ORF-prediction, the Ultra-fast Protein domain Classification tool (UProC) (1.2.0) [@Meinicke_2014] for ORF-annotation with PFAM domains, and the Pfam2GO annotations page (January 2016 version) available from  http://www.geneontology.org/external2go/pfam2go [@Mitchell_2017] for mapping PFAM domains to GO terms.

The datastore was created by converting comma separated value (CSV) files into the RDF specification [@richard_cyganiak_rdf_2014] turtle format [@david_beckett_rdf_2014], using the script py.1, which makes use of the Apache Anything To Triples (any23) command line *rover* tool (Version 2.1) [@any23]. Turtle formatted data along with semantic data annotation files were merged into a single datastore file using the script py.3. The datastore creation workflow is available in D.S.3.1.

## 2.2 Annotation of data with semantic resources

Semantic annotation of the example data was conducted in the RDF serialization turtle facilitate scripting Web Ontology Language (OWL) [@sean_bechhofer_owl_2004] code in RDF. Annotations make use ontology terms from the Open Biomedical Ontologies (OBO) Foundry and Library [@Smith_2007]. Ontology terms were searched for using the Ontobee linked data server [@Ong2017]. Ontology term annotation for the example polar datastore made frequent use of ENVO terms from the envoPolar subset which was primarily developed during the *Ecotone* [@pier_luigi_buttigieg_2017_573849], *Polar express* [@chris_mungall_2017_546433], and *Hot tub time machine*
[@chris_mungall_2017_438339] ENVO releases. Semantic annotations of datasets are available in D.S.3.1.


![**Figure 1:** Content from a CSV file which has been semantically annotated in the RDF serialization turtle. **A**) The CSV file is annotated in turtle as being about chlorophyll a which is part of a marine water body. **B**) A column from the CSV files is annotated in turtle as being about a concentration of chlorophyll a in seawater.  ](figures/turtle_serialization.pdf)


**Figure 2** Shows an example of the post-compositional data annotation of datasets using ontology terms. The example is of a data column which is about a *chlorophyll a concentration* in *sea water*. Expressed as an ontology axiom, we have a data column: which is BFO:*part of* [BFO_0000050] some OBCS:*data matrix* [OBCS_0000120] and IAO:*is about* [IAO_0000136] some PATO:*concentration of* [PATO_0000033] and RO:*inheres in* [RO_0000052] some CHEBI:*chlorophyll a* [CHEBI_18230] and BFO:*part of* [BFO_0000050] some ENVO:*sea water* [ENVO_00002149].

![**Figure 2:** RDF specification turtle code to annotate a data column from a CSV file. **A**) The CSV file data column is labeled *chlorophyll A*. **B**) The data column is BFO:*part of* [BFO_0000050] some OBCS:*data matrix* [OBCS_0000120]. **C**) The data matrix column IAO:*is about* [IAO_0000136] a list of annotation terms. **D**) The object is about a PATO:*concentration of* [PATO_0000033]. **E**) The concentration measured is of CHEBI:*chlorophyll a* [CHEBI_18230]. **F**) The *chlorophyll a* is BFO:*part
of* [BFO_0000050] some ENVO:*sea water* [ENVO_00002149]. ](figures/data_annotation_diagram.pdf){width=100%}


\pagebreak  
## 2.3 SPARQL querying

Scripts were written in Python (Version 2.7.12) [@python] and make use of the rdflib module (Version: 4.2.2) an RDF parsing Python library [@team_rdflib] to parse the example RDF datastore, as well as assemble and execute SPARQL queries against the datastore, or local RDF turtle serialization versions of local copies of ontologies. Additional SPARQL queries were submitted to the Ontobee programmatic SPARQL endpoint available from http://sparql.hegroup.org/sparql/ [@Ong2017]. A demonstration of the process by which a SPARQL query is executed is shown in **Figure 3**. Item **A** shows a SPARQL query, which is created in a Python script based on some user input class (shown in green). This query selects some unknown thing called ?X (shown in red), where ?X is a subclass of some input class, and ?X is part of some class Y (shown in orange). Item **B** shows a knowledge graph of ontology classes and the relations connecting them. The knowledge graph could either be a local copy of an ontology or the merged set of a web accessible OBO ontologies available to query from the Ontobee programmatic SPARQL endpoint. Item **C** shows how the SPARQL query navigates the relations in the knowledge graph to find a term which satisfies the input conditions. Item **D** shows the successful retrieval of the previously unknown ?X term, discovered from the knowledge graph and returned as a class of known type X.

![**Figure 3:** Performing a SPARQL query and retrieving results from a knowledge graph. **A**) SPARQL code for a query which looks for an object ?X which is a subclass of an input class and part of Y. **B**) A knowledge graph of ontology terms and their interconnecting relations. **C**) The process by which the SPARQL query is executed by navigating the knowledge graph to find some unknown ?X class which is both a subclass of some input class and part of some Y. **D**) The end result of the query in which the previously unknown ?X class is discovered from the knowledge graph and returned as a known class X. ](figures/query_illustration.pdf){width=80%}

\pagebreak
## 2.4 Interconnecting genomic and environmental data via ontologies

The following methods were used to answer CQ (1-6), and can be found in D.S.3.2. The python script py.16 was used to retrieve relative proportions of environmentally-annotated omics data, the script makes use of a list of ENVO:*marine benthic biomes* [ENVO_01000024] subclasses terms and a list of GO terms, which are subclasses of a GO term of interest. The GO and ENVO subclasses lists were created using the script py.13, which queries for subclasses of an input term.

The script py.16 was used to query the local datastore for data matrices about an input list of ENVO classes, for data matrix columns which are annotated with GO terms matching an input list of GO classes. The script makes use of the Python Data Analysis Library pandas (Version: 0.22.0) [@python_pandas]. The script returns a data table with rows corresponding to samples, and columns corresponding to relative proportions of GO terms. Relative proportions of metagenomic and metatranscriptomic samples were calculated by querying for subclasses of a GO term of interest, querying for all GO terms in the corresponding GO:*biological process* [GO_0008150] or GO:*molecular function* [GO_0003674] GO hierarchy, then dividing the counts of individual terms by the sum of the total counts of biological process or molecular function terms.

For CQ (4-6), *sites* by *species* principal coordinate analyses were conducted on data matrices of relative GO term proportions. In which *sites* corresponded to the samples annotated with ENVO classes of various ENVO:*marine benthic biomes* [ENVO_01000024], and *species* corresponded to relative proportions of GO terms. This was conducted in R [@R_core] (Version 3.3.2), using the script R.4. In script R.4 the data matrices of relative GO term proportions were standardized using the decostand function which made use of a Hellinger transformation, converted into a Bray-Curtis dissimilarity matrix using the vegdist function with standard parameters, prior to PCoA, which was conducted using the vegan package (Version 2.4-3) [@vegan].


## 2.5 Ontology-guided data collection

The following methods were used to answer CQ (7), and can be found in D.S.3.3. First a hypothetical ENVO term ENVO:*environment determined by a phytoplankton community associated with sea-ice* [URI pending], was proposed, which would include the subclass axioms: ENVO:*environmental system determined by a community* [URI pending], ENVO:*determined by* [ENVO_2100001] some PCO:*phytoplankton community* [URI pending], RO:*located in* [RO_0001025] some (ENVO:*seawater* [ENVO_00002149] and (RO:*part of* [BFO_0000050] some ENVO:*marine water body* [ENVO_00001999])), and finally RO:*adjacent to* [RO_0002220] some ENVO:*sea ice* [ENVO_00002200]. The hypothetical term follows the design pattern of several preexisting terms in the Environment Ontology such as ENVO:*environment determined by a biofilm on a fungal surface* [ENVO_01001035] within the ENVO:*environmental system* [ENVO_01000254] hierarchy.

The classes ENVO:*marine water body* [ENVO_00001999], ENVO:*seawater* [ENVO_00002149], and ENVO:*sea ice* [ENVO_00002200], were included as subclass axioms of the hypothetical term ENVO:*environment determined by a phytoplankton community associated with sea-ice* [URI pending], these classes were passed to the Python script py.13 which queried for subclasses of each of these classes. The resulting subclass lists were concatenated, and then passed to script py.5 to query the datastore for data about any of these classes. This simulated the effect of querying for data about any class mentioned as a subclass axiom of the hypothetical ENVO:*environmental system determined by a community* [URI pending] term.

As a supplement to this work, see appendix **A.4** a PCA analysis was conducted on the data retrieved above. This was conducted in the script R.3 which made use of the vegan package [@vegan] (Version 2.4-3). Prior to PCA analysis, data was z-score standardized using the scale function with parameters: *center* and *scale* being set to *TRUE*.

## 2.6 Knowledge representation with human sources

The following methods were used to answer CQ (10), and can be found in D.S.3.4. Percentages of ENVO and envoPolar ontology terms annotated with a IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation referencing an ORCID were calculated using the following workflow. Local turtle specification versions of the ENVO and envoPolar v2017-08-22 *Planetary ecology* release [@pier_luigi_buttigieg_2017_846451] ontologies were exported to a local version formatted in the RDF turtle serialization using the standard Protégé [@Musen_2015][@protege] ``export as`` function. Python scripts py.7, py.9 and py.15 were used to perform SPARQL queries upon the local turtle ontology versions, for total numbers of ENVO terms and numbers of terms annotated with an IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation an ORCID. Percentages of ontology terms with IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] annotations were calculated from retrieved counts.

The demonstration of how to retrieve the current author contact information from an ORCID, was conducted as follows. A two-legged OAuth authorization request was sent to the ORCID application programming interface sandbox demonstration contact information retrieval service, issuing a token request for the information associated with the demonstration ORCID client identifier ``APP-NPXKK6HFN6TJ4YYI``. Such request was sent from the Linux command line using the curl data transfer tool (Version 7.47.0) using the following line of code:

```
curl "Accept: application/json" -d "client_id=APP-NPXKK6HFN6TJ4YYI" -d "client_secret=060c36f2-cce2-4f74-bde0-a17d8bb30a97" -d "scope=/read-public" -d "grant_type=client_credentials" "https://sandbox.orcid.org/oauth/token"
```
Making use of the returned authentication token ``2bd6d6b7-9438-4a5a-8f87-7e43d6eaac25``, a request for the email contact information associated with the demonstration ORCID client identifier was sent with curl (Version 7.47.0) using the follows line of code:

```
curl -i -H "Accept: application/vnd.orcid+xml" -H 'Authorization: Bearer 2bd6d6b7-9438-4a5a-8f87-7e43d6eaac25' 'https://api.sandbox.orcid.org/v2.0/0000-0002-9227-8514/email'
```
From the returned XML code block, the email address associated with the demonstration ORCID client identifier was parsed using the GNU grep command line tool (Version 2.25), resulting in the retrieval of the email address associated with the demonstration ORCID client identifier.



## 2.7 Connecting datasets and publications with overlapping knowledge referents

The following workflow addressing CQ (9) was used to retrieve DOIs of publications associated with datasets about parts of a ENVO:*marine biome* [ENVO_00000447] and is available from D.S.3.5. The Python script py.11 was used to query for ontology classes which are parts of or have parts which are an ENVO:*marine biome* [ENVO_00000447]. The resulting list of ontology terms which are parts associated with ENVO:*marine biome* [ENVO_00000447] were used to query the local datastore for all data from data matrix columns which are annotated with an oboInOwl:*hasDbXref* [hasDbXref] database cross reference using the py.6 Python script. Results were processed in script R.1.  

The oboInOwl:*hasDbXref* [hasDbXref] relation is commonly used to annotate ontology classes by referencing a source of knowledge used to define a class. In the datastore the oboInOwl:*hasDbXref* [hasDbXref] relation was used to annotate datasets with the papers which reference such datasets.


## 2.8 Glacial semantics community consultation and creation of proposed ontology terms

Referencing CQ (11), my participation in the Feb 2, 2018 VoCamp Glacier Ontology Hackathon community glacial-consultation session [@vocamp_2018] was an opportunity to consult with polar-related domain experts to improve the semantic representation of glacial-related knowledge. Drawing upon knowledge sourced from this event, as well as a variety of scientific publications from AWI polar domain experts [@Cherkasheva_2014][@Janout_2016], referencing CQ (14), I created ontology terms which I have proposed to be added the ENVO [@Buttigieg_2013][@Buttigieg_2016] PATO [@PATO_BioPortal] ECOCORE [@ecocore_2018] and PCO [@PCO__BioPortal] ontologies. These potential ontology terms were created following the best practices for BFO ontology development as outlined by Arp et al. (2015) [@Arp_2015], making use of the BFO to provide common hierarchical structures by which to characterize knowledge, and the RO [@obo-relations], to standardize the connections between represented knowledge. A complete description of these potential ontology terms, are provided in D.S.4.


## 2.9 Retrieval of classes linked by subclasses and subproperties

The following methods were used to answer CQ (12), and can be found in D.S.3.6. Retrieval of classes participating in subclasses of sea ice formation processes was conducted as follows. Subclasses the term ENVO:*sea ice formation process* [ENVO_03000044] were assembled using the py.13 script. Subproperties of RO:*has participant* [RO_0000057] were assembled using the py.14 script. The results of classes which participate in sea ice formation processes, were discovered using the py.8 script with the assembled subclasses of ENVO:*sea ice formation process* [ENVO_03000044] and subproperties of RO:*has participant* [RO_0000057]. This workflow which involves querying for subclasses an an input class, querying for subproperties of an input property and using them to search the knowledge graph for new classes of interest is documented in **Figure 4**.


![**Figure 4:** Ontology-guided knowledge-mobilization workflow in which classes and relations from ontologies are used int combination to discover new classes. **A**) The knowledge graph is queried for subclasses of a desired input class (shown in dark green and denoted with an asterisk), which yields subclasses of the input class (shown in various shades of green). **B**) The knowledge graph is queried for subproperties of an input property (shown in dark red and denoted with an asterisk), which yields subproperties of the input property (shown in various shades of red). **C**) Using both the subclasses of the input class and the subproperties of the input property, new classes (shown in orange) can be discovered from the knowledge graph which are related to one of the subclasses (in green) via one of the subproperties (in red). ](figures/query_classes_linked_by_subclasses_subproperties.pdf){width=100%}

I simulating how much of this data would be retrievable if there were changes made to the Relations Ontology, as well as if my datastore didn't employ hierarchically structured subclass relations to represent knowledge about classes and their subclasses. To simulate the lack of the RO, the script py.13 was used to find subclasses of ENVO:*sea ice formation process* [ENVO_03000044], and the results of which were directly passed to script py.5 to get data about these subclasses, without using script py.8 using RO relations to discover new classes.

To simulate if my datastore didn't employ hierarchically structured subclass relations to represent knowledge about classes and their subclasses, the script py.13 was not used to find subclasses of ENVO:*sea ice formation process* [ENVO_03000044] instead only the class ENVO:*sea ice formation process* [ENVO_03000044] was used, in combination with the subproperties of RO:*has participant* [RO_0000057] which were assembled with script py.14, to be passed to the py.8 script. Thus the py.8 script was only able to discover classes linked to ENVO:*sea ice formation process* [ENVO_03000044] by subproperties of RO:*has participant* [RO_0000057], missing the subclasses of ENVO:*sea ice formation process* [ENVO_03000044]. The results of which were passed to the script py.5 to retrieve data.

## 2.10 Delivering polar-focused knowledge products

Addressing CQ (8), the following methods were used to create a network from the ENVO polar subset, and can be found in D.S.3.7. The envoPolar subset from the ENVO v2017-08-22 *Planetary ecology* release [@pier_luigi_buttigieg_2017_846451] was used. The envoPolar owl file was exported to the RDF specification turtle using the software Protégé's standard `export as` function [@Musen_2015][@protege]. Python script py.7 was used to query for all classes and Python script py.12 was used to query for all property terms in the envoPolar subset. The results of which were used as inputs for the py.8 script to obtain the connections between all classes in the ontology. The resulting output consisting of subject classes, properties linking subject classes to target classes, and target classes, was used to create a network in the program cytoscape [@Shannon_2003].  

Network parameters of the envoPolar subset of ENVO were calculated using the cytoscape network analyzer, treating the graph as directed. Figures for the distribution of shortest path lengths, average clustering coefficient, in degree distribution, out degree distribution, and betweenness centrality were generated in cytoscape.

Calculations of mean and median values for the in-degree, out-degree and shortest path length distributions were conducted in the Python script py.2 using the statistics library Version: 1.0.3.5 [@python_statistics] from distribution data output by the cytoscape network analysis. Figures of the in-degree, out-degree and shortest path length distributions were created in the R script R.1.

Nodes of highest and lowest in-degree value were extracted manually from the envoPolar network in cytoscape.

## 2.11 Estimation of predicted-user data-mobilization proficiency

Lacking the scope to properly address CQ (13) by conducting an experiment on a study group of scientists with various proficiencies for performing semantic queries to retrieve data from the datastore, I instead estimated the performance of predicted user stories, as is done in agile software development [@user_story]. I created three categories of predicted user stories, for users of various SPARQL querying proficiencies, for more details see appendix **A.8**. The predicted users were modeled to have basic, intermediate or advanced querying expertise. I evaluated the performance of these predicted user stories based on the percentage of total data each would be able to retrieve from the datastore, when performing a variety of queries, the code for this can be found in D.S.3.8.

![**Figure 5:** The process by which I used estimated user stories of people with basic, intermediate and advanced querying expertise, in order to evaluate how much of the total data they would retrieve from the datastore. **A**) Querying scenario questions which the estimated user stories were asked to get data about, for example data about 'sea ice thickness' or data about 'part of' a 'marine biome'. **B**) The three categories of simulated user stories which had basic, intermediate or advanced expertise for performing SPARQL queries. **C**) The percentages of data which each estimated user story was able to retrieve for a given querying scenario. **D**) The complete set of data contained within the datastore about classes the querying scenario was attempting to retrieve.](figures/user_querying_scenarios.pdf){width=80%}

The basic user story was programed to only have a very limited understanding of how to perform SPARQL queries. The basic users were programed not to be able to perform queries of any axiomatic depth. They were limited to direct queries. The three querying cases basic users stores were programmed to execute are for 1) data about a class directly, 2) data about a class **and** other classes, 3) data about a class **or** other classes.

The intermediate user story was programed to be able to have moderate understanding of property path relationships and is  modeled to produce queries with a moderate amount of depth. For example queries about some class and *some property* another class.

The advanced user story was programmed to be able to have a fairly deep understanding of possible query paths.  For example queries about some class 1 and *some property* some class 2, and  *another property* some class 3. Although the advanced user story can handle queries of sufficient, they were programmed to only make use of regular pattern. They were not programmed to handle all possible data annotation property path irregularities present in the model datastore.

Two user story experiments were modeled. The first for mobilizing data annotated with an exclusive *and* intersections of two ontology terms was conducted as follows. Eight combinations of terms were used to query for data. For each combination, the py.13 script was used to query for subclasses of the first term in the intersection combination. Modified versions of the py.10 script were run using the list of subclasses generated from the first term in the intersection combination, along with the second term. Retrieving data matrix annotations and columns annotated as being about the intersection of the subclasses of the first term with the second term.

The second user story experiments involved querying for data annotated as being about parts associated with an ontology term, was conducted as follows. Eight terms were queried for data annotated with parts associated therewith. For each term, the py.11 script was used to query for terms corresponding to associated parts of the input term. Modified versions of the py.10 script were run using the list of associated parts derived from the first script. Retrieving data matrices and data points annotated as being about parts associated with the input term.

For both user story experiments, percentages of retrieved data matrix columns, annotations, points and data matrices were calculated compared with the results derived from an unmodified version of the py.10 or py.11 scripts which retrieved 100% of available data. A list of querying cases used to differentiate the levels of querying expertise is available in the mobilizing ontology annotated data supplemental section.

\pagebreak  
# 3. Results

## 3.1 Comparing ontology-mobilized environmentally-annotated omics data


Making use of the interoperable Gene and Environment ontology semantics, I was able to mobilize environmentally-annotated omics data to address CQ (1). The results of querying the datastore for the genomic and transcriptomic proportions of sequences matching GO:*oxidation-reduction process* [GO_0055114] genes, in various ENVO:*marine biome* [ENVO_00000447], relative to the total numbers of GO:*biological process* [GO_0008150] counts are shown in **Table 1**.

: **Table 1:** Results of a query for the relative genomic and transcriptomic proportions of GO:*oxidation-reduction process* [GO_0055114] genes, in various ENVO:*marine biome*s [ENVO_00000447].

| term                                                                     | ENVO:*marine abyssal zone biome* [ENVO_01000027] | ENVO:*marine bathyal zone biome* [ENVO_01000026] | ENVO:*marine neritic benthic zone biome* [ENVO_01000025] |
|:-------------------------------------------------------------------------|:-------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------------|
| GO:*oxidation-reduction process* [GO_0055114]                            | 18.15                                            | 18.39                                            | 9.36                                                     |
| GO:*aerobic respiration* [GO_0009060]                                    | 0.23                                             | 0.26                                             | 0.87                                                     |
| GO:*methanogenesis* [GO_0015948]                                         | 0.11                                             | 0.12                                             | 0.06                                                     |
| GO:*ATP synthesis coupled electron transport* [GO_0042773]               | 0.06                                             | 0.06                                             | 0.04                                                     |
| GO:*L-lysine catabolic process to acetate* [GO_0019475]                  | 0.06                                             | 0.07                                             | 0.01                                                     |
| GO:*respiratory electron transport chain* [GO_0022904]                   | 0.03                                             | 0.03                                             | 0.13                                                     |
| GO:*mitochondrial electron transport, NADH to ubiquinone* [GO_0006120]   | 0.02                                             | 0.02                                             | 0.01                                                     |
| GO:*electron transport chain* [GO_0022900]                               | 0.02                                             | 0.02                                             | 0.05                                                     |
| GO:*fatty acid beta-oxidation using acyl-CoA dehydrogenase* [GO_0033539] | 0.02                                             | 0.02                                             | 0.01                                                     |
| GO:*anaerobic electron transport chain* [GO_0019645]                     | 0.01                                             | 0.01                                             | 0.00                                                     |
| GO:*glycogen biosynthetic process* [GO_0005978]                          | 0.00                                             | 0.00                                             | 0.01                                                     |
| GO:*photosynthetic electron transport in photosystem II* [GO_0009772]    | 0.00                                             | 0.00                                             | 16.08                                                    |
| GO:*photosynthetic electron transport chain* [GO_0009767]                | 0.00                                             | 0.00                                             | 1.38                                                     |

Analysis of these results show deep biome samples ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026], had double the relative proportions of non-specific annotations to general oxidation-reduction reduction processes ~18%, relative to ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples. In contrast, ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples had three fold increases in GO:*aerobic respiration* [GO_0009060] gene proportions relative to the deep samples.

Deep samples had nearly double the GO:*methanogenesis* [GO_0015948] gene proportions than those of neritic samples, while neritic samples had much greater relative GO:*respiratory electron transport chain* [GO_0022904] proportions than deep samples.

Neritic samples had elevated proportions of photosynthetic related genes, 16% GO:*photosynthetic electron transport in photosystem II* [GO_0009772] genes and 1.4% GO:*photosynthetic electron transport chain* [GO_0009767] genes, contrasting with the 0.00% proportions of such genes in the deep benthic samples.  

Addressing CQ (2), I compared the relative proportions of GO:*vitamin biosynthetic process* [GO_0009110] genes in various types of ENVO:*marine benthic biomes* [ENVO_01000024], the results of which are summarized in **Table 2**.

\pagebreak

: **Table 2:** The relative proportions of GO:*vitamin biosynthetic process* [GO_0009110] genes in various types of ENVO:*marine benthic biomes* [ENVO_01000024].

| term                                                       | ENVO:*marine abyssal zone biome* [ENVO_01000027] | ENVO:*marine bathyal zone biome* [ENVO_01000026] | ENVO:*marine neritic benthic zone biome* [ENVO_01000025] |
|:-----------------------------------------------------------|:-------------------------------------------------|:-------------------------------------------------|:---------------------------------------------------------|
| GO:*riboflavin biosynthetic process* [GO_0009231]          | 0.25                                             | 0.25                                             | 0.07                                                     |
| GO:*cobalamin biosynthetic process* [GO_0009236]           | 0.19                                             | 0.19                                             | 0.03                                                     |
| GO:*pantothenate biosynthetic process* [GO_0015940]        | 0.13                                             | 0.12                                             | 0.04                                                     |
| GO:*thiamine biosynthetic process* [GO_0009228]            | 0.10                                             | 0.11                                             | 0.04                                                     |
| GO:*pyridoxine biosynthetic process* [GO_0008615]          | 0.10                                             | 0.09                                             | 0.02                                                     |
| GO:*vitamin B6 biosynthetic process* [GO_0042819]          | 0.05                                             | 0.05                                             | 0.02                                                     |
| GO:*pyridoxal phosphate biosynthetic process* [GO_0042823] | 0.05                                             | 0.05                                             | 0.02                                                     |

In these results there is a general trend in the deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples, toward higher relative proportions of GO:*vitamin biosynthetic process* [GO_0009110] genes are higher than ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples. For example the relative gene proportion of GO:*riboflavin biosynthetic process* [GO_0009231] genes was approximately 3.5 times greater in deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] sample genomes than ENVO:*marine neritic benthic zone biome* sample transcriptomes.

Addressing CQ (3), I investigated other genomic features which may help to explain the differences in riboflavin abundance, I investigated GO:*transition metal ion binding* [GO_0046914] and GO:*transition metal ion transport* [GO_0000041] subclasses. As flavins have been implicated as electron donors in the reduction of insoluble ferric to soluble ferrous iron as well as the transport of ferrous to the cytoplasm [@Crossley_2007][@Fuller_2013]. For full results of relative proportions of metal ion binding, and metal ion transport subclasses see **Tables A1** and **A2**. Querying for subclasses of GO:*transition metal ion binding* [GO_0046914] I found that GO:*ferrous iron binding* [GO_0008198] gene abundance is 0.02-0.03% in deep samples vs. 0.00% in neretic. Furthermore deep sample GO:*ferrous iron transport* [GO_0015684] gene abundance is double that of neritic sample, 0.04% vs. 0.02%.

To evaluate CQ (4) I investigated GO:*biological process* [GO_0008150] which differentiate ENVO:*marine benthic biome* [ENVO_01000024] samples in a sites by species PCoA analysis where all the subclasses of GO:*biological process* [GO_0008150] served as *species* (columns) and the various ENVO:*marine benthic biomes* [ENVO_01000024] served as *sites* (rows) of the analysis. The results of this PCoA analysis comparing the relative proportions genes and transcripts of datasets annotated as various types of ENVO:*marine benthic biomes* [ENVO_01000024] are shown in **Figure 6**. Together PCoA axes 1 and 2 explain 97.9% of the total variance, with axis 1 explaining 96.1% and axis 2 explaining 1.8%. In **Figure 6** there is a clear differentiation between ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples from those of ENVO:*marine neritic benthic zone biome*s [ENVO_01000025] along PCoA dimension 1.

![**Figure 6:** A principal coordinate analyses plot of the relative genomic proportions of genes which are subclasses of GO:*biological process* [GO_0008150] terms in various ENVO:*marine benthic biome*s [ENVO_01000024]. ](figures/all_biological_processes.png){ width=80% }

: **Table 3:** The top ten GO term *species* which were ordinated closest to the average of the ENVO:*marine neritic benthic zone biome* [ENVO_01000025] sites in the PCoA analysis conducted on the subclasses of GO:*biological process* [GO_0008150] from various ENVO:*marine benthic biomes* [ENVO_01000024].

+------------------------------------------------------------+-----------------------------+
| term                                                       | distance between GO *sites* |
|                                                            | and ENVO *species* average  |
+============================================================+=============================+
| GO:*respiratory electron transport chain* [GO_0022904]     | 0.0090311336                |
+------------------------------------------------------------+-----------------------------+
| GO:*intracellular protein transport* [GO_0006886]          | 0.0099281303                |
+------------------------------------------------------------+-----------------------------+
| GO:*response to arsenic-containing substance* [GO_0046685] | 0.0223422138                |
+------------------------------------------------------------+-----------------------------+
| GO:*regulation of cell division* [GO_0051302]              | 0.0241089607                |
+------------------------------------------------------------+-----------------------------+
| GO:*vesicle docking involved in exocytosis* [GO_0006904]   | 0.0246772626                |
+------------------------------------------------------------+-----------------------------+
| GO:*spermatogenesis* [GO_0007283]                          | 0.0269553554                |
+------------------------------------------------------------+-----------------------------+
| GO:*RNA metabolic process* [GO_0016070]                    | 0.027765135                 |
+------------------------------------------------------------+-----------------------------+
| GO:*tRNA wobble position uridine thiolation* [GO_0002143]  | 0.0278909429                |
+------------------------------------------------------------+-----------------------------+
| GO:*cellulose catabolic process* [GO_0030245]              | 0.0285254331                |
+------------------------------------------------------------+-----------------------------+
| GO:*inosine salvage* [GO_0006190]                          | 0.0304904183                |
+------------------------------------------------------------+-----------------------------+


: **Table 4:** Shows the top ten GO term species which were ordinated closest to the average of the deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] sample sites in the PCoA analysis conducted on the subclasses of GO:*biological process* [GO_0008150] from various ENVO:*marine benthic biomes* [ENVO_01000024].

| term                                                                | distance between GO *sites* and ENVO *species* average |
|:--------------------------------------------------------------------|:-------------------------------------------------------|
| GO:*tyrosine biosynthetic process* [GO_0006571]                     | 0.0021397886                                           |
| GO:*2'-deoxyribonucleotide metabolic process* [GO_0009394]          | 0.0026369643                                           |
| GO:*organic phosphonate metabolic process* [GO_0019634]             | 0.0033619593                                           |
| GO:*biotin transport* [GO_0015878]                                  | 0.0035475566                                           |
| GO:*cellular aromatic compound metabolic process* [GO_0006725]      | 0.0038546443                                           |
| GO:*tetrahydrobiopterin biosynthetic process* [GO_0006729]          | 0.0044421841                                           |
| GO:*riboflavin biosynthetic process* [GO_0009231]                   | 0.0045954664                                           |
| GO:*peptidyl-lysine modification to peptidyl-hypusine* [GO_0008612] | 0.0050485454                                           |
| GO:*tetrapyrrole biosynthetic process* [GO_0033014]                 | 0.005543313                                            |
| GO:*glycine biosynthetic process* [GO_0006545]                      | 0.005644747                                            |



Addressing CQ (5), I used the GO biological processes hierarchy, shown in **Figure A2**, to drill down to a more specific term by which to investigate the differentiation of these environmental omic data. I performed another sites by species PCoA analysis on the subclasses of GO:*cellular amino acid biosynthetic process* [GO_0008652]. The results of which are shown in **Figure 7**. Together the first two PCoA axes explain 94.2% or total variance, with axis 1 explaining 81.7 and axis 2 12.5%. The GO terms which ordinated in closest proximity to the average of the ENVO:*marine neritic benthic zone biome* [ENVO_01000025] sites are shown in **Table 5**. The top ten GO terms which ordinated in closest proximity to the average of the ENVO:*marine benthic biomes* [ENVO_01000024] sites are shown in **Table 6**.

![**Figure 7:** Principal coordinate analyses plot of relative genomic proportions of subclasses of GO:*cellular amino acid biosynthetic process*es [GO_0008652] in various ENVO:*marine benthic biomes* [ENVO_01000024]. ](figures/cellular_amino_acid_biosynthetic_process.png){ width=80% }

: **Table 5:** The four GO term *species* which were ordinated closest to the average of the ENVO:*marine neritic benthic zone biome* [ENVO_01000025] *sites* in the PCoA analysis conducted on the subclasses of GO:*cellular amino acid biosynthetic process* [GO_0008652] from various ENVO:*marine benthic biomes* [ENVO_01000024].

| term                                                             | distance between *sites* and *species* average |
|:-----------------------------------------------------------------|:-----------------------------------------------|
| GO:*cysteine biosynthetic process from serine* [GO_0006535]      | 0.0109862681                                   |
| GO:*branched-chain amino acid biosynthetic process* [GO_0009082] | 0.0287599861                                   |
| GO:*leucine biosynthetic process* [GO_0009098]                   | 0.0508556504                                   |
| GO:*glutamine biosynthetic process* [GO_0006542]                 | 0.0525977927                                   |

\pagebreak


: **Table 6:** The top ten GO term *species* which were ordinated closest to the average of the ENVO:*marine benthic biomes* [ENVO_01000024] *sites* in the PCoA analysis conducted on the subclasses of GO:*cellular amino acid biosynthetic process* [GO_0008652] from various ENVO:*marine benthic biomes* [ENVO_01000024].

| term                                                                                                              | distance between *sites* and *species* average |
|:------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------|
| GO:*lysine biosynthetic process via diaminopimelate* [GO_0009089]                                                 | 0.005673472                                    |
| GO:*glutamate biosynthetic process* [GO_0006537]                                                                  | 0.0066474342                                   |
| GO:*glycine biosynthetic process* [GO_0006545]                                                                    | 0.0074418762                                   |
| GO:*tyrosine biosynthetic process* [GO_0006571]                                                                   | 0.0088699732                                   |
| GO:*histidine biosynthetic process* [GO_0000105]                                                                  | 0.0098166072                                   |
| GO*:L-methionine biosynthetic process from homoserine via O-succinyl-L-homoserine and cystathionine* [GO_0019281] | 0.0098643686                                   |
| GO:*aromatic amino acid family biosynthetic process* [GO_0009073]                                                 | 0.0114389565                                   |
| GO:*L-phenylalanine biosynthetic process* [GO_0009094]                                                            | 0.0160432659                                   |
| GO:*arginine biosynthetic process* [GO_0006526]                                                                   | 0.0162479534                                   |
| GO:*methionine biosynthetic process* [GO_0009086]                                                                 | 0.0191591849                                   |

\pagebreak

Addressing CQ (6), I examined the GO hierarchy for subclasses of GO:*cellular amino acid biosynthetic process* [GO_0008652], shown in **Figure A2**, and drilled down into even more specific terms to further differentiate the ENVO:*marine benthic biomes* [ENVO_01000024] samples. The results of investigating the differences between subclasses of GO:*serine family amino acid biosynthetic processes* [GO_0009070] are shown in **Figure 8**. In this *sites* by *species* PCoA analysis, PCoA axis 1 explains 100% of the variance. In this analysis there is a clear differentiation of ENVO:*marine neritic benthic zone biome* [ENVO_01000025] and deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples. The GO:*glycine biosynthetic process*es [GO_0006545] ordinate in close proximity to the deep samples, while the GO:*cysteine biosynthetic process from serine* [GO_0006535] samples ordinate with the ENVO:*marine abyssal zone biome* [ENVO_01000027] samples.

![**Figure 8:** Principal coordinate analyses of relative genomic proportions of subclasses of GO:*serine family amino acid biosynthetic processes* [GO_0009070] in various ENVO:*marine benthic biomes* [ENVO_01000024]. ](figures/serine_family_amino_acid_biosynthetic_process.png){ width=80% }


\lstset{language=}


\pagebreak

## 3.2 Data pertinent to an environment determined by a phytoplankton community associated with sea-ice

To test the fitness for purpose of using ontologies to collect interdisciplinary data relevant to an ecological question as in CQ (7), I made use of a hypothetical ontology term ENVO:*environment determined by a phytoplankton community associated with sea-ice* [URI pending]. This is a hypothetical term because it does not currently exist as an ENVO term, but is composed with a definition and subclass axioms as an actual ENVO term would be. I defined this term as:

> An environmental system which has its properties and dynamics determined by a phytoplankton community which is associated with sea-ice.

This hypothetical term would include the following subclass axioms: ENVO:*environmental system determined by a community* [URI pending], ENVO:*determined by* [ENVO_2100001] some PCO:*phytoplankton community* [URI pending], RO:*located in* [RO_0001025] some (ENVO:*seawater* [ENVO_00002149] and (RO:*part of* [BFO_0000050] some ENVO:*marine water body* [ENVO_00001999])), and finally RO:*adjacent to* [RO_0002220] some ENVO:*sea ice* [ENVO_00002200].

Addressing CQ (7) I was able to search the datastore for data annotated with terms which are present in the axioms of the hypothetical ENVO:*environmental system determined by a community* [URI pending] term, or their subclasses, and collect the following data columns shown in **Table 7**.

\pagebreak
: **Table 7:** Data columns collected with the assistance of the hypothetical ontology term ENVO:*environment determined by a phytoplankton community associated with sea-ice* [URI pending], which may be of relevance to an environment determined by a phytoplankton community associated with sea-ice. The data column label is shown in the first column. The ontology-annotation term which allowed for the retrieval of the collected data column is shown in the second column. Finally the dataset from which the retrieved column originated is shown in the third column.

| data column label       | annotation term                      | dataset of origin                                                                                                  |
|:------------------------|:-------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| phosphate               | ENVO:*sea water* [ENVO_00002149]     | Inorganic nutrients measured on water bottle samples at AWI HAUSGARTEN during POLARSTERN cruise MSM29.             |
| nitrate                 | ENVO:*sea water* [ENVO_00002149]     | Inorganic nutrients measured on water bottle samples at AWI HAUSGARTEN during POLARSTERN cruise MSM29.             |
| ice or snow temperature | ENVO:*multiyear ice* [ENVO_03000073] | Ice-algal chlorophyll a and physical properties of multi-year and first-year sea ice of core CASIMBO-CORE-2_11.    |
| sea ice thickness       | ENVO:*sea ice* [ENVO_00002200]       | Influence of snow depth and surface flooding on light transmission through Antarctic pack ice, supplementary data. |
| signal strength         | ENVO:*sea ice* [ENVO_00002200]       | Influence of snow depth and surface flooding on light transmission through Antarctic pack ice, supplementary data. |
| oxygen                  | ENVO:*sea water* [ENVO_00002149]     | Physical oceanography and current meter data from mooring TD-2014-LT.                                              |
| salinity                | ENVO:*sea water* [ENVO_00002149]     | Physical oceanography and current meter data from mooring TD-2014-LT.                                              |


A demonstration of using such data to perform a mock ecological analysis is included in appendix **A.4**. For the references of the original datasets see appendix **A.2**.



\pagebreak
## 3.3 Provenance of ontology term authors

To evaluate CQ (10), I performed queries to calculate the proportions of ENVO and envoPolar terms which are annotated with an IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation which reference an ORCID. ORCID is a unique identifier for scientific and other academic authors and contributors [@ORCID_2009]. The results of this analysis are summarized in the **Table 8**.

: **Table 8:** Percentages of ENVO and envoPolar terms which are annotated with an IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation.

| ontology  | % terms with oboInOwl:*created_by* [created_by] | % terms with IAO:*term editor* [IAO_0000117] |
|:----------|:------------------------------------------------|:---------------------------------------------|
| ENVO      | 14.5                                            | 4.2                                          |
| envoPolar | 17.2                                            | 31.4                                         |

Examining these results I found that 4.2% of ENVO terms have an IAO:*term editor* [IAO_0000117] annotation, whereas 31.4% of envoPolar terms are annotated with an IAO:*term editor* [IAO_0000117]. Terms related by an oboInOwl:*created_by* [created_by] relation account for 14.5% of ENVO terms, wheres they are found in 17.2% of terms from the envoPolar subset. Altogether approximately 20% of ENVO and nearly 50% of envoPolar terms are annotated with a IAO:*term editor* [IAO_0000117] or oboInOwl:*created_by* [created_by] relation.

To further investigate CQ (10), examined how the ORCID application programming interface can be used to retrieve the current contact information from an input ORCID client identifier. Using the publicly available demonstration ORCID client identifier ``APP-NPXKK6HFN6TJ4YYI``, I was able to retrieve the associated contact information and obtain the email address ``s.garcia@orcid.org``.


\pagebreak

## 3.4 Provenance of dataset-associated primary literature


The results of the evaluation of CQ (9) are as follows, in the datastore there are two datasets which are annotated with a terms which satisfy the condition of being part of an ENVO:*marine biome* [ENVO_00000447]: *Global chlorophyll "a" concentrations for diatoms, haptophytes and prokaryotes obtained with the Diagnostic Pigment Analysis of HPLC data compiled from several databases and individual cruises.* [@soppa2017gcac][@Losa_2017], and *Influence of snow depth and surface flooding on light transmission through Antarctic pack ice, supplementary data.* [@arndt2017iosd][@Arndt_2017]. Both of which are about an ENVO:*marine water body* [ENVO_00001999]. Returned are the DOI persistent uniform resource locators for the 14 publications which make use of these two example AWI datasets. For a full list see **Table A3**. Selected example results of publications, their digital object identifiers as well as the dataset from which the publications were retrieved are shown in **Table 9**. Retrieved publications about variety of ENVO:*marine water body* [ENVO_00001999] related topics, including using chlorophyll pigments to determine phytoplankton taxonomy, plankton ecology, vertical distributions of phytoplankton communities and light transmission through pack-ice.

: **Table 9:** Selected examples of digital object identifiers of publications obtained querying for references of datasets which are about BFO:*part of* [BFO_0000050] a ENVO:*marine biome* [ENVO_00000447].  

+---------------+----------------------------+------------------------+
|data set       |reference DOI               | reference title        |
+===============+============================+========================+
|global        \|10.1016/j.dsr.2011.01.008   |An evaluation of the application\|
|chlorophyll a \|                            |of CHEMTAX to Antarctic coastal\|
|              \|                            |pigment data [@Kozlowski_2011]\|
+---------------+----------------------------+------------------------+
|               |10.3402/polar.v34.23349     |Summertime plankton ecology\|
|               |                            |in Fram Strait a compilation\|
|               |                            |of long and short-term \|
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

## 3.5 Proposed ablation semantics

The Feb 2, 2018 VoCamp Glacier Ontology Hackathon [@vocamp_2018], was a community consultation session in which polar-related domain experts and ontology developers met to work toward the alignment of base semantics around a set of glacier-related terms. A list of participants is included in appendix **Table A5**. During the community consultation session, the semantic representation of a variety of glacier-related topics was discussed. I chose to follow up on one of the more defined outputs of the Hackathon session in which there was discussion about how best to capture the semantics of an ablation process, given that different sources of expert knowledge gave partially different definitions of the process. The NOAA National Weather Service (2009) glossary [@nws_internet_services_team_glossary_2009] defined ablation as only including melting and evaporation processes, whereas the Cogley et al. (2011) IACS-UNESCO Glacier Mass Balance glossary [@cogley_glossary_2011] definition referred to all processes which reduce the mass of a glacier, including calving processes. Addressing CQ (11), with these definitions of ablation serving as a case study, I proposed for the following classes to be added to ENVO.

In order to handle cases in which an ablation processes results only from melting and evaporation, I proposed the creation of the term ENVO:*icemelt-derived ice ablation process* [URI pending] which I define as:

> An ice ablation process during which ice is lost due to an icemelt process.

This term would include the subclasses axioms: ENVO:*ice ablation process* [ENVO_01000919], BFO:*has part* [BFO_0000051] some ENVO:*icemelt* [ENVO_01000721], and oboInOwl:*database_cross_reference* [hasDbXref] http://w1.weather.gov/glossary/.

In order to handle cases in which an ablation processes results from both melting and calving processes, I proposed the creation of the term ENVO:*icemelt or calving-derived ice ablation process* [URI pending] which I define as:

> An ice ablation process during which ice is lost due to an icemelt process or ice calving process.

The subclass axioms included in this term would be: ENVO:*ice ablation process* [ENVO_01000919], BFO:*has part* [BFO_0000051] some (ENVO:*icemelt* [ENVO_01000721] or ENVO:*ice calving process* [ENVO_01000917]), and finally the oboInOwl:*database_cross_reference* [hasDbXref] http://unesdoc.unesco.org/images/0019/001925/192525e.pdf.

## 3.6 Resilience of ontology-enabled data-mobilization workflows to changes in underlying semantic models  

As illustrated in **Figure 3** I developed a workflow which makes use of knowledge contained within the OBO ontologies, to discover new knowledge based on connections to stated input knowledge, and retrieve data about these discovered classes. Using this workflow I was able to find classes which are involved in any type of RO:*has participant* [RO_0000057] relation with any type of ENVO:*sea ice formation process* [ENVO_03000044]. Additionally I was able to retrieve data about the discovered classes. The results of this workflow are shown in **Table 10**.

: **Table 10:** Results of querying for classes involved in any RO:*has participant* [RO_0000057] relation with subclasses of ENVO:*sea ice formation process* [ENVO_03000044], as well as the number of data items about the discovered classes retrieved from the datastore. The first column shows the ENVO:*sea ice formation process* [ENVO_03000044] subclasses which are the subjects in a RO:*has participant* [RO_0000057] relation with another class. The second column shows the subproperties of the RO:*has participant* [RO_0000057] relation, which related an ENVO:*sea ice formation process* [ENVO_03000044] subclass to another class. The third column shows classes discovered to be related to a subclass of an ENVO:*sea ice formation process* [ENVO_03000044] by a subproperty of RO:*has participant* [RO_0000057]. The fourth column shows the number of data items about the discovered class which were retrieved from the datastore.

| subject class                                           | property                       | discovered class                       | number of data items |
|:--------------------------------------------------------|:-------------------------------|:---------------------------------------|:---------------------|
| ENVO:*sea ice formation process* [ENVO_03000044]        | ENVO:*has input* [RO_0002233]  | ENVO:*sea water* [ENVO_01000321]       | 13                   |
| ENVO:*sea ice formation process* [ENVO_03000044]        | ENVO:*has output* [RO_0002234] | ENVO:*sea ice* [ENVO_03000066]         | 6                    |
| ENVO:*nilas formation process* [ENVO_03000058]          | ENVO:*has input* [RO_0002233]  | ENVO:*new ice* [ENVO_03000063]         | 0                    |
| ENVO:*nilas formation process* [ENVO_03000058]          | ENVO:*has output* [RO_0002234] | ENVO:*nilas* [ENVO_03000068]           | 0                    |
| ENVO:*young ice formation process* [ENVO_03000059]      | ENVO:*has output* [RO_0002234] | ENVO:*young ice* [ENVO_03000069]       | 0                    |
| ENVO:*first year ice formation process* [ENVO_03000060] | ENVO:*has output* [RO_0002234] | ENVO:*first year ice* [ENVO_03000071]  | 8                    |
| ENVO:*second year ice formation* [ENVO_03000061]        | ENVO:*has output* [RO_0002234] | ENVO:*second year ice* [ENVO_03000072] | 0                    |
| ENVO:*multiyear ice formation process* [ENVO_03000062]  | ENVO:*has output* [RO_0002234] | ENVO:*multiyear ice* [ENVO_03000073]   | 8                    |

This workflow makes use of knowledge contained within the OBO ontologies to search for subclasses of an input class e.g. ENVO:*sea ice formation process* [ENVO_03000044] and subproperties of an input property e.g. RO:*has participant* [RO_0000057]. Referring to CQ (12), I evaluated how much of this data would be retrievable if changes were made to the semantic models which the ontologies used this workflow themselves use. I tested the susceptibility of this workflow for retrieving data, to changes in the Relations Ontology. I did so by simulating what would happen if substantial changes were to be made to the Relations Ontology without such changes being applied to my example data. I also tested how well this workflow would perform if ontology knowledge graphs didn't employ hierarchically structured subclass relations to represent knowledge about classes and their subclasses. The results of these susceptibility simulations are as follows. If ontologies were to not make use of hierarchically structured subclass relations, only 54.3% of the data items would be retrievable. Faced with major changes to the Relations Ontology 0% of the relevant data would be retrievable.

## 3.7 Polar knowledge graph network parameters

Addressing CQ (8), I treated connectivity within a network created from an ontology knowledge graph as a proxy for the extent to which ontologies can help to connect researchers to new unspecified knowledge from stated input knowledge. I analyzed the envoPolar subset as a network. The resulting network property statistics are summarized as follows. The average degree, the number of edges corresponding to each node, is 1.517. The distributions of in-degree values, edges pointing into a node, and out-degree, edges leading away from a node are shown in **Figures A4**, and **A5**. The average in-degree distribution shows a positive skew with a median of 0 relative to the mean degree of 1.517, with a very wide range of in-degree values from 0 to 44. The average out-degree distribution also shows a positive skew with a median of 1 relative to the mean degree of 1.517, and the out-degree values range from 0 to 5. Additional network parameters are summarized in **Table 11**.

: **Table 11:** Network parameters calculated from the graph of the envoPolar subset of ENVO.

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

Analysis of the distribution of shortest path lengths, the expected distance between two connected nodes is as follows. The mean shortest path length is 2.246, and the distribution of shortest path lengths, **Figure 9**, shows a positive skew with the median shortest path length being 2.0, a value less than that of the mean.  

![**Figure 9:** Distribution of shortest path lengths of the envoPolar subset analyzed as a network.](figures/shortest_path_length_distribution.jpeg){ width=80% }

The average connectivity or average number of neighbors, indicating the expected number of vertices that would need to be removed to separate any randomly chosen pair of vertices is 2.875. The clustering coefficient, a measure of the extent to which nodes in a graph tend to cluster together bounded on a scale from 0 to 1, zero being unconnected and 1 being completely connected is 0.047. Plotting the average cluster coefficients as a function of number of neighbors, see **Figure 10**, I observe two distinct clusters of nodes. Nodes either have a high average clustering coefficient and a small number of neighbors, or they have a low clustering coefficient and a large number of neighbors.

![**Figure 10:** Average clustering coefficient as a function of number of neighboring nodes in the envoPolar subset analyzed as a network.](figures/average_clustering_coefficient.jpeg){ width=70% }

Finally I analyzed the betweenness centrality of nodes in the envoPolar network, see **Figure A6**. Betweenness centrality of a node is a value ranging between 0 and 1, which reflects the amount of control this node exerts over the interactions of other nodes. Plotting betweenness centrality as a function of number of neighboring nodes I find only 3 nodes with non-zero betweenness centrality values, all of which have only 2 neighboring nodes. The rest of the nodes have a betweenness centrality of near zero, regardless of the number of neighbors.

\pagebreak

: **Table 12:** Top ten largest in-degree value polar-related classes from the envoPolar subset.

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

From the results presented in **Table 12** and **13** showing the nodes with the highest and lowest in-degree values, I observed that there are very few nodes of substantial in-degree values. The distribution of in-degree drops off very rapidly with only a few nodes such as ENVO:*water ice* [ENVO_01000277], ENVO:*glacier* [ENVO_00000133], and ENVO:*snow* [ENVO_01000406] having high in-connectivity values. Even within the top ten in-degree nodes the value decrease substantially from ENVO:*water ice* with 24 in connections, to ENVO:*permafrost thawing process* [ENVO_03000086] with only 3 interconnections. From **Table 13** we see that many of the nodes have in-degrees of 0.


\pagebreak
: **Table 13:** The ten smallest in-degree value polar-related classes from the envoPolar subset.

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
## 3.8 Predicted-user mobilized data

Assessing CQ (13), I evaluated the relative amount of data which would be retrieved by estimated user stories programmed to estimate users of various levels of querying expertise, estimating the retrieval rates of data for users of the system with basic, intermediate and advanced querying expertise.

Two estimated user story querying proficiency experiments were conducted, the first queried for data which was about the exclusive *and* intersection of two annotation terms, for example data about *snow and thickness*. The second experiment queried for data which is about a part of an input term, for example, *part of a glacier*. The results of the first experiment, displaying the percentages of annotation terms and data matrix columns retrieved about the intersection of two terms, are presented in **Figure 11**.

![**Figure 11:** Analysis of querying expertise required to obtain data matrix columns and annotations when querying for data about subclasses of a term AND another term. The first panel shows the percentages of annotation terms retrieved by each querying expertise level user story for each of the querying scenarios. The second panel shows the percentages of data columns retrieved by each querying expertise level user story for each of the querying scenarios. ](figures/query_and_annotation_columns_number.jpeg){ width=80% }

User stories estimating basic querying expertise were only able to retrieve data and annotations from the *Bacteria and Archaea* case. User stories estimating intermediate querying expertise were only able to retrieve data from 4 out of the 8 cases tested. Excluding the *Bacteria and Archaea* cases which were covered with 100% success by all three expertise classes, the percentage of annotations retrieved by intermediate user stories ranged from 40-66.7%, whereas the percentage of data columns retrieved ranged from 50-80%. Advanced user stories were able to retrieve data columns and annotations from all 8 of the tested querying cases, with successes ranging from 57.1% to 100% of annotations and 66.7% to 100% of data matrix columns.

The results of the second experiment, displaying the percentages of data matrices and data points retrieved from BFO:*part of* [BFO_0000050] input terms are presented in **Figure 12**. Basic user stories were only able to retrieve data matrices from the  *parts of a marine biome* case, as well as data points from the *part of a centrally registered identifier symbol* case. In terms of the success rates of retrieving data matrices about *parts of a marine biome*, the basic user story expertise case retrieved 25%, the intermediate case retrieved 75% and advanced case retrieved 100%. Intermediate expertise user stories were only able to retrieve data points from 4 out of the 8 *parts of cases*. Although advanced user stories were able to retrieve data points from the majority of *parts of* query cases, they were unable to retrieve any from the *parts of a carbon atom* cases, and they were only able to retrieve 82.3% of data which is *part of a glacier*, and 94.9% of data annotated with an ontology term which is *part of an ocean*.

![**Figure 12:** Analysis of querying expertise required to obtain data matrices and data points when querying for data about parts associated with  an ontology term. The first panel shows the percentages of data matrices retrieved by each querying expertise level user story for each of the querying scenarios. The second panel shows the percentages of data points retrieved by each querying expertise level user story for each of the querying scenarios.](figures/query_parts_of_stats.jpeg){ width=80% }

\newpage

## 3.9 Proposed plankton-ecology semantics

Attempting to build upon the semantic framework proposed as necessary by Stec et al. (2017), for future modeling of plankton ecosystems [@Stec_2017], I addressed CQ (14). To answer this question I proposed the following plankton ecology related ontology term to the ENVO [@Buttigieg_2013][@Buttigieg_2016] PATO [@PATO_BioPortal] ECOCORE [@ecocore_2018] and PCO [@PCO__BioPortal] ontologies. A complete description of these potential ontology terms, are provided in D.S.4.

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
ENVO:*marine water body stratification* [URI pending], finally with oboInOwl:*database_cross_reference*s [hasDbXref] https://doi.org/10.1016/j.jmarsys.2013.11.008 [@Cherkasheva_2014], https://en.wikipedia.org/wiki/Attenuation

I bring these terms together in the following **Figure 13** as to visualize the interconnecting relationships between them.

![**Figure 13:** Diagram indicating relationships interconnecting the example ontology term contributions made during the course of this work to encode expert knowledge about plankton ecology. The nodes in the graph are the example proposed ontology classes for the ENVO, PCO and PATO ontologies. The edges in the graph are the proposed RO relationships between classes.](figures/plankton_ecology.pdf){ width=70% }

I assessed if ontologies can help us to contextualize the interconnections between encoded phenomena about which we have expert knowledge. **Figure 13** illustrating the relationships interconnecting the various phenomena which effect phytoplankton blooms shows how ontologies help us to understand the interconnections between pieces of expert knowledge. Starting by examining physical processes which have effects on phytoplankton blooms, I assembled and encoded the following expert knowledge. As the onset of phytoplankton blooms have been shown to be dependent on the timing of the retreat of melting sea ice [@Janout_2016], I encoded the knowledge of such a relationship into the potential term sea ice melting, by specifying that it is RO:*causally upstream of* [RO_0002411] some ENVO:*marine water body stratification* [URI pending].

I encoded the concept of the ENVO:*marginal ice zone*, which is described as the transition zone between the open ocean and sea ice [78]. In the ENVO:*marginal ice zone*, melting sea-ice has been shown to promote phytoplankton growth by stratifying the water column [@Cherkasheva_2014]. To encode the knowledge of the process of stratification I created the potential class ENVO:*marine water body stratification*, which RO:*results in formation of* [RO_0002297] at least two ENVO:*marine layer*s [ENVO_01000295]. In the ENVO:*marginal ice zone*, stratification of the water body resulting from melting sea ice has been shown to be the location of maximum chlorophyll [@Cherkasheva_2014], controlling the onset of the seasonal phytoplankton blooms [@Janout_2016]. To encode knowledge about phytoplankton blooms, I created a variety of terms related to population and community blooms. An example of which is the potential term phytoplankton bloom process. To represent the knowledge that phytoplankton blooms tend to occur as a result of sea ice retreat in the marginal ice zone. I have encoded into the ENVO:*marginal ice zone* term an axiom stating that marginal ice zones are RO:*causally upstream of, positive effect* [RO_0002304] some PCO:*phytoplankton bloom process* [URI pending]. As phytoplankton bloom processes have a profound impact on their surrounding environment, I have also created the term ENVO:*marine environment determined by a phytoplankton community bloom*, which I have specified to be related to PCO:*phytoplankton bloom processes* with the axiom ENVO:*determined by* [ENVO_2100001] some PCO: *phytoplankton bloom process* [URI pending]. I have also encoded the connection between an ENVO:*marine environment determined by a phytoplankton community bloom* and ENVO:*marine water body stratification* with the RO:*causally downstream of, negative effect* [RO_0002305] relationship.



\newpage

# 4. Discussion

## 4.1 The value of semantically enhance comparative environmental genomics


Addressing CQ (1), I was able to make use of interoperable GO and ENVO ontology terms, to mobilize environmentally-annotated omics data. I examined the results of **Table 1**, showing the relative genomic and transcriptomic proportions of GO:*oxidation-reduction process* [GO_0055114] genes, in various ENVO:*marine biome*s [ENVO_00000447], to address the question of whether ontologies are fit for purpose to facilitate the comparison of omics datasets sourced from various environments. It should be noted that these comparisons are more intended to demonstrate proof of concept that ontology-mobilized genomic comparison are possible, not to conduct a thorough comparison of genomic differences between deep and shallow marine sediments.

My results indicate as would be biologically expected that ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples are relatively enriched in GO:*photosynthetic electron transport in photosystem II* [GO_0009772], GO:*aerobic respiration* [GO_0009060] and GO:*respiratory electron transport chain* [GO_0022904] related genes, relative to the ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples where were enriched in undifferentiated GO:*oxidation-reduction process*es [GO_0055114] and GO:*methanogenesis* [GO_0015948] related genes. This preliminary comparison indicates the feasibility of using ontology term annotations to interlink and compare genomic data differentiated by source environment.

Addressing CQ (2), I further explored the use of interoperable GO and ENVO semantics to compare environmentally annotated omics samples. From **Table 2**, showing the relative abundance of GO:*vitamin biosynthetic process* [GO_0009110] genes in various types of ENVO:*marine benthic biomes* [ENVO_01000024], I noted that in the deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples, there is a general trend that the relative gene proportions of GO:*vitamin biosynthetic process* [GO_0009110] genes are higher than the relative transcriptomic proportions of ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples.

Following up on the result of potentially finding elevated GO:*vitamin biosynthetic process* [GO_0009110] genomic capacity in deep samples relative to the lower transcriptomic capacity in ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples, I addressed CQ (3). I did so by making use of the GO knowledge graph to search for the relative proportions of other GO:*biological process* [GO_0008150] and GO:*molecular function* [GO_0003674] terms which may help to explain the differences in GO:*vitamin biosynthetic process*es [GO_0009110]. As flavin compounds have been implicated as electron donors in the reduction of insoluble ferric to soluble ferrous iron, as well as the transport of ferrous iron to the cytoplasm [@Crossley_2007][@Fuller_2013], I further investigated GO:*transition metal ion binding* [GO_0046914] and GO:*transition metal ion transport* [GO_0000041] subclasses.

The results I obtained showing potentially elevated GO:*ferrous iron binding* [GO_0008198] and GO:*ferrous iron transport* [GO_0015684] gene abundance in ENVO:*marine abyssal zone biome*s [ENVO_01000027] and ENVO:*marine bathyal zone biome*s [ENVO_01000026] relative to ENVO:*marine neritic benthic zone biome*s [ENVO_01000025] samples, combined with the elevated GO:*riboflavin biosynthetic process* [GO_0009231] may hint at a possible ecophysiological connection. Given access to more omics data sourced from similar environments which were made interoperable and machine-accessible, I would be able to propose novel bioinformatic hypotheses. From the currently data-limited example, I might suggest a hypothesis such as the genomic capacity for riboflavin mediated iron reduction differentiates ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] sediments from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] sediments. This example illustrates how using the interoperable semantics from ENVO and GO can be used to facilitate genomic comparisons, enabling specifically direct ecological questions to be asked of omic data.

As OBO ontologies adopt a realist philosophy, representing what exists in reality as opposed to conceptualizations of reality which are shared by knowledgeable agents [@Arp_2015]. Multiple competing hypotheses can be encoded into the ontology knowledge graph without the presumption of any being the absolute truth. A hypothesis such as the interconnection between riboflavin production, iron binding and transport genes in deep marine sediments, could be semantically expressed and added to the ontology knowledge graph. This along with other hypotheses about covariation of gene proportions could subsequently be tested over larger collections of genomic data sets. Leveraging the ontology semantics to retrieve data to analyze gene covariation to support or reject batches of genomic hypotheses. The continued development of cyberinfrastructure by which to conduct these types of comparative genomic analysis could be scaled up to a large machine-actionable system for the analysis of microbial genomics. Thematically this could build upon previous efforts such as the Community cyberinfrastructure for Advanced Microbial Ecology Research and Analysis (CAMERA), a semantically-annotated environmental genomic data base supporting semantic queries [@Sun_2010], or current efforts such as the Ocean Cloud Commons project which allows users to query the Tara Oceans Expedition Data [@ocean_cloud].

Addressing CQ (4), I further investigated potential knowledge which can be derived from the interconnection of data annotated with GO and ENVO terms. Addressing CQ (5), by drilling down into finer levels of granularity within the GO:*biological process* [GO_0008150] hierarchy, see **Figure 6** and **A2**, I was able to pinpoint processes differentiating deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples, specifically GO:*cellular amino acid biosynthetic processes* [GO_0008652]. The results of which are shown in **Figure 7** in which we can see that analyzing the subclasses of GO:*cellular amino acid biosynthetic processes* [GO_0008652], makes for more easily interpretable results than does the examination of the higher level GO:*biological process* [GO_0008150] class with more subclasses shown in **Figure 6**. From these results, I noted that the term GO:*cysteine biosynthetic process from serine* [GO_0006535], is ordinated in close proximity with the ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples. Thus to further investigate this potential difference, again making use of the GO:*biological process* [GO_0008150] hierarchy, see **Figure A2**, I asked and evaluated CQ (6). The results of which are shown in **Figures 8** where I examined GO:*serine family amino acid biosynthetic processes* [GO_0009070] differentiating deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] samples from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples. The analysis in **Figure 8** illustrates a very clear and potentially biologically interesting difference. GO:*glycine biosynthetic process* [GO_0006545], which has as subclass GO:*glycine biosynthetic process from serine* [GO_0019264], is more abundant in the deep ENVO:*marine benthic biomes* [ENVO_01000024] samples, whereas GO:*cysteine biosynthetic process from serine* [GO_0006535] is more abundant in the ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples.

The amino acid serine is a precursor in the production of both glycine and cysteine. Therefore, from these finding we can hypothesize that organisms from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] may tend to produce cysteine from serine, whereas organisms from deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] biomes may tend to produce glycine from serine. A possible explanation is that glycine is an important component in glycine betaine used by microbes as an osmoprotectant, helping to withstand osmotic stress [@Meury1988], which may help microorganisms to cope with high pressure deep environments.

These examples show how ontologies are fit for purpose to interconnect disparate omic datasets and generate working hypotheses therefrom. What is most notable from these finding is that I was able to uncover potential differences based solely on information contained within the GO and ENVO ontologies. Having no preliminary ideas about what GO:*cellular amino acid biosynthetic processes* [GO_0008652] which could differentiate deep ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] samples, nor knowledge of what amino acids serine is a precursor to. Additionally, I didn't need to know what the subclasses of ENVO:*marine benthic biomes* [ENVO_01000024] were in order to perform these analyses. I simply asked for any ENVO:*marine benthic biomes* [ENVO_01000024] subclasses and I was able to draw upon the expert knowledge contained within the ENVO knowledge graph to guide my analysis. It should be remarked that these ontologies are living knowledge graphs continually being updated with expert knowledge, this is especially true of the GO, to which hundreds of domain experts have contribute knowledge.

## 4.2 Ontology-guided data and knowledge discovery: are ontologies fit for purpose?

Being able to navigate machine-accessible information to discover data and knowledge are key competencies for ontologies to be able to perform CQ (7,8). To explore the question of ontological fitness for purpose for the discovery of knowledge and data, I have analyzed how ontology annotation terms can be used to facilitate the retrieval of relevant knowledge and data about a phenomenon of interest. I also evaluated  the network parameters of an example ontology knowledge graph to assess if it is suitable to connecting knowledge explicitly stated by a researcher to new, unstated but related knowledge.

Evaluating CQ (7), I analyzed how ontology terms can be used to facilitate the collection of relevant knowledge and data about a phenomenon of interest from a machine-accessible datastore, for example environmental factors which may influence a sea-ice associated phytoplankton community. Using semantics sourced from ontologies I was able to mobilize machine-accessible data from my datastore, which was of relevance to my phenomena of interest. Doing so, I encountered both expected and unexpected data which may potentially be of use to perform an ecological analysis on the data. For example when I retrieved data about environmental factors which may influence sea-ice associated phytoplankton communities, I retrieved some variables I expected to find such as sea ice thickness, multi-year sea ice temperature, degree of illumination of sea ice. Additionally, I also retrieved some unexpected but potentially relevant data such as sea water salinity, oxygen, phosphate and nitrate concentrations. In an ideal case the ontology annotations would help us to assemble data which researchers would not have thought to include in the analysis. Sea water salinity data for example, may give an indication of the existence of meltwater released from sea ice melting. Such data coinciding with available nutrient concentrations could indicate the beginning of a phytoplankton bloom.

Despite being able to harness the rich wealth of knowledge encoded within ontologies, a lack of machine-accessible data hinders our ability to perform ecological analysis on ontology-discovered data. Hence I would describe the current situation as rich in knowledge but poor in data. In order for future machine-guided routines to make use of ontologies to discover data relevant to a phenomenon of interest and perform ecological analysis thereon, more machine-accessible data is required. This is not necessarily an infeasible goal for the scientific community to strive toward. Simple efforts to toward standardizing data outputs generated by projects such as environmental observatories could go a long way toward providing machine-accessible data to analyze. Striving toward the long term goal of improved data standardization, could help us to enable data to be used to its full potential. This would allow for future machine-guided meta-analyses to be conducted on large machine-accessible data sets. Using ontologies and machine-accessible data as the source material for future artificial intelligence knowledge representation endeavors may allow us to break through traditional analysis barriers. Enabling deeper, expert-knowledge and large-data-informed machine-guided ecological meta-analyses to be performed.

In addition to the discovery of data, I assessed if ontological knowledge graphs are fit for the purpose of discovering new knowledge from ontology knowledge graphs which is related to the stated input knowledge. For this I made use of the envoPolar ENVO subset as an example ontology knowledge graph. Answering CQ (8), I assessed the network parameters of the envoPolar graph, assuming that connectivity within the graph is analogous to the facility of researchers searching the network to discover knowledge associated with their stated input knowledge.

My analysis of the properties of the network envoPolar created from the envoPolar subset is as follows. The network has a low number of components, with the vast majority of nodes and edges belonging to the largest components. Therefore the network should be analyzed as a relational based regime as opposed to a competent based regime. This is logical as the network makes use of structured upper level semantic models of the Basic Formal Ontology. I additionally examined the diameter of the network, the longest possible path between connected nodes in a network to gain insight into how well integrated the network is. Longer maximum path lengths equate to less well integrated networks [@labs_network_2016]. In the envoPolar network, the maximum path length is only 7. Examining the distribution of path lengths, see **Figure 9** I observe that the majority of nodes have a path length of 2. This means that the average node in the network is only 2 steps away from most other nodes. Hence the overall network is well connected. Examining the in-degree distributions of nodes in the network, see **Figure A4** in the appendix, I remarked that some nodes have very many connections, while the majority of nodes have only a few (one or two) connections. A network containing very few highly connected nodes and very many poorly connected nodes implies it bears a centralized network structure. This can also be seen in **Figure 10** the graph of average clustering coefficient as a function of number of neighboring nodes, where I observed two distinct clusters of nodes. Nodes higher up in the hierarchy are well connected to a small number of neighbors. While nodes lower down in the hierarchy are poorly connected to a larger number of neighbors. A third network parameters additionally indicating a very centralized network structure is the distribution of betweenness centrality values. **Figure A6** shows a distribution where only 3 nodes, each of which only have two neighbors, have elevated betweenness centrality values, reflecting the amount of control these nodes exerts over the interactions of other nodes. Demonstrating that the network is highly centralized, with three very important central nodes which exert control over all other nodes in the network. ENVO:*geographic feature* [ENVO_00000000] is an example of one of these central nodes, having the largest degree of in-connectivity in the envoPolar graph. This is logical as this node is relatively high in the material entity hierarchy. The nodes in-degree value of 44 means there are 44 classes in the envoPolar network which fall underneath the geographic feature hierarchy.

Highly centralized networks are termed scale free or power law networks [@Choroma_ski_2013], which describe an exponential relationship between the degree of connectivity a node has and the frequency of its occurrence. Examining the topology of the envoPolar network I observe a hierarchical and branched tree-like structure. Branching structures are typically much more efficient ways of connecting networks, as the branching structures provide an exponential growth in the number of nodes that can be reached relative to the path length traversed [@Kou_2014]. Allowing for a very short average path length within a very large network, which is what I observed in the envoPolar network.   

In terms of robustness a scale free network won't be dramatically affected by removing or changing low degree nodes, however it would be very affected if the central nodes were removed or changed. If for example the Basic Formal Ontology hierarchy were no longer used and suddenly a very central node such as ENVO:*geographic feature* [ENVO_00000000] were to be removed without replacement, the network would shatter into many unconnected components, rendering it unable to interconnect information. In the current organizational structure the majority of nodes are only  two steps away from highly centralized and well-connected *hub* nodes. Through these highly centralized nodes the network is very highly interconnected. This is due to the hierarchical organizational structure of the ontology.

The majority of nodes, however, are not very well connected to. The results of **Table 12** show that only a handful of nodes with high in-degree values are polar related semantic terms sourced from lower down in the hierarchy. Furthermore the low average in connectivity of nodes in the network implies that most nodes are not well connected to by other nodes. Hence it is my assessment that more work is needed to encode the potential relationships which exist between classes. Building upon the relational connectivity of the envoPolar knowledge graph will be necessary in order for nodes within the graph to be of sufficient in-connectivity to facilitate the discovery of new knowledge based on relationships to stated input knowledge.


## 4.3 Challenges and solutions in tracking information provenance

Jackson’s (2012) bestiary of ignorance proposes four categories in an overview of knowledge or lack of knowledge about a subject, the most subtle yet possibly most important of which describes unknown known knowledge [@Jackson_2012]. Unknown known knowledge refers to scientific knowledge which has been generated or recorded, but to which easy access is lacking [@Hortal_2015]. Hortal et al. (2015) propose that informatics methods could be employed to facilitate community access to non-easily search-able knowledge collections [@Hortal_2015]. Considering informatics strategies by which to improve community access to unknown known knowledge, I examined various types of information which ontologies could be used to track the provenance of. I discuss ways in which ontology knowledge graphs can help to identify the provenance of primary literature associated with annotated datasets, specimens from a museum or collection, and authors who contribute expert knowledge to ontologies. Mobilizing known unknown information data and knowledge into a greater ontology knowledge graph, is a first step toward overcoming the limitation of known unknown knowledge.  

In reference to CQ (9), I evaluated the fitness for purpose of using ontologies to connect users to primary literature about datasets annotated with ontology terms. The results of which demonstrate the ontology knowledge graph can be used to direct users toward publications associated with datasets annotated with terms discovered from the ontology knowledge graph. For example, by searching for publications about BFO:*part of* [BFO_0000050] a ENVO:*marine biome* [ENVO_00000447] the ontology knowledge graph lead us to papers about a ENVO:*marine water body* [ENVO_00001999]. In some cases this process leads us to publications written about the data set of interest. For example the publication *Influence of snow depth and surface flooding on light transmission through Antarctic pack ice* [@Arndt_2017], about the *Influence of snow depth and surface flooding on light transmission through Antarctic pack ice, supplementary data* dataset. This publication was retrieved due to the dataset being annotated as being an OBCS:*data matrix* [OBCS_0000120] about some PATO:*physical* quality* [PATO_0001018] and (RO:*inheres in* [RO_0000052] some (ENVO:*marine water body* [ENVO_00001999]) and (RO:*adjacent to* [RO_0002220] some ENVO:*sea ice* [ENVO_00002200]))

In other cases publication less directly related to a dataset about a part of an ENVO:*marine biome* [ENVO_00000447], were retrieved. Such as for example the publication *An evaluation of the application of CHEMTAX to Antarctic coastal pigment data* [@Kozlowski_2011], which made use of a subset of the data from the *Global chlorophyll "a" concentrations for diatoms, haptophytes and prokaryotes obtained with the Diagnostic Pigment Analysis of HPLC data compiled from several databases and individual cruises.* dataset. This publication was retrieved as it is referenced in a dataset annotated as being an OBCS:*data matrix* [OBCS_0000120] about some CHEBI:*chlorophyll a [CHEBI_18230] and (RO:*part of* [BFO_0000050] some ENVO:*marine water body* [ENVO_00001999])

Although these are relatively uninteresting examples of retrieving publication referenced in a dataset about a term of interest. They demonstrate proof of concept for the interconnection of datasets and publications annotated using ontology terms. This process could be applied to search for data annotated at a higher level of granularity. For example to search for publications which use datasets about a prokaryotic phytoplankton community bloom occurring in icebergs calved from Antarctic glaciers in the Weddell Sea. Semantically expressed as some: PCO:*phytoplankton community bloom* [URI pending] and (RO:*composed primarily of* [RO_0002473] some *prokaryotic organisms* and (RO:*overlaps* [RO_0002131] some RO:*output of* [RO_0002353] some  ENVO:*iceberg calving process* [ENVO_03000031] and (RO:*located in* [RO_0001025] some GAZ:*Weddell Sea* [GAZ_00004045]))).

A semantic annotation such as this could be realized by using the open source gazetteer GAZ [@gaz_2015], an ontologically-oriented listing of place names. Which could be used to provide the semantic annotation for a specific geographic feature of interest such as the GAZ:*Weddell Sea* [GAZ_00004045]. Terms such as *phytoplankton community bloom* or *prokaryotic organisms* could be provided by the Population and Community Ontology. The objective being to interconnect data sets and publications annotated at a very specific level of granularity. Allowing users to ask questions such as:

> "What publications reference datasets about prokaryotic phytoplankton community bloom occurring in icebergs calved from Antarctic glaciers in the Weddell Sea?"

These same semantic data annotation, querying and retrieval principals could also be used to facilitate the search for information about specimens. For example if natural history collections containing preserved NCBITaxon:*Alveolata* [NCBITaxon_33630] (dinoflagellates), were to encode information about the morphologies of such specimens in queryable formats with ontology term annotations. Providing an specimen annotation such as some: owl:*NamedIndividual* [NamedIndividual] and (rdf:*subClassOf* [subClassOf] some  NCBITaxon:*Alveolata* [NCBITaxon_33630] and (*has role* [RO_0000087] some OBI:*specimen role* [OBI_0000112] and (RO:*has quality* [RO_0000086] some PATO:*morphology* [PATO_0000051]))).

Users would be enabled to ask questions of the query-able natural history specimen collections such as:

> "What are all possible morphologies of Alveolata species for which there are collected specimens?"

This would go a long way toward facilitating the ease of access to knowledge about unconnected parts of the collective scientific knowledge base, helping the scientific community to overcome the challenge of coping with unknown known knowledge.

Ontologies can also be used to track the provenance of term authors who have contributed expert knowledge to an ontology knowledge graph. There is a need to track the provenance of expert knowledge authorship, as scientific discoveries are increasingly being enabled through Internet based collaboration [@nielsen_2012]. Ontologies are semantic representations of expert knowledge, and thus have the potential to facilitate on-line networking among scientists, allowing users to connect to the authors who have contributed their expert knowledge.

In order for ontologies to facilitate future scientific networking and discoveries, ontologies would benefit from more domain experts recording their knowledge into ontologies. To incentivize such actions, ontologies would benefit from micro-crediting knowledge contributions at the term level. To facilitate scientific networking, authors who contribute knowledge to ontologies should be micro-credited with unambiguous personal identifiers. These identifiers would need to be connected to a living system which is query-able. Allowing for users to query the ontology knowledge for any authors who contributed knowledge related to specific input terminology of interest. Enabling a query such as:

> "Find the contract information for all authors who contributed knowledge to the sea ice terminology hierarchy."

A standard method by which to micro-credit authors within ontologies is to annotate terms with a link to an Open Researcher and Contributor ID (ORCID) [@ORCID_2009]. ORCIDs are persistent digital identifier serving as primary keys to distinguish researchers. ORCID satisfies the requirement of being a permanently maintained persistent living system by which to track author provenance. Being a web service, ORCID also provides an application programming interface by which user contact information can be queried. Authors may change affiliations or contact information multiple times throughout their career; however they would only ever use a single ORCID account. Hence ORCIDs provide a persistent unique identifier fit for the purpose of interconnecting authors of ontology terms to the knowledge they have helped to encode.

In reference to CQ (10), I evaluated the extent to which ontologies serve to interconnect people who contribute knowledge to the knowledge they have contributed. The results of which indicated that only 20% and 50% of terms from the Environment Ontology and its polar subset respectably contain a directly querable author annotation, making it difficult to directly search for the author of a given term. Although ontologies such as ENVO make use of term ranges to identify authors. This information is stored in a separate meta-data owl file, which would be difficult to query for without a priori knowledge of its existence. The practice of using author ID ranges works for ontologies with smaller numbers of contributing authors, but constituents a cumbersome solution for the micro-crediting of many authors who may only ever contribute to a single term. Directly annotating terms with links to contributing author ORCIDs provides a more easily scalable solution for future influxes of contributing authors. The direct annotation of ontology terms with links to the ORCIDs of contributing authors would serve to identify term author provenance. As well as facilitate future networking amongst scientists by connecting ontology term authors to OCRIDs, from which current contact information can be pulled.

## 4.4 Practical and resilient systems for knowledge-representation and data-mobilization

In principal, ontologies can be used to provide machine-readable representations of expert knowledge as well as the semantic infrastructure by which to interconnect and mobilize machine-accessible data. In this section I discuss the practicality of using ontologies to perform such functions, as well as their resilience to the incorporate of new knowledge, or changes to their underlying semantic models. First in reference to CQ (11) I discuss strategies for ontology development to make them resilient to the incorporation of new and possibly contradictory expert knowledge. Next, referencing CQ (12), I discuss the resilience of ontology-enabled data-mobilization workflows, if subject to changes in their underlying semantic models. Finally, referencing CQ (13), I evaluated how practical it is for predicted users to retrieve ontology-annotated machine-accessible data.

Addressing CQ (11), an example of the requirement of ontologies to be resilient to the incorporation of expert knowledge which may have conflicting or partially non-overlapping definitions came up during the VoCamp Glacier Ontology Hackathon community glacial-consultation session [@vocamp_2018], in which different expert knowledge sources presented different definitions of ablation. As ontologies take an agnostic stance when representing knowledge which has multiple definitions or which pertains to competing hypotheses [@Arp_2015], a variety of approaches can be taken in parallel to incorporate such definitional discrepancies into the ontology knowledge graph. This involves determining the differences between competing definitions, finding or creating other semantics to represent these differences and finally creating multiple versions of the term of interest which have subclass axioms referencing their differences. In the ablation case the difference concerned whether or not calving processes contribute to ice ablation processes. Thus I suggested the creation of two different ablation classes, both of which are to be subclasses of the general ENVO:*ice ablation process* [ENVO_01000919]. The first class ENVO:*icemelt-derived ice ablation process* [URI pending] would have the axiom: BFO:*has part* [BFO_0000051] some ENVO:*icemelt* [ENVO_01000721], telling the semantic knowledge layer that this class only refers to ablation which is due to an icemelt process. The second class ENVO:*icemelt or calving-derived ice ablation process* [URI pending], would have the axiom: BFO:*has part* [BFO_0000051] some (ENVO:*icemelt* [ENVO_01000721] or ENVO:*ice calving process* [ENVO_01000917]), telling the semantic knowledge layer that this class represents ablation processes which are due to icemelt and or calving processes. If in the future, more polar data were to be available for analysis; these terms could be used to evaluate the overlap of data retrieved when performing queries for these different definitions of ablation. This could possibly help to ask and answer a question such as:

> "To what extent are calving processes contributing to ice ablation process relative to icemelt processes?"

Addressing CQ (12), I evaluated the extent to which ontology-enabled data-mobilization workflows such as those I developed to mobilize data about participants in any type of ENVO:*sea ice formation process* [ENVO_03000044], are susceptible to potential changes made to their underlying semantic models. I simulated the effects of not using hierarchically structured subclass relations or structured RO relations to retrieve data about participants in ENVO:*sea ice formation process*es [ENVO_03000044] from my datastore. The results of these simulations indicate that my ontology guided data-mobilization workflow would be quite susceptible to changes made to the underlying semantic models employed by ontologies.

The results show that if ontologies didn't make use of hierarchically structured subclass relationships to represent the taxonomy of knowledge, for example representing the knowledge that a first year ice formation process is a type of sea ice formation process, a data-mobilization workflow such as the one I devised would retrieve substantially less data. Additionally, if a non-standardized set of relations were to be used in place of the structured Relations Ontology relations, it would not be possible to use a data-mobilization workflow to retrieve data.

These results illustrate that in order for ontologies to be used in data-mobilization workflows, it is important that the foundational semantic models they employ are not radically changed. This underscores the need for a well-established and well-structured set of semantics to be used to annotate and mobilize machine-accessible data. Although I am not specifically advocating for the use of the OBO Foundry and Library ontologies to serve as the semantic infrastructure for the annotation and mobilization of machine-accessible data, OBO ontologies would be a reasonable choice to do so. OBO ontologies provide a pre-existing, interoperable semantic infrastructure, including the arguably most successful and widely used biomedical ontology, the Gene Ontology [@Ashburner_2000]. Additionally, efforts are underway to align the OBO ontologies, primarily the Environment Ontology with the NASA Semantic Web for Earth and Environmental Technology (SWEET) ontologies [@sweet_2018]. The SWEET ontologies are the *de facto* standards for the formal representation of earth and environmental science domain knowledge [@DiGiuseppe_2014]. Aligned OBO and SWEET semantics hold great potential to aid in the future interconnection of environmental and genomic data.

Addressing CQ (13) I evaluated how practical it would be for potential users of various levels of querying expertise to retrieve ontology-annotated machine-accessible data from my datastore. Lacking the scope to be able to conduct a proper experiment on a study group of scientists with various proficiencies for performing semantic queries to retrieve data from the datastore, I evaluated this question by testing the performance of predicted user stores estimating users of various querying proficiencies to retrieve example data. The results of these predicted user stories indicated that users of basic querying expertise were only able to retrieve a tiny fraction of annotated data, users of intermediate expertise less than half the data and even users advanced users could not fully retrieve all data. Possible reasons for such results may be due to non-uniformities in axiomatic structures used to annotate the example data.

Clearly these outcomes are limited being only user story simulation conducted in place of proper user group analyses. Semantic science advances could be made by creating an open linked data repository with various styles of data annotations of which a user focus group would be tasked with querying. This would serve to inform us as to what axiomatic annotations are readily queryable, lending themselves to successful data mobilization and which are not. Additional efforts could make use of Neuro-Linguistic Programming (NLP) knowledge to create data annotations which are intuitive to average users. Additionally, efforts could be undertaken to find better ways of connecting and storing linked data which make use of more natural linguistic patterns, to attempt to make linked data accessible by methods other than cumbersome and technical SPARQL queries.

Next, I discuss the axiomatic data annotation patterns which the predicted user stories were and were not able to query. I first examine an example axiomatic pattern used to annotate data about *snow thickness*. This annotation axiom was successfully queried by user stories of intermediate expertise and makes use of the following axiom: PATO:*thickness* [PATO_0000915] and (RO:*inheres in* [RO_0000052] some ENVO:*snow*[ENVO_01000406])). This example axiomatic annotation structure, about a thickness quality which is realized in the material entity snow is relatively straight forward. Employing the pattern of:

```
class A, relation 1, some class B
```

When creating an axiomatic data annotation there is trade-off between a complete and correct philosophical description of a subject vs. a more pragmatic linked-data approach intended to make data easily mobilizable. The example of data about *snow thickness*, presents an axiomatic pattern which is a reasonable comprise between a correct description and an easily mobilizable data annotation.

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

In conclusion this work has demonstrated that ontologies are fit for purpose to perform a variety of tasks related to the interconnection of knowledge information and data. In this work I have demonstrated that interoperable environmental and genomic semantics provided by the Environment Ontology and Gene Ontology can be leveraged to interconnect and mobilize machine-accessible omics data annotated with environmental semantics, thus allowing for the comparisons of the genomic potential of different environments, and the creation of novel bioinformatic hypotheses through such comparisons.

Evaluating the fitness for purpose of ontologies to discovery new knowledge and data, I have shown that ontologies can be used to discover and retrieve data about a phenomenon of interest by leveraging knowledge from an ontology graph to retrieved machine-accessible data about such knowledge. I have also shown that the envoPolar ontology knowledge graph is a highly centralized networks due to the hierarchical structure provided by the BFO upper level semantic model, allowing it to efficiently access nodes in the network. The majority of classes, however, have few connections to other classes thus more axiomatic relationships are required in order for the envoPolar networks to facilitate the discovery of new information based on connections to stated information.

I have also shown that ontology knowledge graphs are fit for purpose to identify the provenance of various types of knowledge information and data, such as primary literature associated with annotated datasets, and authors who contribute expert knowledge to ontologies.

In terms of serving as resilient knowledge representation models, I have shown that ontologies are fit for the purpose of incorporating potentially conflicting knowledge into a shared knowledge representation model. I have also shown that in order for ontologies to be used in robust data-mobilization workflows, the foundational semantic models employed by ontologies should not be radically changed. Finally, I have shown that uniform and repetitive annotation patterns can aid in the mobilization of ontology-annotated machine-accessible data.


\newpage

# 6. Outlook

An outlook to this work which is currently underway is the creation of polar terminology to be used for the annotation of polar genomic sequence data. Such terminology would be detailed in cryosphere extension paper to the Minimum Information about any (x) Sequence (MIxS) genomic sequence submission standards [91].

A future outlook from this work could involve the creation of an Environmental Observatory Intelligence System. Such a system would be built using knowledge representation, a branch of artificial intelligence. This would involve the use of axioms which exist in ENVO and GO to build propositional or first order logic models. These logic models would be supplemented with ontology-annotated machine-accessible polar data sourced from current observatory project such as HAUSGARTEN [@Soltwedel_2005] FRAM [@Soltwedel_2013] and AtlantOS [@AtlantOS], as well as future environmental sensor networks which make use of the Sensor Web Enablement (SWE) standards which allow for the creation of an integrated network of sensors [@Broring_2011]. Alignment of the SWE standards with the OBO Foundry semantics would allow for future influxes of sensor data to be used interoperably with GO and ENVO, facilitating large-data enabled monitoring of marine microbial communities. Such a system would be programed to dynamically incorporate new data as it is published or generated by sensors, and could be developed to systematically address interdisciplinary questions such as:

> "Does microbial taxon diversity in deep-sea sediments show resilient patterns over seasonal cycles?"

> "What metabolic processes are enriched in the microbial communities of multi-year sea ice?"

> "Which ranges of nutrients result in high taxon turnover in the epipelagic zone?"

> "Which cellular components are enriched during a bloom induced by sea ice retreat?"

\pagebreak
# References

<div id="refs"></div>


\pagebreak
# Appendices

## A.1 Performing the scientific method in semantic science

Semantic science adaption of scientific method

![**Figure A1:** Digram illustrating the process of performing the scientific method in semantic science. First observations are made about existing knowledge and information which encoded into ontologies. Next hypotheses about whether ontology-encoded knowledge can be used to gather other information and data are created and formalized as competency questions which are used to represent how well ontologies perform essential knowledge-representation and data-mobilization related tasks. Next methods centered around answering competency are used to test the interaction of ontology knowledge graphs and datasets. Data collection involves both the collection of datasets as well as the collection of knowledge from an ontology knowledge graph. Data analysis involves analyzing the interactions between collection data and knowledge. Finally conclusions can be drawn from the results of analyzing the interactions between collected data and knowledge. ](figures/supplemental/scientific_method_in_semantic_research.pdf)

\pagebreak

## A.2 Datasets and semantic annotations included in the datastore

A Model data store of environmental and genomic data was created during this work. The datastore file ``datastore.ttl`` along with detailed description of axioms making use of ontology terms used to post-compositionally annotate the datastore are available in D.S.1.

The following datasets were included in the datastore:

1. Inorganic nutrients measured on water bottle samples at AWI HAUSGARTEN during POLARSTERN cruise MSM29. @bauerfeind2014inmo

2. Physical oceanography and current meter data from mooring TD-2014-LT. @bauerfeind2016poac

3. Chlorophyll a measured on water bottle samples during POLARSTERN cruise ARK-XXIV/2. [@nthig2015camo][@N_thig_2015]

4. Global chlorophyll "a" concentrations for diatoms, haptophytes and prokaryotes obtained with the Diagnostic Pigment Analysis of HPLC data compiled from several databases and individual cruises. [@soppa2017gcac][@Losa_2017]

5. Biogenic particle flux at AWI HAUSGARTEN from mooring FEVI7. [@bauerfeind2009bpfa][@Bauerfeind_2009]

6. Snow height on sea ice and sea ice drift from autonomous measurements from buoy 2015S22, deployed during the Norwegian Young sea ICE cruise N-ICE 2015. [@nicolaus2015shos][@nicolaus2017shaa]

7. Sea ice thickness at Ice Camp 1 on 2013-09-01 (GEM2IceTh_DiveHole_IceStation1). [@ricker2017sita][@Arndt_2017]

8.  Influence of snow depth and surface flooding on light transmission through Antarctic pack ice, supplementary data. [@arndt2017iosd][@Arndt_2017]

9. Ice-algal chlorophyll a and physical properties of multi-year and first-year sea ice of core CASIMBO-CORE-2_11. [@lange2015icaa2][@Lange_2015]

10. Unpublished metagenomic data from deep sea sediments from Hausgarten POLARSTERN Polarstern cruise PS85, encompassing both functional genomic data in the form of preprocessed pfam2go tables as well as 16S taxonomic data, courtesy of Josephine Z. Rapp. This data consisted of four samples collected from Polarstern cruise PS85, at stations 470, 460, 464, 465. Samples 1 and 2 were collected from depths of 1244m and 2403m which best correspond to ENVO:*marine bathyal zone biome* [ENVO_01000026] Samples 3 and 4 were collected from depths of 3531m and 5525m which best correspond to ENVO:*marine abyssal zone biome* [ENVO_01000027]

11. Unpublished transcriptomic data from shallow Helgoland Marine Sediments during a spring phytoplankton bloom, encompassing preprocessed pfam2go tables, courtesy of David Probandt, and Matthew Schechter. These samples were collected from shallow ~8m depth Helgoland Marine Sediments during a spring phytoplankton bloom. Sediments were characterize as being ENVO:*sandy sediment* [ENVO_01000118] from an ENVO:*marine neritic benthic zone biome* [ENVO_01000025]. The first 4 samples: labeled X1-X4 were used.



\newpage
## A.3 Ontology-mobilized environmentally-annotated omics data comparison supplemental

full results of relative proportions of metal ion binding and metal ion transport subclasses

: **Table A1:** Results of the relative genomic and transcriptomic proportions of GO:*transition metal ion transport* [GO_0000041] process in various types of ENVO:*marine benthic biome*s [ENVO_01000024], queried for in the datastore.

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

: **Table A2:** Results of the relative genomic and transcriptomic proportions of GO:*transition metal ion binding* [GO_0046914] molecular functions in various types of ENVO:*marine benthic biome*s [ENVO_01000024], queried for in the datastore.


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

![**Figure A2:** GO:*biological process* [GO_0008150] hierarchy differentiating ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] ENVO:*marine sediments* [ENVO_03000033]. Subclasses of boldfaced terms GO:*biological process* [GO_0008150], GO:*cellular amino acid biosynthetic process* [GO_0008652], and GO*serine family amino acid biosynthetic process* [GO_0009070] are the subjects of the Principal coordinate analyses plots in **Figures 6**, **7** and **8** respectably. GO*serine family amino acid biosynthetic process* [GO_0009070] terms differentiating ENVO:*marine abyssal zone biome* [ENVO_01000027] and ENVO:*marine bathyal zone biome* [ENVO_01000026] from ENVO:*marine neritic benthic zone biome* [ENVO_01000025] ENVO:*marine sediments* [ENVO_03000033], shown in **Figure 8**, are GO:*glycine biosynthetic process* [GO_0006545], and GO:*cysteine biosynthetic process from serine* [GO_0006535]. ](figures/supplemental/GO_bio_process_hierarchy.png){ width=80% }



\pagebreak
## A.4 Ecological analysis of ontology-collected environmental data

As a demonstration of how an ecological analysis could be conducted on machine-actionable data collected via an ontology semantics, I performed a principal component analysis. The data was collected by searching the datastore for data annotated with terms which are present in the axioms of the hypothetical ontology term ENVO:*environmental system determined by a community* [URI pending]

This mock analysis used the collected data to investigate which environmental variables would have the greatest influence on the analysis. **Figure A3** shows a hypothetical principal component analysis showing the effects of the various environmental variables, assembled due to their inclusion in axioms of the term ENVO:*environment determined by a phytoplankton community associated with sea-ice*. The first two PCA axes explain 53.6% of the variance in this analysis with PCA axis 1 explaining 34.0% of variance and PCA axis 2 explaining 19.6% of variance. Included in **Figure A3** are the Environment Ontology terms which were referenced as axioms of the hypothetical term ENVO:*environment determined by a phytoplankton community associated with sea-ice* [URI pending], and from which annotated data was retrieved. For example *SignalStrength_ENVO_00002200* represents a column which is labeled *Signal Strength* which is about a PATO:*degree of illumination* [PATO_0015013] which RO:*inheres in* [RO_0000052] some ENVO:*sea ice* [ENVO_00002200].

![**Figure A3:** Principal Component Analysis on data collected about terms included as axioms of the hypothetical term ENVO:*environment determined by a phytoplankton community associated with sea-ice* [URI pending]  ](figures/assemble_data_for_ ecological_analysis.pdf){ width=90% }

: **Table A3:** Results of the Principal Component Analysis on data collected about terms included as axioms of the hypothetical term ENVO:*environment determined by a phytoplankton community associated with sea-ice* [URI pending], showing the data columns retrieved in the first column, the annotation term by which the data column was retrieved, is shown in the second column. Loadings from principal components 1 and 2 are shown in the third and fourth columns. Rows are ordered in descending order based on PC 1 then PC 2. The first row of the table is a data column about the PATO:*concentration of* [PATO_0000033] CHEBI:*phosphate* [CHEBI_26020] in ENVO:*sea water* [ENVO_00002149].

| data columns            | annotation term                      | PC1 loading | PC2 loading |
|:------------------------|:-------------------------------------|:------------|:------------|
| phosphate               | ENVO:*sea water* [ENVO_00002149]     | 1.22009153  | 0.09015633  |
| nitrate                 | ENVO:*sea water* [ENVO_00002149]     | 1.21200068  | 0.01720033  |
| ice or snow temperature | ENVO:*multiyear ice* [ENVO_03000073] | 0.58457003  | 0.82623573  |
| sea ice thickness       | ENVO:*sea ice* [ENVO_00002200]       | 0.52555148  | -0.48198612 |
| signal strength         | ENVO:*sea ice* [ENVO_00002200]       | 0.24304142  | -0.80299701 |
| oxygen                  | ENVO:*sea water* [ENVO_00002149]     | -0.01611319 | 0.87287456  |
| salinity                | ENVO:*sea water* [ENVO_00002149]     | -0.70229106 | 0.21544285  |

Example results of this hypothetical analysis are that ENVO:*sea water* [ENVO_00002149] CHEBI:*phosphate* [CHEBI_26020] and CHEBI:*nitrate* [CHEBI_17632] concentrations have positive PC1 loading values. ENVO:*sea water* [ENVO_00002149] CHEBI:*dioxygen* [CHEBI_15379] and PATO:*salinity* [URI pending] have negative PC1 loading values. ENVO:*sea ice* [ENVO_00002200] PATO:*thickness* [PATO_0000915], and signal strength PATO:*degree of illumination* [PATO_0015013] which RO:*inheres in* [RO_0000052] some ENVO:*sea ice* [ENVO_00002200] have negative PC2 loading values.

\newpage
## A.5 Primary literature associated with datasets part of marine biomes

: **Table A4:** Complete list of digital object identifiers of publications obtained by querying for references of datasets which are about BFO:*part of* [BFO_0000050] an ENVO:*marine biome* [ENVO_00000447].

+---------------+----------------------------+------------------------+
|data annotation|reference DOI               | reference title        |
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
|               |                            |in Fram Strait a compilation\|
|               |                            |of long and short-term \|
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



## A.6 Glacial community consultation working group participants

Participants in the Feb 2, 2018 VoCamp Glacier Ontology Hackathon are listed in the following **Table A2**.

: **Table A5** Participants in the Feb 2, 2018 February VoCamp Glacier Ontology Hackathon and community semantic consultation session.

| participant             | affiliation                                                             |
|:------------------------|:------------------------------------------------------------------------|
| Pier Luigi Buttigieg    | Alfred Wegener Institute Helmholtz Centre for Polar and Marine Research |
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
## A.7 Network analysis supplemental figures

![**Figure A4:** In degree distribution of the envoPolar subset analyzed as a network.](figures/supplemental/in_degree_distribution.jpeg){ width=70% }

![**Figure A5:** Out degree distribution of the envoPolar subset analyzed as a network.](figures/supplemental/out_degree_distribution.jpeg){ width=70% }

![**Figure A6:** Plot of betweenness centrality as a function of number of neighbors of nodes from the envoPolar subset analyzed as a network. ](figures/supplemental/betweenness_centrality.jpeg){ width=70% }


\newpage

## A.8 Development of estimated user stories used in querying expertise simulations

Estimated user stories were developed to evaluate the proficiencies of users of basic, intermediate or advanced querying expertise for performing semantic queryies of the model datastore. The predicted user stories were tested with two mobilization tasks. 1) mobilizing annotated with an exclusive *and* intersection of two ontology terms, 2) mobilizing data annotated as being about parts associated with an ontology term.

Exclusive *and* querying cases used in the first task involved the following pairs of ontology terms: NCBITaxon:*Bacteria* [NCBITaxon_2] and NCBITaxon*Archaea* [NCBITaxon_2157], PATO:*concentration of* [PATO_0000033] and CHEBI*chlorophyll a* [CHEBI_18230], ENVO:*marine current* [ENVO_01000067] and PATO:*velocity* [PATO_0002242], PCO:*microbial community* [PCO_1000004] and PCO:*species diversity* [PCO_0000019], ENVO:sea ice* [ENVO_00002200] and PATO:depth* [PATO_0001595], ENVO:sea ice* [ENVO_00002200] and PATO:*temperature* [PATO_0000146], ENVO:*sea water* [ENVO_00002149] and CHEBI*chlorophyll a* [CHEBI_18230], ENVO:*snow* [ENVO_01000406] and PATO:*thickness* [PATO_0000915].

Data about parts associated with an ontology term querying cases used in the second task involved the following term annotations by which to query for data: ENVO:*brine channel* [ENVO_03000041], CHEBI:*carbon atom* [CHEBI_27594], CHEBI:*cation* [CHEBI_36916], IAO:*centrally registered identifier symbol* [IAO_0000577], ENVO:*glacier* [ENVO_00000133], ENVO:*marine biome* [ENVO_00000447], ENVO:*melt pond* [ENVO_03000040], and finally ENVO:*ocean* [ENVO_00000015].

The predicted user stories were programed to have knowledge of a subset of the turtle data annotation querying case property paths used in the datastore. The querying cases the various user stories were programed to include are shown in **Table A6**.

: **Table A6:** SPARQL querying cases which were included for each of the predicted user stories of various querying expertise levels.

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

The following code block shows sudo-code representations of all the querying cases which were included to query for all annotated data included in the model datastore.

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
