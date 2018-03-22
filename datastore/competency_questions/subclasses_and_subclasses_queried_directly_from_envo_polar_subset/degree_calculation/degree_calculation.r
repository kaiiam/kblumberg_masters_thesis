library(ggplot2)

#data(diamonds)

setwd("/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/subclasses_and_subclasses_queried_directly_from_envo_polar_subset/degree_calculation")

in_degree_distribution <- as.data.frame(read.csv(file = "in_degree_distribution.csv",header = TRUE))

in_deg_plot <- ggplot(in_degree_distribution, aes(values)) +
               geom_bar(fill="#1461f0") +
               theme_linedraw() +
               #scale_x_discrete(limits=0:45) +
               ylab("Frequency") +
               xlab("In-degree") 

in_deg_plot


ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/subclasses_and_subclasses_queried_directly_from_envo_polar_subset/degree_calculation/in_degree_distribution.jpeg", 
       plot = in_deg_plot, width = 6, height = 4)



out_degree_distribution <- as.data.frame(read.csv(file = "out_degree_distribution.csv",header = TRUE))

out_deg_plot <- ggplot(out_degree_distribution, aes(values)) +
  geom_bar(fill="#1461f0") +
  theme_linedraw() +
  #scale_x_discrete(limits=0:45) +
  ylab("Frequency") +
  xlab("Out-degree") 

out_deg_plot


ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/subclasses_and_subclasses_queried_directly_from_envo_polar_subset/degree_calculation/out_degree_distribution.jpeg", 
       plot = out_deg_plot, width = 6, height = 4)



shortest_path_length_distribution <- as.data.frame(read.csv(file = "shortest_path_length_distribution.csv",header = TRUE))

spld <- ggplot(shortest_path_length_distribution, aes(values)) +
  geom_bar(fill="#1461f0") +
  theme_linedraw() +
  #scale_x_discrete(limits=0:45) +
  ylab("Frequency") +
  xlab("Path length") 

spld


ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/subclasses_and_subclasses_queried_directly_from_envo_polar_subset/degree_calculation/shortest_path_length_distribution.jpeg", 
       plot = spld, width = 6, height = 4)

#avg_clust_coef

avg_clust_coef <- as.data.frame(read.csv(file = "avg_clust_coef",header = TRUE))


acc <- ggplot(avg_clust_coef, aes(x=x,y=y)) +
  geom_point(aes(colour = y)) +
  scale_colour_gradient(low = "blue", high = "red")+
  labs(x = "Number of neighbors", y = "Average clustering coefficient", colour = "average\nclustering\ncoefficient") +
  theme_linedraw() 
  
  
  #geom_bar(fill="#1461f0") +
  #scale_x_discrete(limits=0:45) +
#  ylab("Average clustering coefficient") +
 # xlab("Number of neighbors") 

acc

ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/subclasses_and_subclasses_queried_directly_from_envo_polar_subset/degree_calculation/average_clustering_coefficient.jpeg", 
       plot = acc, width = 6, height = 4)

#Betweenness_centr

Betweenness_centr <- as.data.frame(read.csv(file = "Betweenness_centr",header = TRUE))


bc <- ggplot(Betweenness_centr, aes(x=x,y=y)) +
  geom_point() +
  labs(x = "Number of neighbors", y = "Average clustering coefficient") +
  theme_linedraw() 


#geom_bar(fill="#1461f0") +
#scale_x_discrete(limits=0:45) +
#  ylab("Average clustering coefficient") +
# xlab("Number of neighbors") 

bc

ggsave(filename = "/home/kai/Desktop/grad_school/marmic/master_thesis/kblumberg_masters_thesis/datastore/competency_questions/subclasses_and_subclasses_queried_directly_from_envo_polar_subset/degree_calculation/betweenness_centrality.jpeg", 
       plot = bc, width = 6, height = 4)
