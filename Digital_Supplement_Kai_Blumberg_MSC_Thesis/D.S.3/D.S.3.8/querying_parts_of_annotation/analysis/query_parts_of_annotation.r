library(ggplot2)
library(dplyr)

setwd("") // set working directory here

# plot annotations chart
parts_of_data <- read.csv(file = "query_parts_of.csv",header = TRUE)

parts_of_data <- mutate(parts_of_data, Expertise = factor(Expertise, levels = c('advanced', 'intermediate', 'basic')))

parts_of_number <- ggplot(data=parts_of_data, aes(x=Query, y=Percent, fill = Expertise)) + 
              geom_col(stat="identity", position = "dodge") +
              coord_flip() +
              theme_linedraw() +
              labs(colour ="Expertise") + scale_fill_manual(values = c("#E47461", "#AEE99A", "#F4F093")) +
              ylab(expression(paste("Percent retrieved" ))) +
              geom_text(aes(label = Percent),
              position = position_dodge(width = 0.9), vjust=0.2, size =2) +
              theme(legend.position = "top")

parts_of_number <- parts_of_number + facet_grid(. ~ Sample, scales="free", space="free")

#save the plot
ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/querying_parts_of_annotation/analysis/query_parts_of_stats.jpeg", 
       plot =  parts_of_number, width = 8, height = 5.33)



