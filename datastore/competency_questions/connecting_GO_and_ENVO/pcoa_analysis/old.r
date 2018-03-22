

##version for supplemental
# organic acid biosynthetic process http://purl.obolibrary.org/obo/GO_0016053
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

(my.pcoa$eig/(sum(my.pcoa$eig))*100)


spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Benthic biome", text.font = 1)
#####################################################################

#from this we see asparagine biosynthetic process http://purl.obolibrary.org/obo/GO_0006529 has a lot of pull
#hence we try: 



# cellular metabolic process
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0044237.csv",header = TRUE))

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
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Benthic biome", text.font = 1)
#####################################################################



#metabolic process
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0008152.csv",header = TRUE))

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
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Benthic biome", text.font = 1)
#####################################################################
#biological_process cleaned
#remove outliers:
#http://purl.obolibrary.org/obo/GO_0019882
#http://purl.obolibrary.org/obo/GO_0023052
#http://purl.obolibrary.org/obo/GO_0030431
#http://purl.obolibrary.org/obo/GO_0006955
#http://purl.obolibrary.org/obo/GO_0016485
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0008150_cleaned.csv",header = TRUE))

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
text(fig, "species", col="#d43e24", cex=0.6)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

(my.pcoa$eig/(sum(my.pcoa$eig))*100)

spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Benthic biome", text.font = 1)
#####################################################################



#biological_process
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0008150.csv",header = TRUE))

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
text(fig, "species", col="#d43e24", cex=0.4)
points(fig, "sites", col=colors_vec, cex=1.4, pch=19)

(my.pcoa$eig/(sum(my.pcoa$eig))*100)

spp.names <- levels(combined$sample)
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Benthic biome", text.font = 1)
#####################################################################















##small molecule metabolic process
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0044281.csv",header = TRUE))

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
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Benthic biome", text.font = 1)
#####################################################################



##small molecule metabolic process
##cleaned removed GO_0006066
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0044281_cleaned.csv",header = TRUE))

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
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Benthic biome", text.font = 1)
#####################################################################














##cleaned version
#removed outliers: http://purl.obolibrary.org/obo/GO_0018189
# and http://purl.obolibrary.org/obo/GO_0051479
# and http://purl.obolibrary.org/obo/GO_0030418
# organic acid biosynthetic process http://purl.obolibrary.org/obo/GO_0016053
#####################################################################
combined <- as.data.frame(read.csv(file = "go_envo_data_GO_0016053_cleaned.csv",header = TRUE))

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
legend("bottomleft", col = c("#1461f0","#14c4ff","#0d742e"), lty = 1, legend = spp.names, title="Benthic biome", text.font = 1)
#####################################################################


