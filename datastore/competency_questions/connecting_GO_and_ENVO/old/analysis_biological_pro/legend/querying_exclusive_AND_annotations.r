library(ggplot2)
library(dplyr)

#from https://stackoverflow.com/questions/12018499/how-to-put-labels-over-geom-bar-for-each-bar-in-r-with-ggplot2

setwd("/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/connecting_GO_and_ENVO/analysis_biological_pro/legend")

# plot annotations chart
annotation_number_data <- read.csv(file = "query_and_column_and_annotation_number.csv",header = TRUE)

annotation_number_data <- mutate(annotation_number_data, Depth_m = factor(Depth_m, levels = c('1244','2403','3531','5525')))

annotation_number <- ggplot(annotation_number_data, aes(Query, Percent, fill = Depth_m)) + 
              geom_bar(stat="identity", position = "dodge") + 
              theme_linedraw() +
              labs(colour ="Depth") + scale_fill_manual(values = c("#14c4ff","#1461f0","#0d742e","#0A3A0A")) +
              ylab(expression(paste("Percent Retrieved" ))) +
              geom_text(aes(label = Percent),
              position = position_dodge(width = 0.9), vjust=0.2, size =2) 

annotation_number <- annotation_number + theme(axis.text = element_text(angle = 90, hjust = 1))

annotation_number <- annotation_number + facet_grid(Sample ~ ., scales="free", space="free")

annotation_number

ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/querying_exclusive_AND_annotations/analysis/query_and_annotation_columns_number.jpeg", 
       plot =  annotation_number, width = 8, height = 5.33)



