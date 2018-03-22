library(vegan)
library(ggplot2)
library(dplyr)
library(tidyr)
require(stats)

setwd("") //set working directory
#have to open with delimiters being both commas and spaces and save the data_set_assoc_raw.csv to properly format it as
#a csv from the output of previous script!!
data <- read.csv(file = "data_set_assoc_raw.csv",header = FALSE)

#transpose data
t_data <- as.data.frame(t(data))
#grab the data sets names (in this case there is only one so the process is a bit simplified)
first <- as.character(t_data[1,1])
first <- gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/","", first)
first <- gsub(".csv","", first)

#get the purl from the second position. 
purl <- as.character(t_data[2,1])
purl <- gsub("http://purl.obolibrary.org/obo/","", purl)

#filter database cross refferences
f_data <- t_data %>% filter(grepl('https://doi.org/', V1) )
f_data <- f_data %>% filter(!grepl('PANGAEA', V1) )

#write out data after parsing
write.csv(f_data, file = "post_process_out.csv", row.names = FALSE)
