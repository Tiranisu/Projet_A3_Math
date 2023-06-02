#Lire un fichier csv et afficher les données avec pandas, pylab et seabornù


import pandas as pd
import pylab as plt
import seaborn as sns
import numpy as np

# instant : date du séisme
# lat : latitude du séisme
# lon : longitude du séisme
# profondeur : profondeur du séisme
# mag : magnitude du séisme
# pays : région du séisme

#Lecture du fichier csv
df = pd.read_csv('seismes_2014(1).csv', sep=',')
df[df['mag'].isnull()]
#Affichage des données
# print(df)

# instant = np.array(df['lat'])
# pays = np.array(df['lon'])

#Affichage des données avec pylab
# plt.plot(instant, pays, 'ro')
# plt.show()

#Affichage des données avec seaborn
# sns.regplot(x='lat', y='lon', data=df)
# plt.show()


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


fig = px.density_mapbox(F[F['m'] < 5], lat="lat", lon="lon", hover_name="pays", hover_data=["mag"], zoom=1)


G = df[df['mag'] >= 5]
G['m'] = G['mag'].astype(int)
G['size'] = 10 + 10*(G['m'] - 5)
print(G)

fig.add_trace(px.scatter_mapbox(G, lat="lat", lon="lon", hover_name="pays", hover_data=["mag"], zoom=1, color_continuous_scale=list(palette.values()), size="size").data[0])

fig.update_layout(mapbox_style="open-street-map")

#representer l'épicentre des points




fig.show()

