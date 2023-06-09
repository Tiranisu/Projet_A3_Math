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

# sns.boxplot(mag,whis=100)
# plt.gca().xaxis.set_ticklabels(nom)
# plt.xlabel("pays")
# plt.ylabel("magnitude")
# locs, labels = plt.xticks()
# plt.setp(labels, rotation=90)
# plt.show()


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
import plotly.graph_objects as go

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
# print(G)

fig2 = px.scatter_mapbox(G, lat="lat", lon="lon", hover_name="pays", hover_data=["mag"], zoom=1, color='m', color_continuous_scale=['chocolate', 'blue', 'red', 'black'], size="size")

fig.update_layout(mapbox_style="open-street-map")
fig2.update_layout(mapbox_style="open-street-map")

# fig.show()
# fig2.show()

#---------------------------------------------#
#                                             #
#----------------- Partie III ----------------#
#                                             #
#---------------------------------------------#

#-------------------- Q1 ----------------------

E = pd.DataFrame()

E['effectif'] = F['m'].value_counts()

E['index'] = E.index

E = E.sort_values(by='index',ascending = True)

#-------------------- Q2 ----------------------

import plotly.graph_objects as go

Q = df[(df["mag"] >= 3) & (df["mag"] < 9)]
Q['m'] = Q['mag'].astype(int)
Q['size'] = 5 + 2 * (Q['m'] - 2)
Q = Q.sort_values(by='m',ascending = True)

fig_final = go.Figure()
    
fig_pie = go.Pie(
    labels=E['index'],
    values=E['effectif'],
    domain={'x': [0, 0.2], 'y': [0.8, 1]},
    marker_colors=list(palette.values()),
    legendgroup='magnitude',  # Assignation du même legendgroup pour le trace principal
    title='Répartition',
    showlegend=False,
    name='Magnitude',
    hovertext='Effectif : ',
    hoverinfo='label+value+percent+text',
    textinfo='percent+label',
    textposition='outside',
    )

for i in range(3, 9):
    # Création d'une trace Scattergeo pour chaque valeur de m
    trace_temp = go.Scattergeo(
        lat=Q[Q['m'] == i]['lat'],
        lon=Q[Q['m'] == i]['lon'],
        mode='markers',
        marker=dict(
            size=Q[Q['m'] == i]['size'],
            color=list(palette.values())[i-3],
            line=dict(width=0.5, color='white'),
        ),
        text = 'Région : '+Q['pays']+'<br>'+'Date : '+Q['instant']+'<br>'+'Profondeur (km) : '+Q['profondeur'].astype(str),
        name=str(i),
    )
    fig_final.add_trace(trace_temp)

fig_final.add_trace(fig_pie)

fig_final.update_geos(
    projection_type="natural earth",
)

fig_final.update_layout(
    height=700,
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    dragmode=False,
    title = 'Séismes en 2014 selon leur magnitude',
    title_x=0.5,
    legend=dict(title="Magnitude")
)

fig_final.show()

#---------------------------------------------#
#                                             #
#----------------- Partie IV -----------------#
#                                             #
#---------------------------------------------#

# pop




#------------------ Notes ---------------------

# instant = np.array(df['lat'])
# pays = np.array(df['lon'])

#Affichage des données avec pylab
# plt.plot(instant, pays, 'ro')
# plt.show()

#Affichage des données avec seaborn
# sns.regplot(x='lat', y='lon', data=df)
# plt.show()
