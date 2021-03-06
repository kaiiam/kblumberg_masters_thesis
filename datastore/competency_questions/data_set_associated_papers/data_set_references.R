library(vegan)
library(ggplot2)
library(dplyr)
library(tidyr)
#library(data.table)
require(stats)

setwd("/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/data_set_associated_papers")

#have to open with delimiters being both commas and spaces and save the data_set_assoc_raw.csv to properly format it as
#a csv from the output of previous script!!
data <- read.csv(file = "data_set_assoc_raw.csv",header = FALSE)



#long_DF <- data %>% gather(Quarter, Revenue, V3:V5)






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

write.csv(f_data, file = "post_process_out.csv", row.names = FALSE)












pca_data <- tp_data[2:23,]
colnames(pca_data) <- as.character(unlist(tp_data[1,]))

#colnames(pca_data) <- gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/","", colnames(pca_data))
#combined <- mutate(pca_data, colnames(pca_data) <- gsub("file:/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/build_datastore/","", colnames(pca_data)))

#colnames(pca_data) <- gsub("^.*csv","", colnames(pca_data))
#colnames(pca_data) <- gsub("http...purl.obolibrary.org.obo.","_", colnames(pca_data))

columns_string <- "influence_snow_depth.csvSignalStrength|chlorophyll_a.csvChlorophyllA|inorganic_nutrients.csvNitrate|physical_oceanography.csvOxygen|inorganic_nutrients.csvPhosphate|physical_oceanography.csvSalinity|ice_algal_chlorophyll_myi.csvIceOrSnowTemperature|influence_snow_depth.csvSeaIceThickness"
c <- grep(columns_string, colnames(pca_data))
data <- cbind(pca_data[c])

colnames(data) <- gsub("^.*csv","", colnames(data))
colnames(data) <- gsub("http...purl.obolibrary.org.obo.","_", colnames(data))

#convert from factors to numeric
indx <- sapply(data, is.factor)
data[indx] <- lapply(data[indx], function(x) as.numeric(as.character(x)))

#zscore the data
#find all numeric columns
indx <- sapply(data, is.numeric)
#apply the zcore function via scale to the numeric columns making the result a dataframe.
data.zscored <- as.data.frame(lapply(data[,indx], function(x) scale(x, center = TRUE, scale = TRUE)))

# perform PCA on filtered data
#for PCA see https://rstudio-pubs-static.s3.amazonaws.com/259028_dbe846c67e144065b4c2bcd012fb130d.html

# Doing unconstrained RDA (PCA) on my data
my.rda <- rda(data.zscored)

pca_plot <- biplot(my.rda, display = c("sites", "species"), type = c("text", "points"))

#Add hulls
#spp.names <- levels(data[,1])
#ordihull(my.rda, group = data[,1], col = c("blue","green","orange"))
#legend("topright", col = c("blue","green","orange"), lty = 1, legend = spp.names)
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

