library(vegan)
library(ggplot2)
library(dplyr)
library(tidyr)
require(stats)

setwd("") //Set the working directory
#have to open and save the PCA_output_data_raw.csv to properly format it as
#a csv from the output of previous script!!
p_data <- read.csv(file = "PCA_output_data_raw.csv",header = FALSE)
tp_data <- as.data.frame(t(p_data))

#take the columns we want
pca_data <- tp_data[2:23,]
colnames(pca_data) <- as.character(unlist(tp_data[1,]))

#chose columns to analyze 
columns_string <- "influence_snow_depth.csvSignalStrength|inorganic_nutrients.csvNitrate|physical_oceanography.csvOxygen|inorganic_nutrients.csvPhosphate|physical_oceanography.csvSalinity|ice_algal_chlorophyll_myi.csvIceOrSnowTemperature|influence_snow_depth.csvSeaIceThickness"
c <- grep(columns_string, colnames(pca_data))
data <- cbind(pca_data[c])

#clean columns labels
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

# Doing unconstrained RDA (PCA) on my data
my.rda <- rda(data.zscored)

#plot pca
pca_plot <- biplot(my.rda, display = c("sites", "species"), cex=2, type = c("text", "points"))

