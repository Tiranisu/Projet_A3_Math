library(ggplot2)

mag <- read.csv("magNC.csv")

ggplot(mag, aes(x=effectif, y=mag, color=coastal))+ 
  geom_point()+
  ggtitle("Comparaison de la répartition des seismes sur les regions non-cotières :")+
  xlab("Magnitude")+ 
  ylab("Nb d'occurance")