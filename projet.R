# Installer et charger la bibliothèque "rgl" pour la visualisation 3D
#install.packages("rgl")
library(rgl)

deg2rad <- function(degrees) {
  return(degrees * pi / 180)
}

data <- read.csv("seismes_2014(1).csv")
data[is.na(data)] <- 0

# Convertir les coordonnées de latitude et de longitude en radians
latitude_radians <- deg2rad(data$lat)
longitude_radians <- deg2rad(data$lon)

# Calculer les coordonnées cartésiennes x, y et z à partir de la latitude et de la longitude
x <- cos(latitude_radians) * cos(longitude_radians)
y <- cos(latitude_radians) * sin(longitude_radians)
z <- sin(latitude_radians)

# Normaliser la profondeur entre 0 et 1
profondeur_normalisee <- data$profondeur / 700
profondeur_normalisee <- 1- profondeur_normalisee

# Multiplier les coordonnées cartésiennes par la profondeur normalisée
x <- x * profondeur_normalisee
y <- y * profondeur_normalisee
z <- z * profondeur_normalisee

# Créer une fenêtre de visualisation 3D
open3d()
bg3d("black")

size_ <- as.integer(ceiling(data$mag))
size_
# Ajouter les points sur la sphère à la visualisation
points3d(x, y, z, col = "#fef0d9", size = 2, shininess = 100)
material3d(col = "white", emission = "orange", specular = "white", shininess = 100)

# Afficher la sphère avec les points
aspect3d(1, 1, 1)  # Assure un aspect visuel équilibré de la sphère

