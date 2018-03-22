library(ggplot2)
library(dplyr)

setwd("") //set working directory here

# plot annotations chart
annotation_number_data <- read.csv(file = "query_and_column_and_annotation_number.csv",header = TRUE)

annotation_number_data <- mutate(annotation_number_data, Expertise = factor(Expertise, levels = c('advanced', 'intermediate', 'basic')))

annotation_number <- ggplot(data=annotation_number_data, aes(x=Query, y=Percent, fill = Expertise)) + 
              geom_col(position="dodge", stat="identity") + 
              coord_flip() +
              theme_linedraw() +
              labs(colour ="Expertise") + scale_fill_manual(values = c("#E47461", "#AEE99A", "#F4F093")) +
              ylab(expression(paste("Percent retrieved" ))) +
              geom_text(aes(label = Percent),
              position = position_dodge(width = 0.9), vjust=0.2, size =2) +
              theme(legend.position = "top")

annotation_number <- annotation_number + facet_grid(. ~ Sample, scales="free", space="free")

#save plot
ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/querying_exclusive_AND_annotations/analysis/query_and_annotation_columns_number.jpeg", 
       plot =  annotation_number, width = 8, height = 5.33)



