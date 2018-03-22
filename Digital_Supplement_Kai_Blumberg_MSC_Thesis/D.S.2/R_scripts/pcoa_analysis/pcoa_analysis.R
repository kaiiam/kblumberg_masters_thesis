library(vegan)
library(ggplot2)
library(dplyr)
library(tidyr)

#Biological Process

#data filtering:
setwd("") //set the working directory here:

# pcoa on all biological process
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_all_BP_in_example.csv",header = TRUE))

#strip the url prefix
colnames(combined) <- gsub("http...purl.obolibrary.org.obo.","", colnames(combined))
# clean up file names:
combined <- mutate(combined, sample = gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/[a-z]*[_][a-z]*[_]","", sample))
combined <- mutate(combined, sample = gsub(".csv.*","", sample))
#add sample types labels
combined <- mutate(combined, sample =c('abyssal','abyssal','bathyal','bathyal','neritic','neritic','neritic','neritic'))
combined <- mutate(combined, sample = factor(sample, levels = c('abyssal','bathyal','neritic')))

# doing pcoa on my data
my.dis <- vegdist(decostand(combined[,-1],"hellinger")) 
my.pcoa <- cmdscale(my.dis, eig = TRUE)

#blue to green colors
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

#get the species names
my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)

#plot the figure
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=0.9)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)
#####################################################################







#2 pcoa on  cellular amino acid biosynthetic process http://purl.obolibrary.org/obo/GO_0008652
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0008652.csv",header = TRUE))

#strip the url prefix
colnames(combined) <- gsub("http...purl.obolibrary.org.obo.","", colnames(combined))
combined <- mutate(combined, sample = gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/[a-z]*[_][a-z]*[_]","", sample))
combined <- mutate(combined, sample = gsub(".csv.*","", sample))
combined <- mutate(combined, sample =c('abyssal','abyssal','bathyal','bathyal','neritic','neritic','neritic','neritic'))
combined <- mutate(combined, sample = factor(sample, levels = c('abyssal','bathyal','neritic')))

# doing pcoa on my data
my.dis <- vegdist(decostand(combined[,-1],"hellinger")) 
my.pcoa <- cmdscale(my.dis, eig = TRUE)

#colors blue to green
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

#get the species names
my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)

#plot the figure
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)
#####################################################################


#pcoa on serine family amino acid biosynthetic process http://purl.obolibrary.org/obo/GO_0009070
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0009070.csv",header = TRUE))

#strip the url prefix
colnames(combined) <- gsub("http...purl.obolibrary.org.obo.","", colnames(combined))
combined <- mutate(combined, sample = gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/[a-z]*[_][a-z]*[_]","", sample))
combined <- mutate(combined, sample = gsub(".csv.*","", sample))
combined <- mutate(combined, sample =c('abyssal','abyssal','bathyal','bathyal','neritic','neritic','neritic','neritic'))
combined <- mutate(combined, sample = factor(sample, levels = c('abyssal','bathyal','neritic')))

# doing pcoa on my data
my.dis <- vegdist(decostand(combined[,-1],"hellinger")) 
my.pcoa <- cmdscale(my.dis, eig = TRUE)

#colors blue to green
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

#get the species names
my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)

#plot the figure
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)
#####################################################################

#From that plot we learn the relative gene abundance of
# glycine biosynthetic process http://purl.obolibrary.org/obo/GO_0006545 
#(which has subclass glycine biosynthetic process from serine)
# is more abundant in the deep samples

#whereas
#cysteine biosynthetic process from serine http://purl.obolibrary.org/obo/GO_0006535
#is more abundant in the neretic samples. 

#export at 1000 - 730
