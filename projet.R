# Installer et charger la bibliothèque "rgl" pour la visualisation 3D
#install.packages("rgl")
library(rgl)
library(shiny)
library(mapdata)

# Charger les données de contours des pays
data(world2HiresMapEnv)

deg2rad <- function(degrees) {
  return(degrees * pi / 180)
}

data <- read.csv("seismes_2014(1).csv")
data[is.na(data)] <- 0

test <- data$mag[data$mag == "3"]
test

couleurs <- list(
  "3" = "#fef0d9",
  "4" = "#fdd6a0",
  "5" = "#fdcc8a",
  "6" = "#fc9660",
  "7" = "#e34a33",
  "8" = "#b30000"
)

open3d()
#bg3d("black")


for (i in seq(from = 3, to = 8, by = 1)) {
  
  # Convertir les coordonnées de latitude et de longitude en radians
  latitude_radians <- deg2rad(data$lat[data$mag == i])
  longitude_radians <- deg2rad(data$lon[data$mag == i])
  
  # Calculer les coordonnées cartésiennes x, y et z à partir de la latitude et de la longitude
  x <- cos(latitude_radians) * cos(longitude_radians)
  y <- cos(latitude_radians) * sin(longitude_radians)
  z <- sin(latitude_radians)
  
  # Normaliser la profondeur entre 0 et 1
  profondeur_normalisee <- data$profondeur[data$mag == i] / 700
  profondeur_normalisee <- 1 - profondeur_normalisee
  
  # Multiplier les coordonnées cartésiennes par la profondeur normalisée
  x <- x * profondeur_normalisee
  y <- y * profondeur_normalisee
  z <- z * profondeur_normalisee
  
  # Créer une fenêtre de visualisation 3D
  
  
  size_ <- as.integer(ceiling(data$mag))
  size_
  # Ajouter les points sur la sphère à la visualisation
  points3d(x, y, z, col = couleurs[i], size = i*2, add = TRUE)
  #material3d(col = "white", emission = "orange", specular = "white", shininess = 100)
}

# Afficher la sphère avec les points
aspect3d(1, 1, 1)  # Assure un aspect visuel équilibré de la sphère