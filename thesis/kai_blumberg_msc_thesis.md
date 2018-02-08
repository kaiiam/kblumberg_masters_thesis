---
title: '\begin{minipage}{\textwidth}\protect\centering
Interconnecting Arctic observatory \\ data through machine-actionable knowledge \\ representation: are ontologies fit for purpose? \\
\end{minipage}'

author: '\begin{minipage}{\textwidth}\protect\centering \textbf{Masters Thesis}\\ submitted by\\ \textbf{Kai Blumberg}\footnote{\url{https://orcid.org/0000-0002-3410-4655}} \end{minipage}'
---

---
toc: True
---

<!---
example comment with example latex table

\begin{table}[hbt]
\caption{Table of Grades}
\centering
\begin{tabular}{llr}
\toprule
\multicolumn{2}{c}{Name} \\
\cmidrule(r){1-2}
First name & Last Name & Grade \\
\midrule
John & Doe & $7.5$ \\
Richard & Miles & $2$ \\
\bottomrule
\end{tabular}
\label{tab:label}
\end{table}


-->
\pagebreak
# Summary

Well this about sums it up xP

\pagebreak
# Introduction

### Rapid effects of climate change on Polar systems


Anthropogenic green house gas emissions are leading to increased climate change and weather extremes.

cite @Naafs_2016 for rapid pace of climate change and how the rate of movement of ecosystems south is unlike anything seen in earth's history making it really hard for species to keep up evolutionarily.

#### Microbes and Biogeochemical cycles
//maybe this can be fit in here? perhaps start with a microbial perspective to keep marmic happy?

> The prokaryotic and eukaryotic microorganisms that drive the pelagic ocean's biogeochemical cycles are currently facing an unprecedented set of comprehensive anthropogenic changes
@Hutchins_2017

#### Arctic climate change
With the a rapidly changing environmental conditions, the Arctic is very vulnerable.

**cite and discuss some Arctic climate change research**
...



//monitoring efforts
### Polar ocean observatories and marine monitoring programs

Polar marine monitoring initiatives such as FRAM ... are working to gauge the effects of climate change on such rapidly changing environments.


#### AtlantOS
//maybe mention this?

the Atlantic Ocean Observation Systems (AtlantOS) [1st AtlantOS Briefing Paper](https://www.atlantos-h2020.eu/2017/02/10/1st-atlantos-briefing-paper/)




#### FRAM & HAUSGARTEN

At the forefront of climate change affected environments are polar habitats.

HAUSGARTEN intro: @Soltwedel_2005

FRAM intro: @Soltwedel_2013



# Make better use of the generated data
// why generate all this Arctic observational data when we can't get the most use of it. ... transition to the need for linked data. COuld also have some other ideas to serve as the transition glue.

## Need for semantics in Environmental data


Observatories generate considerable volumes and varieties of data. The management and integration of such data remains a major obstacle, as the data are often not semantically interoperable. I.e. the data cannot be used in combination, because they are not annotated with a controlled vocabulary of interconnected terms which would allow for a computer to perform logical reasoning upon them.

FROM @Madin_2007 paraphrase and harvest useful introductory material

> Research in ecology increasingly relies on the integration of small, focused studies, to produce larger datasets that allow for more powerful, synthetic analyses. The results of these synthetic analyses are critical in guiding decisions about how to sustainably manage our natural environment, so it is important for researchers to effectively discover relevant data, and appropriately integrate these within their analyses. However, ecological data encompasses an extremely broad range of data types, structures, and semantic concepts. Moreover, ecological data is widely distributed, with few well-established repositories or standard protocols for their archiving and retrieval. These factors make the discovery and integration of ecological data sets a highly labor-intensive task.





### linked data
[wiki](https://en.wikipedia.org/wiki/Linked_data)

Such efforts could benefit from *linked data* a term referring to data which is published in a structured format which allows it to be linked to other data.

This is done by making use of standard web technologies.



 Linked data makes use of Hypertext Transfer Protocol (HTTP) to give data objects a web address, as well as the Resource Description Framework (RDF) @richard_cyganiak_rdf_2014  a ... to share information in a machine-readable format. This allows for

> In computing, linked data (often capitalized as Linked Data) is a method of publishing structured data so that it can be interlinked and become more useful through semantic queries. It builds upon standard Web technologies such as HTTP, RDF and URIs, but rather than using them to serve web pages for human readers, it extends them to share information in a way that can be read automatically by computers.

### semantic web

[wiki](https://en.wikipedia.org/wiki/Semantic_Web)

> The Semantic Web is an extension of the World Wide Web through standards by the World Wide Web Consortium (W3C). @tim_berners-lee_world   The standards promote common data formats and exchange protocols on the Web, most fundamentally the Resource Description Framework (RDF). @david_beckett_rdf_2014

> According to the W3C, "The Semantic Web provides a common framework that allows data to be shared and reused across application, enterprise, and community boundaries".[2] The term was coined by Tim Berners-Lee for a web of data that can be processed by machines[3]—that is, one in which much of the meaning is machine-readable.



> Linked data may also be open data, in which case it is usually described as linked open data (LOD).

### linked open data

read and cite @Auer_2007 about linked open data arguments presented by tim_berners-lee and on the wiki page on open data https://en.wikipedia.org/wiki/Open_data

from the wiki: citing @Auer_2007
> Open data is the idea that some data should be freely available to everyone to use and republish as they wish, without restrictions from copyright, patents or other mechanisms of control.


> Open data which is also linked data is usually termed linked open data.

> Open data may include non-textual material such as maps, genomes, connectomes, chemical compounds,

parlalles with open science  [wiki](https://en.wikipedia.org/wiki/Open_science)

> the movement to make scientific research, data and dissemination accessible to all levels of an inquiring society, amateur or professional.

#### open science

@Molloy_2011 Open Data Means Better Science
> Data provides the evidence for the published body of scientific knowledge, which is the foundation for all scientific progress. The more data is made openly available in a useful manner, the greater the level of transparency and reproducibility and hence the more efficient the scientific process becomes, to the benefit of society. This viewpoint is becoming mainstream among many funders, publishers, scientists, and other stakeholders in research, but barriers to achieving widespread publication of open data remain.


### FAIR
the FAIR data guiding principles (machine-focused findability, accessibility, interoperability reusability) @Wilkinson_2016

AWI data is currently Findable and accessable at a high level for example within Pangaea files. Improvements would be to make the data findable and accessible. Improve Polar data re-usability with the cryo-MIXS extension paper in prep. Most importantly Interoperability, a formally controlled and machine accessible vocabulary, through ontologies, (ENVO, PATO, PCO, ECOCORE).





#### OPeNDAP

> OPeNDAP will be a fundamental component of systems which provide machine-to-machine interoperability with semantic meaning in a highly distributed environment of heterogeneous datasets.

[Open-source Project for a Network Data Access Protocol](https://www.opendap.org/about)
There is a need for semantic interoperability ...




### Internet of things

build up on the semantic web will be the Internet of things, which will have a major inpact on environmental sciences in terms of sensor newtorks ... as there will be be an influx of ocean sciences big data such as sensor networks. SWE SOS and SENSORML



### UN decade of ocean science for sustainable development 2021-2030.

This is related to his work on ocean best practices (to generate such data): as there will be be an influx of ocean sciences big data such as sensor networks. SWE SOS and SENSORML look more into this. Ontologies and this kind of semantic work will be important for mobilize this large data generated by sensor networks, for ocean best practices decade of ocean science. My work will help prepare for this on slot of coming big data using the awi data case study.

### ontology management of big data

For example the HASNetO ontology @Pinheiro_2017
> has been in use to support the data management of a number of large-scale ecological monitoring activities (observations) and empirical experiments.




### Ontologies and the OBO Foundry

Ontology, a human and machine readable semantic representation of domain knowledge ...

An ontology is a hierarchically structured, machine and human readable representation of the knowledge used by experts to describe entities, and capture the relationships between them @Smith_2007. In informatics, ontologies exist in the form of a knowledge graph, where nodes represent entities, and edges represent logical relations linking entities together (i.e. axioms). Ontologies provide a digital semantic infrastructure upon which advanced querying, discovery and analysis of data can occur.

Ontologies are a methodology to systematically structure and connect data, allowing users to ask more complicated questions involving the synthesis of disparate data types which currently can not be combined.

//revise a bit from lab rotation:
Because, no single knowledge graph can encompass the needs of interdisciplinary projects, work must be done in a coordinated fashion with other ontology researchers and developers. In order to interconnect ontologies representing scientific knowledge from different domains, the Open Biological and Biomedical Ontology (OBO) Foundry and Library was created [@Smith_2007]. The OBO Foundry and Library established a set of principles by which to develop and coordinate ontologies such that the scientific knowledge they represent and hence the data they link can interoperate. These ontologies share a common upper level in the hierarchy and use of the same types of logical connective operations to interlink their knowledge. Following these principles are a family of ontologies representing scientific knowledge from non-overlapping domains, which can be used in combination to describe natural phenomena in greater depth. OBO compliant ontologies make use of the Basic Formal Ontology (BFO) @Arp_2015 @bfo_homepage @BFO-ontology, to ensure they have a compatible hierarchical structure, and use logical relations from the Relations Ontology (RO) @obo-relations, to standardize the connections between their knowledge.  

OBO compliant ontologies can be benefit observatory networks such as Hausgarten FRAM, by providing connections between data collected by researchers of different disciplines studying overlapping entities.

//example from my rotation add something like this.
> For example sea ice physicists studying the reflectivity of various ice mass features, may have light intensity data that would help microbial ecologists studying photosynthetic bacteria in brine channels, to calculate the light dependent growth rates of such bacteria



#### ENVO for representing environmental semantics.

ENVO papers: @Buttigieg_2013 @Buttigieg_2016

The Environment Ontology (ENVO) represents expert knowledge about different types of environments[@Buttigieg_2013][@Buttigieg_2016]. ENVO is an OBO aligned ontology.

Environmental knowledge represented by ENVO is used to annotate data from a variety of life science disciplines including oceanography and polar research. [@Buttigieg_2013][@Buttigieg_2016]


#### Gene Ontology
go paper: @Ashburner_2000

GO frequently used to interpret omic data @Ashburner_2000. It has been used to do genomewide RNA expression profile data to compare samples based on shared biological pathways. @Subramanian_2005

The combination of GO and ENVO is less frequently attempted. @Henschel_2015

Paring GO with ENVO is a potential avenue for future study allowing researchers to ask questions such as
> “What is the omic potential of microbes associated with particular environments?”.

#### Example Ontology uses

A communal catalogue reveals Earth’s multiscale microbial diversity. //Uses EMPO a light-weight application ontology built on ENVO the Earth Microbiome Project Ontology
@Thompson_2017
//good to have an example which demonstrates the utility of ENVO for an application ontology to provide utility.  

//from my rotation rewrite example
> Thesen et al.13. show how such a federated semantic approach can enhance handling of environmental and phenotype data, in order to ask increasingly complex questions such as “Which crop varieties are expected to do well in a particular location over the next century?”.
Thesen et al [Emerging semantics to link phenotype and environment](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4690371/) @Thessen_2015


#### PANGAEA

observational networks often upload their data to open access repositories such as the [PANGAEA](https://pangaea.de/)

Although vast quantities of environmental data are freely available to the scientific community, integrated analysis of such data is hindered by a lack of logical connections between different types of data.



#### role of data in [2015 - 2020 ESIP Strategic Plan](http://wiki.esipfed.org/index.php/2015-2020_Strategic_Plan)

[link to my log](https://github.com/kaiiam/kblumberg_masters_thesis/wiki/log#080118)



#### SDGIO


## Policy and SDGIOs

[Making Marine Life Count: A New Baseline for Policy](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1000531)
@Williams_2010 Just use a little bit from this as policy intro.

[DOOS Consultative Draft](http://deepoceanobserving.org/wp-content/uploads/2017/07/DOOS-Consultative-Draft-V5-1-2017-06-19.pdf) (no DOI) for insight into functions that can be understood as ecosystem services of the deep, and thus linked to natural capital.

### UN sustainability development goals in response to climate change

The effects of increased climate change and extreme weather events are hardest felt by indigenous people and the global precariat subsiding via land and ocean subsistence farming and fishing.

[UN publication: TRANSFORMING OUR WORLD: THE 2030 AGENDA FOR SUSTAINABLE DEVELOPMENT](https://sustainabledevelopment.un.org/content/documents/21252030%20Agenda%20for%20Sustainable%20Development%20web.pdf) no DOI reference for the sustainable development goals and targets.

The UN framework for SDG's have setup targets for improvements to many global issues such as UN SDG 14 for ocean health.

14.1

> By 2025, prevent and significantly reduce marine pollution of all kinds, in particular from land-based activities, including marine debris and nutrient pollution

link the nitrogen phosphorus data to the concept of those cycle being out of balance as doccumented in the Planetary Boundaries: Exploring the Safe Operating Space for Humanity paper. @Rockstr_m_2009




United Nations Environment Programme

SDGIO is an OBO compliant ontology

uses the same interoperable semantic standards to ENVO.  Although UNEP PURLS cannot currently be queried.


### Linking earth science data initiatives such ESIP Open knowledge network to the UN SDGIO's

There exist a variety of earth and life science initiatives attempting to capture and represent the knowledge associated with environmental data. ...

The knowledge required to interface the concepts needed for the Sustainable development goals are represented in a machine operable form via the SDGIO sustainable development goals interface ontology.



#### knowledge outreach

Knowledge graphs are becoming more popular and useful, need to bridge the gap between patchy but growing resources such as Wikipedia, and expert knowledge (locked away in text books), using an ontology helps to bridge this, it can be applied to querying Wikipedia data and for improved semantic representation make data FAIR. Ontology for an agreed upon term structure




### competency questions:

In order to leverage growing data and knowledge representation semantic infrastructure we test if a semantic knowledge web represented by an ontologies can be used in combination with AWI data to address competency questions such as:

**************************************

# Materials and Methods

### Datasets used in Datastore

1. Inorganic nutrients measured on water bottle samples at AWI HAUSGARTEN during POLARSTERN cruise MSM29. @bauerfeind2014inmo

2. Physical oceanography and current meter data from mooring TD-2014-LT. @bauerfeind2016poac

3. Chlorophyll a measured on water bottle samples during POLARSTERN cruise ARK-XXIV/2. [@nthig2015camo][@N_thig_2015]

4. Global chlorophyll "a" concentrations for diatoms, haptophytes and prokaryotes obtained with the Diagnostic Pigment Analysis of HPLC data compiled from several databases and individual cruises. [@soppa2017gcac][@Losa_2017]

5. Biogenic particle flux at AWI HAUSGARTEN from mooring FEVI7. [@bauerfeind2009bpfa][@Bauerfeind_2009]

6. Snow height on sea ice and sea ice drift from autonomous measurements from buoy 2015S22, deployed during the Norwegian Young sea ICE cruise N-ICE 2015. [@nicolaus2015shos][@nicolaus2017shaa]

7. Sea ice thickness at Ice Camp 1 on 2013-09-01 (GEM2IceTh_DiveHole_IceStation1). [@ricker2017sita][@Arndt_2017]

8. Ice-algal chlorophyll a and physical properties of multi-year and first-year sea ice of core CASIMBO-CORE-1_10. [@lange2015icaa][@Lange_2015]

9. Ice-algal chlorophyll a and physical properties of multi-year and first-year sea ice of core CASIMBO-CORE-2_11. [@lange2015icaa2][@Lange_2015]

10. Unpublished metagenomic data from deep sea sediments from Hausgarten POLARSTERN Polarstern cruise PS85, encompassing both functional genomic data, and 16S taxonomic data, courtesy of Josephine Z. Rapp.

### programs used:

semantic technologies make use of the specifications of the World Wide Web Consortium (W3C) @tim_berners-lee_world

SPARQL 1.1 Query Language and W3C Recommendation 21 March 2013 query language for RDF @steve_harris_sparql_2013

Python @python Version 2.7.12

RDF 1.1 Concepts and Abstract Syntax W3C Recommendation 25 February 2014 @richard_cyganiak_rdf_2014

RDF specifications turtle @david_beckett_rdf_2014,


Anything To Triples (any23) a library, a web service and a command line tool that extracts structured data in RDF format from a variety of Web documents [@any23].


owl @sean_bechhofer_owl_2004

> The Web Ontology Language OWL is a semantic markup language for publishing and sharing ontologies on the World Wide Web. OWL is developed as a vocabulary extension of RDF (the Resource Description Framework)


 [Protégé](https://protege.stanford.edu/) @Musen_2015 @protege


### Semantic Data Annotation

Semantic annotation of example data was conducted in the RDF serialization turtle, drawing upon its blank node feature to facilitate  scripting owl code in RDF. Annotations make use ontology terms from the OBO Foundry @Smith_2007. Ontology terms can be search for using [Ontobee](http://www.ontobee.org/) A linked data server hosting ontologies and their terms. @Ong2017


### sparql query scripting

scripts to perform queries were written in python verion?

using the rdf-lib module

Queryies preformed against the ontobee endpoint http://sparql.hegroup.org/sparql/ a serive provied by the He Group @Ong2017

The script makes use of a conjunctive graph object from the rdf-lib module, to emulate an RDF triple store.


**************************************

# Results
In my masters thesis work I have devised a semantic data annotation and querying schema. It allows for the phenomena inhering in data, to be represented and searched in the same way as ontology classes. Annotating data to be semantically inter-operable with existing ontologies, allows us to ask questions of interdisciplinary data, making use of the connections between phenomena encoded within ontologies.

In my masters thesis work I have been writing scripts to assemble and query a demonstration datastore comprised of semantically annotated AWI data. As a part of my proposed work, I would create a human and machine-readable web accessible endpoint to host a variety of AWI data, as well as a the semantic search tools to facilitate querying it.

## Competency Questions

experiments to test knowledge model against competency questions.

### Lookup author of ontology term

[see my thesis here](https://github.com/kaiiam/kblumberg_masters_thesis/wiki/thesis-pieces#lookup-author-of-ontology-term)

The Internet is enabling collaborative dissemination of knowledge and data


Ontologies being semantic representations of expert knowledge should empower users to connect knowledge but also facilitate networking among scientists.

Hence as part of the evaluation of the fitness for purpose of ontologies for interconnecting interdisciplinary data, we evaluated the utility of ontologies and semantic querying to retrieve author information about the creator of an ontology term.

An example question question to this effect asks:

> "What are the email addresses of all authors who contributed to ontology classes about any kind of 'sea ice'?"

Evaluating if the semantic layer encoded into ontologies is capable of answering this question, we begin by sending the following query to the [OBO ontology knowledge graph](http://www.ontobee.org/sparql):

\lstset{language=SPARQL}

~~~
PREFIX obo: <http://purl.obolibrary.org/obo/>
SELECT DISTINCT ?term (STR(?label) as ?label) (STR(?author) as ?author)
WHERE
{
  ?term rdfs:subClassOf+ obo:ENVO_00002200;
        rdfs:label ?label;
        obo:IAO_0000117 ?author .
}
ORDER BY ?term
~~~

Finding all subclasses of the term ['sea ice'](http://purl.obolibrary.org/obo/ENVO_00002200) this query uses the ['term editor'](http://purl.obolibrary.org/obo/IAO_0000117) property from the Information Artifact Ontology **CITE IAO** (IAO) to retrieve any author information linked to the terms. The results of which are displayed in the following table.


: Authors information about contributors to sea ice classes.

| label           | author                                                                     |
|:----------------|:---------------------------------------------------------------------------|
| first year ice  | http://orcid.org/0000-0002-3410-4655, http://orcid.org/0000-0002-4366-3088 |
| second year ice | http://orcid.org/0000-0002-3410-4655, http://orcid.org/0000-0002-4366-3088 |
| multiyear ice   | http://orcid.org/0000-0002-3410-4655, http://orcid.org/0000-0002-4366-3088 |


Returned are the ontology classes representing various types of sea ice, along with the author information associated with those classes. A common, though not universally accepted practice in ontology development, is for authors to annotate classes they have contributed to using a hyperlink to an Open Researcher and Contributor ID (ORCID) page. An ORCID code serves as a primary key for a researcher, as well as a webpage to host their public research record information.

the process for obtaing the contact information from the ORCID links is as follows:


Assessing if ontologies and associated semantic systems are fit to the task of automating the retrieval of contact information an experiment was performed to query for of x randomly selected terms from the following ontologies ... , to evaluate what percentage of the sample ontology terms are annotated with ORCIDs or email addresses.

RUN the experiment make a table of results like:

| Ontology | % sampled terms linked to ORCID pages | % sampled terms linked to email addresses |
|:---------|:--------------------------------------|:------------------------------------------|
| Envo ... |                                       |                                           |

I could maybe also write a script to select random terms from a given ontology (making use of the FROM clause) or run the subclasses of query on a top level class using the real ontobee endpoint (not the test one), and randomly sample x number of terms from there.


// Evaluate a bunch of term and see what proportion have an ORCID associated with them.



### Retrieve any data which is about a subclass of sea ice

//easy to bang out [see my thesis here](https://github.com/kaiiam/kblumberg_masters_thesis/wiki/thesis-pieces#retrieve-any-data-which-is-about-a-subclass-of-sea-ice)

### What compounds play a role as algae metabolites?

easy enough to answer Make use of the CHEBI class: [algal metabolite](http://purl.obolibrary.org/obo/CHEBI_84735)

purl

querying the [ontobee sparql endpoint](http://www.ontobee.org/sparql)

\lstset{language=SPARQL}

~~~
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
SELECT DISTINCT ?purl (STR(?label) as ?label)
WHERE
{
  ?purl rdfs:subClassOf/owl:someValuesFrom obo:CHEBI_84735.
  ?purl rdfs:subClassOf/owl:onProperty obo:RO_0000087.
  ?purl rdfs:label ?label.
}
GROUP BY ?purl
LIMIT 10
~~~




This query gives us the purls and the labels of the first 20 classes which are subclasses of 'has role' some algal metabolite

using the restriction has role.

The group by ?purl is to ensure we don't get duplicates of purls which have duplicated labels such as http://purl.obolibrary.org/obo/CHEBI_15756 which has labels: `hexadecanoic acid` and `Hexadecanoic acid`

Returning the following results:

: Compounds serving as algal metabolites.

|                    purl                    |        label         |
|:------------------------------------------:|:--------------------:|
| http://purl.obolibrary.org/obo/CHEBI_17992 |       Sucrose        |
| http://purl.obolibrary.org/obo/CHEBI_80716 |     aplysiatoxin     |
| http://purl.obolibrary.org/obo/CHEBI_90820 |    11(R)-HEPE(1-)    |
| http://purl.obolibrary.org/obo/CHEBI_86386 | 3-mercaptopropionate |
| http://purl.obolibrary.org/obo/CHEBI_17754 |       Glycerin       |
| http://purl.obolibrary.org/obo/CHEBI_17754 |       glycerol       |
| http://purl.obolibrary.org/obo/CHEBI_16810 |  2-oxoglutarate(2-)  |
| http://purl.obolibrary.org/obo/CHEBI_16914 |    salicylic acid    |
| http://purl.obolibrary.org/obo/CHEBI_16914 |    Salicylic Acid    |
| http://purl.obolibrary.org/obo/CHEBI_16811 |      Methionine      |


### Hackathon competency question

> To what extend are polar semantics encoded into the environment ontology accepted by domain experts such as glaciologists.

I was able to test this question during the vocamp glacial hackathon, organized by ... . During the "hackathon" a variety of scientists and domain experts participated in a collaborative semantics research session with the objective of common vocabulary/ontology for glaciers and related concepts to be used and made interoperable between various existing ontologies.

tuned into and deliberated expert knowledge

33 terms formation processes standing stock ice removal from glaciers were the focus of the work. Have a look at the gloceries for the citations for where ruth got these terms.

**table of how many and which of those terms are semantically represented in ENVO?** perhaps a column for number of links to constituents? Pier says yes.

Final envo representation relative to vocamp consensus diagram.

Polar terms | included in ENVO (Y/N or purl) | % axiomatic links captured in ENVO
---|---|---|

In semantic research the term "unpacking" refers to the disambiguation of terms, clarifying and separating out ambiguous or overlapping terminology to arrive at a single set of terms and definitions.


could also make a table about how much of ENVO is represented the BS diagram from the east coast group, and make a case about how we didn't do so much of their BS.

Overall many of the polar terms added to ENVO in the course of this work were generally accepted in a consensus of the domain experts. Work sourced from this hackathon was added to the environment ontology in the ... release.

to the supplemental for this add the list of participants, and perhaps the final diagram.  

classify ice caps ... as glaciers (things not just on land?) We'll fix this in envo. Use the DOI for the hackathon repostory to reference this




### make one or cc's by breaking the OR statement in my scripts
to fetch less of the data, taking only the simpler querying cases and compare how much data I get back make a table, could use the output from a combination of several scripts perhaps even split into several competency questions.

This could definately be done with the script in the  ``kblumberg_masters_thesis/datastore/scripts/query_for_data_about_exclusive_and``  folder.  


something like:

| scenario                   | # of columns returned broken / total | # of annotation axioms broken / total | % data points returned |
|:---------------------------|:-------------------------------------|:--------------------------------------|:-----------------------|
| sea ice types and depth    | 2 / 3                                | 1 / 2                                 |                        |
| sea ice types and pressure | 2 / 3                                | 1 / 2                                 |                        |


this could maybe also be done with the script in  ``query_for_classes_linked_by_input_classes_and_input_properties``

For this case I have


perhaps it would be better to use or ``query_for_parts_associated_with_input_class`` because these cases would be easier scenarios to fit into the table.

where %'s are the broken (limited OR query set case representing novice queries) / complete querying

| scenario                     | % of columns returned | % of csv returned | % of data point returned |
|:-----------------------------|:----------------------|:------------------|:-------------------------|
| parts of a marine water body |                       |                   |                          |
| parts of a sea ice           |                       |                   |                          |





### is it possible to move annotated data

> "Do we have any data about sea ice and if so can we use semantic annotations to retrieve such data?"

### what level of granularity

> "Do we have any data about the depth of any type of sea ice?" "About the temperature of sea ice.?" or depth or sea ice.


### Can a semantic knowledge graph guide scientists toward data which is relevant to a natural process they are studying?


//I'm pretty sure I was using the ``query_for_classes_linked_by_input_classes_and_input_properties``

with the file ``classes_related_by_ENVO_01000950_classes_and_RO_0000057_properties``

participants of water ice formation processes.

I could maybe make several competency questions out of this by cycling through different combinations of input classes and properties paired together. We'll see if this actually generates different results between ice melting and freezing we'll see if not I do have a bunch to talk about. here so maybe it's not necessary to cycle through different combinations or try 'break'  the script and make a table of how well the model performs. 

for example:

> What kinds of data could be used to assess the phenomena of ice formation?


My workflow assembles useful and expected data such as: minimum and maximum sea ice depth, sea ice temperature, the degree of illumination of sea ice, sea ice texture, and thickness of snow on sea ice,

Also retrieved are some unexpected but potentially useful data such as: sea water salinity, sea water chlorophyll and areal chlorophyll a concentration, sea water phosphate and nitrate concentrations.

When assessing the potential of some seawater to freeze, data about the water's salinity valuable as per the relationship between salinity and the freezing point of water.

Nutrient data to asses the role of nutrient limitation on bloom termination, post sea ice retreat.

Also potentially valuable to asses such sea water for it's potential to freeze are data about nitrate, phosphate and chlorophyll, as they are indicators of the biotic activities in such seawater which are most likely linked to the extent to which the ice is freezing. This leads to the generation of more hypothesis about relationships between for example sea ice and nutrient concentrations or chlorophyll which can be harvested into the knowledge graph. Examples of which include the occurrence of blooms associated with the melting of sea ice, or the effects of sea ice melting on on water body stratification, which could potentially inhere in the nutrient data. Codifying such relationships into the semantic layer and using that layer to annotate and mobilize data provides a way illuminate the connections between otherwise disparate data sets, for example using nitrate and phosphate data in combination with other data such as temperature, to help report on the potential freezing or melting processes.


### Connecting GO and ENVO terms

//I should be able to get two different competency questions out of this.

Can we use the semantic layer to get any genomic annotation data about a given set of molecular functions in any type of X environment for example:

> What 'transition metal ion binding' molecular functions are found in marine benthic biomes?

From a preliminary look it appears that in such biomes 'zinc ion binding', and 'iron ion binding' are much more prevalent than the other transition metal ion binding molecular functions.

//Either extend this example or make a new one in which I find some go terms which differentiate the abyssal and bathyl samples and feed those results into a PCA or 2 as proof of concept for an automated system pipeline which to pulls in data and does some ecological analysis on them. Go through the Go term data and try to find GO term which are different between the samples and then query for subclasses of these and queyr for data about those terms and use those results to do the PCA's. (hopefully one or 2 different ones from the different GO upper level terms.)


### biogeochemical cycling

> What types of in interdisciplinary data about the Biogeochemical Silicon Cycle would we expect to access?

for example I get back
* Genomic data annotated with GO terms about silicate metabolic process, silicate transmembrane transporter activity, silicate transport,

* concentration of silicate in seawater

* Data about Particulate Silicon Flux (from the Arctic phytoplankton and particle flux under climate change)


## PCO contributions & Plankton Ecology

//Assuming I get any of this stuff pushed to PCO and or ENVO. I can still write about the semantics qued for addition even if I don't get to push them.

I may still be able to write about the proposed design patterns for PCO, even if I don't get to submit a pull request.

#### Tilman Satelite Data

Paper: Diatom Phenology in the Southern Ocean: Mean Patterns, Trends and the Role of Climate Oscillations. @Soppa_2016 //Associated with the plankton ecology project using Tillman satellite chlorophyll data and the plankton bloom ontology classes. **maybe move this to outlook for how this could be used in a system which draws from larger datasets (like my email to Anya explained)** Plus I could also talk about this paper as a motivation for the PCO terms, harvesting expert Domain knowledge for example from Anya's section doing the full cycle of the scientific with semantic questions.

form a hypothesis, test etc.

example of expert awi knowledge to harvest:

Harvest anya's expert knowledge into ontologies to capturing phenomena such as the "wineglass effect" distribution of mesoscale eddies, and the spacial relationships to carbon fluxes and deep sea export. Also link knowledge about the effects of cyclones, zooplankton migrations, Zooplanton traits (through work on the phenotype and trait ontology PATO).


### cryoMIxS

original MIxS paper: @Yilmaz_2011

//talk about my contributions to the cryoMIxS project. Including work from my lab rotation.

talk about the annotaion for alreal chlorophyll a, plus some of the other terms used to annotate some of the data in the datastore, will work toward the semantic axiomatization and definitions of terms which will be included in the cryoMIxS paper.

#### ENVO releases of interest:
[Ecotone](https://github.com/EnvironmentOntology/envo/releases/tag/v2017-05-10), [Polar express](https://github.com/EnvironmentOntology/envo/releases/tag/v2017-04-15), [Hot tub time machine](https://github.com/EnvironmentOntology/envo/releases/tag/v2017-03-27).





## post compositional data annotation model
//Maybe this could go in material and methods but I'll argue this is a result in the sense of semantic research, a model for data annotation.

In this work we present a novel semantic data annotation model. Semantics have been used to represent data ... //TODO FIND REFS. In this model data annotations are composed of terms from the OBO Foundry. Data annotations are written in The RDF  turtle specification, and structured as nested owl classes. Annotating the data as owl classes ensures parity to the OBO ontologies. This enables us to perform sparql queries on the annotated data in the same manor as would be done to query OBO Foundry ontologies.  

In order to emulated owl code written in RDF, we chose the turtle RDF format for its ability to nest blank nodes within strings of triples.

//ADD THE is about property in the data model, it could also be cool to have a vue figure which explains the workflow.

The creation of ontology classes involves the composition of axioms, the links between classes, which are assembled from other preexisting ontology classes and relational properties. In ontology development this is refereed to as precomposition, which has the effect of taking a set of ontology classes and properties and joining them together in a specific way and assigning this assemblage to be a novel class.

The proposed semantic data annotation model allows for this process to be done in reverse. This is not necessary when an appropriate term for annotation already exists, however, in cases where the appropriate annotation term is lacking, it can be created from a combination of other terms. This practice, referred to as "post composition", enables a user to annotate their data with axioms that comprise a non existent ontology term. By writing the data annotations as owl classes, they are functionally equivalent to existing ontology classes, in terms of their ability to be searched for using a sparql query.

This allows for the phenomena inhering in data, to be represented in a machine readable semantic layer prior to their incorporation as ontology terms.

The model makes use of owl equivalence classes, to structure the annotation as the intersection (and) and or union (or) of post compositionally annotated classes.

Thus the proposed data annotation  model will allow for users, who are not ontologists, to post compositionally annotate their data. //ADD section about how I'll write a tool to automate this in the outlook.

### Example of Post Compositional Data Annotation with Ontology Terms

[change this competency question example](https://github.com/kaiiam/kblumberg_masters_thesis/wiki/thesis-pieces#pre-and-post-composition-of-complex-classes) to be about how to annotate data which is about a **marine environment determined by a diatom community** or a **marine environment determined by a diatom community bloom** instead of being about I intened to create these classes.

**Maybe put this into the PCO contributions section?**





## Vocamp Virtual Glacial Hackathon

[vocamp](http://vocamp.org/wiki/Main_Page):

> VoCamp is a series of informal events where people can spend some dedicated time creating lightweight vocabularies/ontologies for the Semantic Web/Web of Data.

Virtual-Hackahon-on-Glacier-topic

//to be held on Feb. 2nd. I should have an example of moving snow and ice related data ready to demonstrate by then.


### AWI DBPEDIA contributions
Contributing semantic knowledge to the website Wikipedia in the form of an improved heirarchaly structure but aligning with ENVO.

Implement and talk about dpbedia contributions, hopefully they'll let me edit. My intention is to align dbpedia glacial semantics to those in ENVO, should be relatively quick and easy once I can edit.

@Auer_2007 (citation for )

### UNEP SDGIO

Despite operating within a semantically which is interoperable with the OBO Foundry the UNEP ontology is currently non queryable. Future work needs to be done to improve the way SDGIO purls are hosted via UNEP so that they can be querable. This would allow for the the incorporation of data mobililzed via semantics to the UN SDGs to help achieve their objectives.  

**************************************
# Discussion



## Querying Semantically Annotated Data
using polar semantics to annotate AWI Polar data in a machine-readable way. This allows for knowledge to be captured in a data querying

### Creating Classes vs post compositional annotation for data annotation


#### VOCAMP Discussion section:
An example of the semantic clarification that took place during the "hackathon" was coming to a consensus definition of *ablation*. Ontologies take an agnostic stance when representing knowledge which has multiple definitions or which pertains to competing hypothesis. In the *ablation* example the NOAA National Weather Service Glossary 2009 @nws_internet_services_team_glossary_2009 stipulates the restriction that only melting and evaporation processes contribute to ablation. The Cogley et al. IACS-UNESCO Glacier Mass Balance 2011 @cogley_glossary_2011 definition however, refers to all processes which reduce the mass of a glacier. Specifically noting the inclusion of calving processes as significantly contributing to ablation processes.

In order to incorporate such discrepancies into a semantic knowledge graph a variety of approaches can be taken in parallel. A general *ablation* class can be created to include all the possible ice loss processes included in the various definitions of *ablation*. If users are attempting to mobilize data about a specific combination of ice loss process classes, they may post-compose a semantic annotation which includes the specific processes of interest as axioms. A post-compositional annotation describing data specifically about *ablation* due to melting ice and ice calving could for example be:

> ['ice loss process'](http://purl.obolibrary.org/obo/ENVO_01000915) and (['formed as result of'](http://purl.obolibrary.org/obo/RO_0002354) some (['icemelt'](http://purl.obolibrary.org/obo/ENVO_01000721) or ['ice calving process'](http://purl.obolibrary.org/obo/ENVO_01000917)))


If pre-composition is desired, in for example a case where a combination of specific ablation processes are commonly refereed to together as a set, a new term with a descriptive label could be created. A pre-compositional invocation of the example mentioned above would to create a descriptive term such as *calving and icemelt derived ablation*. Having a descriptive human readable label would facilitate the term's use for people such as domain experts or data stewards who are annotating data or describing a specific process. From a linked data perspective, both the pre-compositional and post-compositional annotations of the phenomena in question would make use of the same axiom (above), hence in terms of machine-readability and machine-searchability would be equivalent. This would facilitate the interoperation of data annotated both manually for example with a term such as *calving and icemelt derived ablation* and automatically for example by a semi-automated routine for post-compositionally annotating data, making use of existing terms.


### consistent data structures for published data

outlook/discussion: a semantical data annotation system can work but the data needs to be consistently structured, have a common standard. This isn't too much to ask for, examples like neon national ecological observatory network, tara or osd have fixed standards for data and or metadata.

Demonstrate to research groups such as AWI the importance of consistently structuring data

Could maybe mention the new FAIR tools which are coming to evaluate if data is truly FAIR in terms of interoperability.



## Semantics as AWI Public Outreach
AWI [Education & Communication](https://www.awi.de/en/science/special-groups/bionics/education-communication.html)

Contributions to semantic models such as those discussed in this work serve to improve AWI public outreach efforts to educate and communicate polar research outputs to the public. Dissemination of AWI knowledge has been demonstrated in this work via the contributions made to the open source encyclopedia Wikipedia. This was achieved by aligning the dpbedia ontology glacial semantics to those of ENVO, which were contributed during this work.


**************************************


# Conclusion

This work has demonstrated that semantics can be used to mobilize polar data.

**************************************

# Outlook

**add the stuff from the email to Anya.**

I believe the use of ontologies and semantics data annotation could serve as a valuable tool to address broad biological questions, such as those in the Raes et al. 2017 paper, about which mechanism, temperature or productivity is responsible for marine microbial diversity.

An outlook for the goals presented in this work would be to semantically annotate a wide variety of interdisciplinary AWI datasets in order render such data machine-readable and query-able. This creates the possibility to ask deeper questions of large data sets to address fundamental biological questions such as: "Does microbial diversity coincide with temperature or with primary productivity sourced from nitrogen fixation?"

Such questions could be asked of semantically annotated and machine-readable genomic datasets, which contain basic metadata. Such data could be sourced from anywhere, in house AWI data or already published data, from a variety environmental locations. Working with a data publication service such as PANGAEA to host such data in an open machine-readable web accessible format would allow for complex queries and questions to be asked.

For example to address the aforementioned question, we would perform a query to gather all datasets which include temperature, functional genomic and taxonomic information. From this ecological analysis could be conducted such as testing if temperature tends to correlate with microbial diversity, or with samples enriched in nitrogen fixation genes. The intentional interoperability between the Environment Ontology and the Gene Ontology would facilitate a query for the latter.

**************************************
\pagebreak
# References

<div id="refs"></div>

**************************************
\pagebreak
# Appendices

## Python Scripts and Documentation

### script 1 ...

\lstset{language=Python}
~~~
#!/usr/bin/python

from SPARQLWrapper import SPARQLWrapper, JSON
import rdflib
import rdfextras
import rdflib.graph as g
rdfextras.registerplugins() # so we can Graph.query()
import sys
import re                   #to filter files using regex

########################################################################
# import from sys
#could later use this to accept a list of input classes to query
#in_args = sys.argv[1:]

in_arg = sys.argv[1]

########################################################################
# Put together a sparql query from pieces.

# Put together the PREFIX block:
def prefix_func():
    prefix_list = ['obo: <http://purl.obolibrary.org/obo/>', 'rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>', 'rdfs: <http://www.w3.org/2000/01/rdf-schema#>', 'owl: <http://www.w3.org/2002/07/owl#>', 'html: <http://tools.ietf.org/html/>']
    insert_prefix = ' \nPREFIX '
    return ('PREFIX ' + insert_prefix.join(prefix_list) + '\n' )

# Put together a select block
#takes the query and a bool for whether or not to add a distinct
def select_func(variables, distinct):
    insert_p = ' ?'
    if distinct == 1:
        return ('SELECT DISTINCT ?' + insert_p.join(variables) + '\n' )
    else:
        return ('SELECT ?' + insert_p.join(variables) + '\n')

# Put together a WHERE clause which will only query for subclasses+ of a given input class
def where_subclass_query_func(input_class):
    return 'WHERE {' + '?s rdfs:subClassOf+ <' + str(input_class) + '> . } \n'

#put together a sparql query string which will query for subclasses of a
#given input class
def subclass_query_function(input_class):
    function_list = [prefix_func(), select_func(['s'], 1), where_subclass_query_func(input_class)]
    return ''.join(function_list)

#call the function to query for the subclass of the in_arg
query_for_subclasses = subclass_query_function(in_arg)

########################################################################
# wrap the ontobee SPARQL end-point
endpoint = SPARQLWrapper("http://sparql.hegroup.org/sparql/")
# set the query string
endpoint.setQuery(query_for_subclasses)
# select the return format (e.g. XML, JSON etc...)
endpoint.setReturnFormat(JSON)
# execute the query and convert into Python objects
# Note: The JSON returned by the SPARQL endpoint is converted to nested Python dictionaries, so additional parsing is not required.
results = endpoint.query().convert()

#save the results to a file with the name of the input purl
namestring = str(sys.argv[1])
#remove the http://purl.obolibrary.org/obo/ from the input file.
namestring = re.sub('http://purl.obolibrary.org/obo/', '', namestring)
namestring = re.sub('http://purl.unep.org/sdg/', '', namestring)
#make the file name to write to
outstring = 'subclasses_of_' + namestring + '.txt'

#write out to outfile: query_for_subclasses_of_out.txt
f = open(outstring, 'w')

#write each PURL fetched in query to outfile.
for res in results["results"]["bindings"] :
    f.write(res['s']['value'] + '\n')

~~~

### script 2 ...

**************************************
