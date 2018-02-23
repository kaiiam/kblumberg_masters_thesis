library(vegan)
library(ggplot2)
library(dplyr)
library(tidyr)
#library(data.table)

#Molecular function

#data filtering:

setwd("/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/connecting_GO_and_ENVO/analysis_molecular_fun")

#transition metal ion binding
###########################################################
pca_data <- read.csv(file = "go_envo_data_GO_0046914.csv",header = FALSE) #this is for the old version without the neritic samples

#filter the bathyl samples 
bathyal <- pca_data %>% filter(grepl('bathyal', V1) )
bat <- rbind(bathyal[1,], bathyal[2,])
colnames(bat) <- as.character(unlist(bathyal[3,]))
colnames(bat)[1] <- "sample"

#filter the abyssal samples
abyssal <- pca_data %>% filter(grepl('abyssal', V1) )
aby <- abyssal[1:2,]
colnames(aby) <- as.character(unlist(abyssal[3,]))
colnames(aby)[1] <- "sample"

#order the column names
aby <- aby[colnames(bat)]
#combine the data frames
combined <- rbind(bat,aby)
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

write.csv(combined, file = "output_numerator.csv",row.names=FALSE)


###########################################################





#all data (may not need this)
###########################################################
pca_data <- read.csv(file = "go_envo_data_all_MF.csv",header = FALSE)

#filter the bathyl samples 
bathyal <- pca_data %>% filter(grepl('bathyal', V1) )
bat <- rbind(bathyal[1,], bathyal[2,])
colnames(bat) <- as.character(unlist(bathyal[3,]))
colnames(bat)[1] <- "sample"

#filter the abyssal samples
abyssal <- pca_data %>% filter(grepl('abyssal', V1) )
aby <- abyssal[1:2,]
colnames(aby) <- as.character(unlist(abyssal[3,]))
colnames(aby)[1] <- "sample"

#order the column names
aby <- aby[colnames(bat)]
#combine the data frames
combined <- rbind(bat,aby)
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


write.csv(combined, file = "output_denominator.csv",row.names=FALSE)


# perform PCA on filtered data
#for PCA see https://rstudio-pubs-static.s3.amazonaws.com/259028_dbe846c67e144065b4c2bcd012fb130d.html

#my.rda <- rda(iris[,-5])
#biplot(my.rda)
#head(iris[,-5])

#########################
# Doing unconstrained RDA (PCA) on my data
#my.rda <- rda(combined[,-1])

#pca_plot <- biplot(my.rda, display = c("sites", "species"), type = c("text", "points"))
#spp.names <- levels(combined$sample)

#Add hulls
#ordihull(my.rda, group = combined$sample, col = c("blue","green"))
#legend("topright", col = c(1,2), lty = 1, legend = spp.names)
#########################

# trying out different analysis 
#data(dune)
#data(dune.env)
#dune.Manure <- rda(dune ~ Manure, dune.env)
#plot(dune.Manure) 

#example pcoA with dune data
# Draw a plot for a non-vegan ordination (cmdscale).
#data(dune)
#dune.dis <- vegdist(wisconsin(dune))
#dune.mds <- cmdscale(dune.dis, eig = TRUE)
#dune.mds$species <- wascores(dune.mds$points, dune, expand = TRUE)
#fig <- ordiplot(dune.mds, type = "none")
#points(fig, "sites", pch=21, col="red", bg="yellow")
#text(fig, "species", col="blue", cex=0.9)
# Default plot of the previous using identify to label selected points

# trying pcoa on my data
#my.dis <- vegdist(wisconsin(combined[,-1])) 
#my.pcoa <- cmdscale(my.dis, eig = TRUE)
#fig <- ordiplot(my.pcoa, type = "text")

#my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
#fig <- ordiplot(my.pcoa, type = "none")
#text(fig, "species", col="red", cex=0.7)
#points(fig, "sites", col=c("blue","blue","green","green"), cex=1.2, pch=21)

#text(fig, "sites", col=c("blue","blue","green","green"), cex=0.9)

#spp.names <- levels(combined$sample)
#legend("topright", col = c("blue","green"), lty = 1, legend = spp.names)

# old example 
#my.pcoa$species <- wascores(my.pcoa$points, combined[,-1], expand = TRUE)
#fig <- ordiplot(my.pcoa, type = "none")
#points(fig, "sites", pch=21, col="red", bg="yellow")
#text(fig, "species", col="blue", cex=0.9)


## Principal coordinates analysis with extended dissimilarities

#data(varespec)
#vare.pcoa <- capscale(varespec ~ 1, dist="bray", metaMDS = TRUE)
#plot <- ordiplot(vare.pcoa, type = "text")

# try pcoa on dune data
#dune.pcoa <- capscale(dune ~ 1, distance = "bray", sqrt.dist = FALSE,
#                  dfun = vegdist, metaMDSdist = TRUE)

#fig <- ordiplot(dune.pcoa, type = "text")

# try pcoa on my data
#my.pcoa <- capscale(combined[,-1] ~ 1, distance = "bray", sqrt.dist = FALSE,
#                      dfun = vegdist, metaMDSdist = TRUE)

#fig1 <- ordiplot(my.pcoa, type = "text")

