library(ggplot2)
library(dplyr)

#from https://stackoverflow.com/questions/12018499/how-to-put-labels-over-geom-bar-for-each-bar-in-r-with-ggplot2

setwd("/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/querying_exclusive_AND_annotations/analysis/facet_wrap")

# plot annotations chart
annotation_number_data <- read.csv(file = "query_and_column_and_annotation_number.csv",header = TRUE)

annotation_number_data <- mutate(annotation_number_data, Expertise = factor(Expertise, levels = c('advanced', 'intermediate', 'basic')))

annotation_number <- ggplot(annotation_number_data, aes(Query, Percent, fill = Expertise)) + 
              geom_bar(stat="identity", position = "dodge") + 
              theme_linedraw() +
              labs(colour ="Expertise") + scale_fill_manual(values = c("#E47461", "#AEE99A", "#F4F093")) +
              ylab(expression(paste("Percentage Retrieved" ))) +
              geom_text(aes(label = Percent),
              position = position_dodge(width = 0.9), vjust=-0.15, size =2.6) 

annotation_number <- annotation_number + theme(axis.text = element_text(angle = 90, hjust = 1))

annotation_number <- annotation_number + facet_grid(Sample ~ ., scales="free", space="free")

annotation_number

ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/querying_exclusive_AND_annotations/analysis/facet_wrap/query_and_annotation_columns_number.jpeg", 
       plot =  annotation_number, width = 8, height = 5.33)



