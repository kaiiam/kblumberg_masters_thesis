library(vegan)
library(ggplot2)
library(dplyr)
library(tidyr)
#library(data.table)

#cellular components

#data filtering:

setwd("/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/connecting_GO_and_ENVO/analysis_cellular_comp_periplasm")
pca_data <- read.csv(file = "go_envo_data_GO_0042597.csv",header = FALSE)

#filter the bathyl samples 
bathyal <- pca_data %>% filter(grepl('bathyal', V1) )
bat <- rbind(bathyal[1,],bathyal[3,])
colnames(bat) <- as.character(unlist(bathyal[2,]))
colnames(bat)[1] <- "sample"

#filter the abyssal samples
abyssal <- pca_data %>% filter(grepl('abyssal', V1) )
aby <- abyssal[2:3,]
colnames(aby) <- as.character(unlist(abyssal[1,]))
colnames(aby)[1] <- "sample"

#order the column names
aby <- aby[colnames(bat)]
#combine the data frames
combined <- rbind(aby, bat)
#strip the url prefix
colnames(combined) <- gsub("http://purl.obolibrary.org/obo/","", colnames(combined))

#make the samples factors
combined <- mutate(combined, sample = gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/[a-z]*[_][a-z]*[_]","", sample))
combined <- mutate(combined, sample = gsub(".csv.*","", sample))
#make the leves for the "sites"
combined <- mutate(combined, sample = factor(sample, levels = c('abyssal','bathyal')))

#change the data from character to numeric
#make an index of all columns which are factors
indx <- sapply(combined, is.factor)
#change the first column (sample) not to be changed to numeric
indx[1] <- FALSE
#change the rest of the data to numeric 
combined[indx] <- lapply(combined[indx], function(x) as.numeric(as.character(x)))

# trying pcoa on my data
my.dis <- vegdist(wisconsin(combined[,-1])) 
my.pcoa <- cmdscale(my.dis, eig = TRUE)
#fig <- ordiplot(my.pcoa, type = "text")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=0.7)
points(fig, "sites", col=c("#1461f0","#1461f0","#0d742e","#0d742e"), cex=1.3, pch=19)

#text(fig, "sites", col=c("blue","blue","green","green"), cex=0.9)

spp.names <- levels(combined$sample)
legend("topright", col = c("#1461f0","#0d742e"), lty = 1, legend = spp.names,title="Deep marine biome type", text.font = 1)

