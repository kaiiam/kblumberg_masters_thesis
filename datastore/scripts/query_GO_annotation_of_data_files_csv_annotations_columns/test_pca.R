library(vegan)

#see https://rstudio-pubs-static.s3.amazonaws.com/259028_dbe846c67e144065b4c2bcd012fb130d.html

my.rda <- rda(iris[,-5])


biplot(my.rda)
