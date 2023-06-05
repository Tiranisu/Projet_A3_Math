#install.packages('rgl')
library(rgl)
library(ggplot2)

data <- read.csv("seismes_2014(1).csv")
data2 <- read.csv("V.csv")
mag <- read.csv("mag.csv")

ggplot(mag, aes(x=mag, y=effectif, color=coastal))+ 
  geom_point()

#ggplot(magC, aes(x=mag, y=effectif)) + 
#  geom_point()+
 # scale_color_manual(values = c("blue"))+
 # geom_smooth()

#plot.new()
#plot(table(data$mag[data$pays == data2$pays[data2$coastal == "True"]]), type="o", col="blue")

#lines(smooth.spline(magni, nb_seism),col="red",lwd=2)

#lines(smooth(table(data$mag[data$pays == data2$pays[data2$coastal == "True"]])), col = "red", lwd = 2)
#par(new = T)  
#plot(table(data$mag[data$pays == data2$pays[data2$coastal == "False"]]), type="o", axes=F, col="red")

