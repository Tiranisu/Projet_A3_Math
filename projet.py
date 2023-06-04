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

E['values'] = E.values

E['index'] = E.index

E['effectif'] = E.values/len(F)*100

E = E.sort_values(by='index',ascending = True)

print("Effectif de chaque magnitude :")
print(E)
print("FIN")

#-------------------- Q2 ----------------------

# figM = px.density_mapbox(F[F['m'] >= 7], lat="lat", lon="lon", hover_name="pays", hover_data=["mag"], zoom=1, radius=10)

H = df[df['mag'] >= 3]
H['m'] = H['mag'].astype(int)

H['size'] = 5 + 2*(H['m']-2)
H = H.sort_values(by='m',ascending = True)

H['m'] = H['m'].astype(str)

# print("hello",H['m'])

# figM = px.scatter_geo(H, lat="lat", lon="lon",
#                      hover_name="pays", size='size',
#                      projection="natural earth", color='m', color_discrete_sequence=["hotpink","green"'chocolate', 'blue', 'red','black'],labels={"m": "Magnitude"})

from plotly.subplots import make_subplots
import plotly.graph_objects as go

# colors = ['hotpink','green','chocolate', 'blue', 'red','black']

# fig_show = go.Figure()

# fig_pie = go.Pie(values=E['effectif'], labels=E["index"], marker=list(palette.values()))

# fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
#                   marker=dict(colors=colors, line=dict(color='#000000', width=2)))

# fig_show.add_trace(fig_pie)

import plotly.graph_objects as go

Q = df[(df["mag"] >= 3) & (df["mag"] < 9)]
Q['m'] = Q['mag'].astype(int)
Q['size'] = 5 + 2 * (Q['m'] - 2)
Q = Q.sort_values(by='m',ascending = True)

colors = ['hotpink','green','chocolate', 'blue', 'red','black']

palettes = {
    3: 'hotpink',
    4: 'green',
    5: 'chocolate',
    6: 'blue',
    7: 'red',
    8: 'black'
}

# Création de la liste de couleurs en fonction des valeurs de m
couleurs = [palettes[m] for m in Q['m']]

fig_final = go.Figure()
    
fig_pie = go.Pie(
    labels=E["index"],
    values=E['values'],
    domain={'x': [0, 0.4], 'y': [0.8, 1]},
    marker_colors=list(palette.values()),
    legendgroup='markers',  # Assignation du même legendgroup pour le trace principal
    title="Répartition",
    name="magnitude"
    )

print("hello maxence",E)

fig_map = go.Scattergeo(
    lat=Q['lat'],
    lon=Q['lon'],
    mode='markers',
    marker=dict(
        size=Q['size'],
        color=couleurs,
        line=dict(width=0.5, color='white')
    ),
    legendgroup='markers',  # Assignation du même legendgroup pour le trace principal
    name="magnitude"
)

# for i in range(3, 9):
#     # Création d'une trace Scattergeo pour chaque valeur de m
#     trace_temp = go.Scattergeo(
#         lat=F[F['m'] == i]['lat'],
#         lon=F[F['m'] == i]['lon'],
#         mode='markers',
#         marker=dict(
#             size=[5 + 5 * (i - 2)],
#             color=['hotpink', 'green', 'chocolate', 'blue', 'red', 'black'][i - 3],
#             line=dict(width=0.5, color='white')
#         ),
#         hoverinfo='none',  # Pas de texte de survol
#         name="m = " + str(i)
#     )

fig_final.add_trace(fig_map)
fig_final.add_trace(fig_pie)

# fig_final.update_traces(hoverinfo='label+percent', textfont_size=20,
#                   marker=dict(colors=colors))

# fig_final.update_layout(
#         title = 'Séisme en 2014 selon leur magnitude',
#         geo_scope='world',
#     )

fig_final.update_geos(projection_type="natural earth")
fig_final.update_layout(
    height=700,
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    dragmode=False,
    title = 'Séisme en 2014 selon leur magnitude',
)

#---------------------------------------------#
fig_final.show()
#---------------------------------------------#

# fig_show.add_trace(
#      go.Scattergeo(H, lat="lat", lon="lon",
#                      hover_name="pays", size='size',
#                      projection="natural earth", color='m', labels={"m": "Magnitude"},color_discrete_sequence=list(palette.values())),
#     row=1, col=1
# )

# fig_show.update_layout(title='Séisme en 2014 selon leur magnitude', title_x=0.5)

# fig3.show()

# fig_show.add_trace(
#      go.Pie(E, values='effectif', names="index", color_discrete_sequence=list(palette.values())),
#      row=1, col=2
# )

# fig_pie.update_layout(
#             title={
#             'text' : 'Répartition',
#             'x':0.5,
#             'xanchor': 'center'
#         })

# fig_pie.show()

# fig_show.update_layout(
#     template="plotly_dark",
#     margin=dict(r=10, t=25, b=40, l=60),
#     annotations=[
#         dict(
#             text="Source: NOAA",
#             showarrow=False,
#             xref="paper",
#             yref="paper",
#             x=0,
#             y=0)
#     ]
# )

# fig_pie.update_traces(hole=0.4)

# fig_show.show()

#associate fig3 and fig4
# fig3.add_trace(fig4.data[0])
# fig3.show()

# fig3.add_trace(fig4.data[0])

# fig3.show()

#---------------------------------------------#
#                                             #
#----------------- Partie IV -----------------#
#                                             #
#---------------------------------------------#
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots

# import pandas as pd

# # read in volcano database data
# df2 = pd.read_csv(
#     "https://raw.githubusercontent.com/plotly/datasets/master/volcano_db.csv",
#     encoding="iso-8859-1",
# )

# # frequency of Country
# freq = df2
# freq = freq.Country.value_counts().reset_index().rename(columns={"index": "x"})

# # read in 3d volcano surface data
# df_v = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/volcano.csv")

# # Initialize figure with subplots
# fig = make_subplots(
#     rows=2, cols=2,
#     column_widths=[0.6, 0.4],
#     row_heights=[0.4, 0.6],
#     specs=[[{"type": "scattergeo", "rowspan": 2}, {"type": "bar"}],
#            [            None                    , {"type": "surface"}]])

# # Add scattergeo globe map of volcano locations
# fig.add_trace(
#     go.Scattergeo(lat=df2["Latitude"],
#                   lon=df2["Longitude"],
#                   mode="markers",
#                   hoverinfo="text",
#                   showlegend=False,
#                   marker=dict(color="crimson", size=4, opacity=0.8)),
#     row=1, col=1
# )

# # Add locations bar chart
# fig.add_trace(
#     go.Bar(x=freq["x"][0:10],y=freq["Country"][0:10], marker=dict(color="crimson"), showlegend=False),
#     row=1, col=2
# )

# # Add 3d surface of volcano
# fig.add_trace(
#     go.Surface(z=df_v.values.tolist(), showscale=False),
#     row=2, col=2
# )

# # Update geo subplot properties
# fig.update_geos(
#     projection_type="orthographic",
#     landcolor="white",
#     oceancolor="MidnightBlue",
#     showocean=True,
#     lakecolor="LightBlue"
# )

# # Rotate x-axis labels
# fig.update_xaxes(tickangle=45)

# # Set theme, margin, and annotation in layout
# fig.update_layout(
#     template="plotly_dark",
#     margin=dict(r=10, t=25, b=40, l=60),
#     annotations=[
#         dict(
#             text="Source: NOAA",
#             showarrow=False,
#             xref="paper",
#             yref="paper",
#             x=0,
#             y=0)
#     ]
# )

# fig.show()
#------------------ Notes ---------------------

# instant = np.array(df['lat'])
# pays = np.array(df['lon'])

#Affichage des données avec pylab
# plt.plot(instant, pays, 'ro')
# plt.show()

#Affichage des données avec seaborn
# sns.regplot(x='lat', y='lon', data=df)
# plt.show()