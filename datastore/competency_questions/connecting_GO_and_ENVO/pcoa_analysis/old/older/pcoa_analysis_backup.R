library(vegan)
library(ggplot2)
library(dplyr)
library(tidyr)

#Biological Process

#data filtering:
setwd("/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/connecting_GO_and_ENVO/pcoa_analysis")


# all molecular functions 
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_all_MF_in_example.csv",header = TRUE))

#strip the url prefix
colnames(combined) <- gsub("http...purl.obolibrary.org.obo.","", colnames(combined))
combined <- mutate(combined, sample = gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/[a-z]*[_][a-z]*[_]","", sample))
combined <- mutate(combined, sample = gsub(".csv.*","", sample))
combined <- mutate(combined, sample =c('abyssal','abyssal','bathyal','bathyal','neritic','neritic','neritic','neritic'))
combined <- mutate(combined, sample = factor(sample, levels = c('abyssal','bathyal','neritic')))

# doing pcoa on my data
my.dis <- vegdist(decostand(combined[,-1],"hellinger")) 

my.pcoa <- cmdscale(my.dis, eig = TRUE)

#blue to green
#colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################
#way to messy




# organic acid biosynthetic process
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0016053.csv",header = TRUE))

#strip the url prefix
colnames(combined) <- gsub("http...purl.obolibrary.org.obo.","", colnames(combined))
combined <- mutate(combined, sample = gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/[a-z]*[_][a-z]*[_]","", sample))
combined <- mutate(combined, sample = gsub(".csv.*","", sample))
combined <- mutate(combined, sample =c('abyssal','abyssal','bathyal','bathyal','neritic','neritic','neritic','neritic'))
combined <- mutate(combined, sample = factor(sample, levels = c('abyssal','bathyal','neritic')))

# doing pcoa on my data
my.dis <- vegdist(decostand(combined[,-1],"hellinger")) 

my.pcoa <- cmdscale(my.dis, eig = TRUE)

#blue to green
#colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################

#from this we see asparagine biosynthetic process http://purl.obolibrary.org/obo/GO_0006529 has a lot of pull
#hence we try: 

#2 cellular amino acid biosynthetic process http://purl.obolibrary.org/obo/GO_0008652
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

#blue to green
#colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################



#try alpha-amino acid biosynthetic process http://purl.obolibrary.org/obo/GO_1901607
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_1901607.csv",header = TRUE))

#strip the url prefix
colnames(combined) <- gsub("http...purl.obolibrary.org.obo.","", colnames(combined))
combined <- mutate(combined, sample = gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/[a-z]*[_][a-z]*[_]","", sample))
combined <- mutate(combined, sample = gsub(".csv.*","", sample))
combined <- mutate(combined, sample =c('abyssal','abyssal','bathyal','bathyal','neritic','neritic','neritic','neritic'))
combined <- mutate(combined, sample = factor(sample, levels = c('abyssal','bathyal','neritic')))

# doing pcoa on my data
my.dis <- vegdist(decostand(combined[,-1],"hellinger")) 

my.pcoa <- cmdscale(my.dis, eig = TRUE)

#blue to green
#colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################


#what is really differentiating the samples is 
#asparagine biosynthetic process http://purl.obolibrary.org/obo/GO_0006529
#and 
#cysteine biosynthetic process from serine


#hence try aspartate family amino acid biosynthetic process http://purl.obolibrary.org/obo/GO_0009067
#and serine family amino acid biosynthetic process http://purl.obolibrary.org/obo/GO_0009070

#aspartate family amino acid biosynthetic process http://purl.obolibrary.org/obo/GO_0009067
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0009067.csv",header = TRUE))

#strip the url prefix
colnames(combined) <- gsub("http...purl.obolibrary.org.obo.","", colnames(combined))
combined <- mutate(combined, sample = gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/[a-z]*[_][a-z]*[_]","", sample))
combined <- mutate(combined, sample = gsub(".csv.*","", sample))
combined <- mutate(combined, sample =c('abyssal','abyssal','bathyal','bathyal','neritic','neritic','neritic','neritic'))
combined <- mutate(combined, sample = factor(sample, levels = c('abyssal','bathyal','neritic')))

# doing pcoa on my data
my.dis <- vegdist(decostand(combined[,-1],"hellinger")) 

my.pcoa <- cmdscale(my.dis, eig = TRUE)

#blue to green
#colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################
#seperates two of the neritic from the other 4

#serine family amino acid biosynthetic process http://purl.obolibrary.org/obo/GO_0009070
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

#blue to green
#colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")
colors_vec <- c("#1461f0","#1461f0","#14c4ff","#14c4ff","#0d742e","#0d742e","#0d742e","#0d742e")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################

#From that plot we learn the relative gene abundance of
# glycine biosynthetic process http://purl.obolibrary.org/obo/GO_0006545 
#(which has subclass glycine biosynthetic process from serine)
# is more abundant in the deep samples

#whereas
#cysteine biosynthetic process from serine http://purl.obolibrary.org/obo/GO_0006535
#is more abundant in the neretic samples. 
