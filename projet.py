# ---------------------------------------------

import pandas as pd
import pylab as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# ----------------- Variables -----------------

# instant : date du séisme
# lat : latitude du séisme
# lon : longitude du séisme
# profondeur : profondeur du séisme
# mag : magnitude du séisme
# pays : région du séisme

#---------------------------------------------#
#                                             #
#----------------- Partie I ------------------#
#                                             #
#---------------------------------------------#

#-------------------- Q1 ----------------------

#----------- Traitement de la DB  -------------

#Lecture du fichier csv
df = pd.read_csv('seismes_2014(1).csv', sep=',')
df[df['mag'].isnull()]
#Affichage des données

#print(df)

#-------------------- Q2 ----------------------

print("Nombre de séisme en 2014 : %d" %len(df))
print(df['pays'].value_counts()[:20])

#-------------------- Q3 ----------------------

table = df['pays'].value_counts()[:20]

nom = table.index.tolist()

#------------------- Q4 -----------------------

mag = []

for pays in nom:
    magn = df[df['pays'] == pays]['mag'].tolist()
    mag.append(magn)
    # print(pays, mag)

# print(nom)
# print(mag)

# Affichage des données avec seaborn & pylab

sns.boxplot(mag,whis=100)
plt.gca().xaxis.set_ticklabels(nom)
plt.xlabel("pays")
plt.ylabel("magnitude")
locs, labels = plt.xticks()
plt.setp(labels, rotation=90)
plt.show()


# 6 pays avec les plus fortes magnitudes

maxMag = df.sort_values(by='mag',ascending = False)['pays'].unique()[:6]
print("6 pays avec les plus fortes magnitudes :",maxMag)

# Séisme de magnitude inférieure ou égale à 2 en Californie et en Alaska

magCalifornia = df[(df['pays']=='California') & (df['mag'] <= 2)].shape[0]
magAlaska = df[(df['pays']=='Alaska') & (df['mag'] <= 2)].shape[0]
print("Nombre de séisme Californie :",magCalifornia)
print("Nombre de séisme Alaska :",magAlaska)

magAlaCali = df[((df['pays']=='Alaska') | (df['pays']=='California')) & (df['mag'] <= 2)].shape[0]
print("Nombre de séisme Ala + cali :",magAlaCali)

#---------------------------------------------#
#                                             #
#----------------- Partie II -----------------#
#                                             #
#---------------------------------------------#

#---------------------------------------------
#Cartes des séismes dans le monde
#---------------------------------------------
#1.
F = pd.DataFrame()
#contenant une magnitude superieur a 3
F = df[df['mag'] >= 3]
#ajouter colonne nommée m avec les entiers des magnitudes
F['m'] = F['mag'].astype(int)
#afficher la taille de F
# print(F.shape)
# print(F)


from datetime import datetime, timedelta
import plotly.express as px

import chart_studio
import chart_studio.plotly as py
chart_studio.tools.set_credentials_file(username='tiranisu', api_key='pk.eyJ1IjoidGlyYW5pc3UiLCJhIjoiY2xpY3dtOGU3MDI2cjNobWk2dGR6c2M4dyJ9.glFr_ld9NLZhLQ3gGhzsXg')

#creer un dictionnaire
palette = {3 : "hotpink", 
           4 : "green", 
           5 : "chocolate", 
           6 : "blue", 
           7 : "red", 
           8 : "black"}


fig = px.density_mapbox(F[F['m'] < 5], lat="lat", lon="lon", hover_name="pays", hover_data=["mag"], zoom=1, radius=10)


G = df[df['mag'] >= 5]
G['m'] = G['mag'].astype(int)
G['size'] = 10 + 10*(G['m'] - 5)
print(G)

fig2 = px.scatter_mapbox(G, lat="lat", lon="lon", hover_name="pays", hover_data=["mag"], zoom=1, color='m', color_continuous_scale=['chocolate', 'blue', 'red', 'black'], size="size")

fig.update_layout(mapbox_style="open-street-map")
fig2.update_layout(mapbox_style="open-street-map")

fig.show()
fig2.show()

#---------------------------------------------#
#                                             #
#----------------- Partie III ----------------#
#                                             #
#---------------------------------------------#



#---------------------------------------------#
#                                             #
#----------------- Partie IV -----------------#
#                                             #
#---------------------------------------------#

#------------------ Notes ---------------------