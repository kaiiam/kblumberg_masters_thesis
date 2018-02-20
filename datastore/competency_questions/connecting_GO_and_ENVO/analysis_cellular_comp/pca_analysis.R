library(vegan)
library(ggplot2)
library(dplyr)
library(tidyr)
#library(data.table)

#cellular components

#data filtering:

setwd("/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/connecting_GO_and_ENVO/analysis_cellular_comp")

#1
#####################################################################
pca_data <- read.csv(file = "go_envo_data_GO_0044444.csv",header = FALSE)

#filter the bathyl samples 
bathyal <- pca_data %>% filter(grepl('bathyal', V1) )
bat <- rbind(bathyal[3,],bathyal[1,])
colnames(bat) <- as.character(unlist(bathyal[2,]))
colnames(bat)[1] <- "sample"

#filter the abyssal samples
abyssal <- pca_data %>% filter(grepl('abyssal', V1) )
aby <- rbind(abyssal[3,], abyssal[2,] )
colnames(aby) <- as.character(unlist(abyssal[1,]))
colnames(aby)[1] <- "sample"

#order the column names
aby <- aby[colnames(bat)]
#combine the data frames
combined <- rbind(bat,aby)
#strip the url prefix
colnames(combined) <- gsub("http://purl.obolibrary.org/obo/","", colnames(combined))
combined <- mutate(combined, sample =c('1244m','2403m','3531m','5525m'))
combined <- mutate(combined, sample = factor(sample, levels = c('1244m','2403m','3531m','5525m')))

#change the data from character to numeric
#make an index of all columns which are factors
indx <- sapply(combined, is.factor)
#change the first column (sample) not to be changed to numeric
indx[1] <- FALSE
#change the rest of the data to numeric 
combined[indx] <- lapply(combined[indx], function(x) as.numeric(as.character(x)))

# doing pcoa on my data
my.dis <- vegdist(wisconsin(combined[,-1])) 
my.pcoa <- cmdscale(my.dis, eig = TRUE)

#blue to green
colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
#legend("bottomleft", col = colors_vec, lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################


#2
#####################################################################
pca_data <- read.csv(file = "go_envo_data_GO_0044432.csv",header = FALSE)

#filter the bathyl samples 
bathyal <- pca_data %>% filter(grepl('bathyal', V1) )
bat <- rbind(bathyal[3,],bathyal[1,])
colnames(bat) <- as.character(unlist(bathyal[2,]))
colnames(bat)[1] <- "sample"

#filter the abyssal samples
abyssal <- pca_data %>% filter(grepl('abyssal', V1) )
aby <- rbind(abyssal[3,], abyssal[2,] )
colnames(aby) <- as.character(unlist(abyssal[1,]))
colnames(aby)[1] <- "sample"

#order the column names
aby <- aby[colnames(bat)]
#combine the data frames
combined <- rbind(bat,aby)
#strip the url prefix
colnames(combined) <- gsub("http://purl.obolibrary.org/obo/","", colnames(combined))
combined <- mutate(combined, sample =c('1244m','2403m','3531m','5525m'))
combined <- mutate(combined, sample = factor(sample, levels = c('1244m','2403m','3531m','5525m')))

#change the data from character to numeric
#make an index of all columns which are factors
indx <- sapply(combined, is.factor)
#change the first column (sample) not to be changed to numeric
indx[1] <- FALSE
#change the rest of the data to numeric 
combined[indx] <- lapply(combined[indx], function(x) as.numeric(as.character(x)))

# doing pcoa on my data
my.dis <- vegdist(wisconsin(combined[,-1])) 
my.pcoa <- cmdscale(my.dis, eig = TRUE)

#blue to green
colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
#legend("bottomleft", col = colors_vec, lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################


#3
#####################################################################
pca_data <- read.csv(file = "go_envo_data_GO_0044455.csv",header = FALSE)

#filter the bathyl samples 
bathyal <- pca_data %>% filter(grepl('bathyal', V1) )
bat <- rbind(bathyal[3,],bathyal[1,])
colnames(bat) <- as.character(unlist(bathyal[2,]))
colnames(bat)[1] <- "sample"

#filter the abyssal samples
abyssal <- pca_data %>% filter(grepl('abyssal', V1) )
aby <- rbind(abyssal[3,], abyssal[2,] )
colnames(aby) <- as.character(unlist(abyssal[1,]))
colnames(aby)[1] <- "sample"

#order the column names
aby <- aby[colnames(bat)]
#combine the data frames
combined <- rbind(bat,aby)
#strip the url prefix
colnames(combined) <- gsub("http://purl.obolibrary.org/obo/","", colnames(combined))
combined <- mutate(combined, sample =c('1244m','2403m','3531m','5525m'))
combined <- mutate(combined, sample = factor(sample, levels = c('1244m','2403m','3531m','5525m')))

#change the data from character to numeric
#make an index of all columns which are factors
indx <- sapply(combined, is.factor)
#change the first column (sample) not to be changed to numeric
indx[1] <- FALSE
#change the rest of the data to numeric 
combined[indx] <- lapply(combined[indx], function(x) as.numeric(as.character(x)))

# doing pcoa on my data
my.dis <- vegdist(wisconsin(combined[,-1])) 
my.pcoa <- cmdscale(my.dis, eig = TRUE)

#blue to green
colors_vec <- c("#14c4ff","#1461f0","#0d742e","#0A3A0A")

my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
fig <- ordiplot(my.pcoa, type = "none")
text(fig, "species", col="#d43e24", cex=1)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

spp.names <- levels(combined$sample)
#legend("bottomleft", col = colors_vec, lty = 1, legend = spp.names, title="Depth", text.font = 1)
#####################################################################


