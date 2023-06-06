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

print("this is df : ",df)

df[df['mag'].isnull()]

print("this is df : ",df)
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

# fig_final.show()

#---------------------------------------------#
#                                             #
#----------------- Partie IV -----------------#
#                                             #
#---------------------------------------------#

# voir fichier R

#---------------------------------------------#
#                                             #
#----------------- Partie V ------------------#
#                                             #
#---------------------------------------------#

#afficher les 20 pays avec le moins de seisme

nbr = 70

table = df['pays'].value_counts()[len(df['pays'].value_counts())-nbr:]

V = pd.DataFrame()
V['Hcount'] = df['pays'].value_counts()
V = V[V['Hcount'] >= 30]

country_list = ['California', 'Alaska', 'Oregon', 'Nevada', 'Washington', 'Hawaii', 'PuertoRico', 'Indonesia', 'Oklahoma', 'Montana', 'Utah', 'PapuaNewGuinea', 'Chile', 'Japan', 'Kansas', 'Wyoming', 'Canada', 'NewZealand', 'Philippines', 'Mexico', 'Fiji', 'SolomonIslands', 'BritishVirginIslands', 'Tonga', 'Idaho', 'Iceland', 'Russia', 'NorthernMarianaIslands', 'Vanuatu', 'SouthoftheFijiIslands', 'Greece', 'Iran', 'DominicanRepublic', 'India', 'China', 'U.S.VirginIslands', 'Peru', 'Argentina', 'Guatemala', 'northernAlaska', 'Tennessee', 'Afghanistan', 'Nicaragua', 'Missouri', 'NorthernMid-AtlanticRidge', 'Arkansas', 'Guam', 'CA', 'Colombia', 'CentralAlaska', 'CarlsbergRidge', 'Taiwan', 'SouthSandwichIslands', 'ElSalvador', 'NorthernCalifornia', 'Turkey', 'Mid-IndianRidge', 'NewCaledonia', 'SouthernAlaska', 'CentralMid-AtlanticRidge', 'Tajikistan', 'EastTimor', 'Japanregion', 'ReykjanesRidge', 'Arizona', 'WallisandFutuna', 'Pacific-AntarcticRidge', 'Burma', 'KurilIslands', 'Ecuador', 'CentralCalifornia', 'Pakistan', 'WesternIndian-AntarcticRidge', 'Texas', 'Panama', 'SouthernEastPacificRise', 'BallenyIslandsregion', 'FederatedStatesofMicronesiaregion', 'Micronesia', 'Colorado', 'SouthernMid-AtlanticRidge', 'SoutheastIndianRidge', 'NewMexico', 'CostaRica', 'Bolivia', 'CentralEastPacificRise', 'Fijiregion', 'Yemen', 'OffthewestcoastofnorthernSumatra', 'SouthofTonga', 'EasterIslandregion']

coastal_list = ['California', 'Alaska', 'Oregon', 'Washington', 'Hawaii', 'PuertoRico', 'Indonesia', 'PapuaNewGuinea', 'Chile', 'Japan', 'Canada', 'NewZealand', 'Philippines', 'Mexico', 'Fiji', 'SolomonIslands', 'BritishVirginIslands', 'Tonga', 'Iceland', 'Russia', 'NorthernMarianaIslands', 'Vanuatu', 'SouthoftheFijiIslands', 'Greece', 'Iran', 'DominicanRepublic', 'India', 'China', 'U.S.VirginIslands', 'Peru', 'Argentina', 'Guatemala', 'Nicaragua', 'Guam', 'Colombia', 'Taiwan', 'SouthSandwichIslands', 'ElSalvador', 'Turkey', 'NewCaledonia', 'EastTimor', 'WallisandFutuna', 'Burma', 'KurilIslands', 'Ecuador', 'Pakistan', 'Texas', 'Panama', 'BallenyIslandsregion', 'FederatedStatesofMicronesiaregion', 'Micronesia', 'CostaRica', 'Yemen']

non_coastal_list = [country for country in country_list if country not in coastal_list]

V['coastal'] = False

# change coastal to True if country is in coastal_list
for country in coastal_list:
    V.loc[country, 'coastal'] = True

area_list = ['423970','1717854','255026','286351','184824','28337','9104','1904569','181196','380800','220080','462840','755276','377975','213283','253338','9984670','268680','300400','1964375','18274','28450','153','747','216632','102775','17234033','477','12189','0','131957','1648195','48671','3287263','9596961','346','1285216','2780400','108889','207199','109247','652230','129494','180694','0','137732','549','0','1141748','642','0','35980','310','20742','0','783562','0','18575','0','0','143100','15410','0','0','295254','124','0','676578','10355','256370','0','881913','0','696241','75420','0','816','702','0','269837','0','0','315194','51100','1098581','0','0','527968','0','0','0']

V['area'] = area_list

# filtrer les pays avec une superficie égale à 0
V = V[V['area'] != '0']

# convertir V en fichier csv
V.to_csv('V.csv', index=True)

#---------------------------------------------

#creer une dataframe data avec les données de df pour les pays de coastal_list
data = df[df['pays'].isin(country_list)]
data[data['mag'].isnull()]

coastal = df[df['pays'].isin(coastal_list)]
coastal[coastal['mag'].isnull()]

non_coastal= df[df['pays'].isin(non_coastal_list)]
non_coastal[non_coastal['mag'].isnull()]

print("data : ",data.shape)
print("coastal : ",coastal.shape)
print("non_coastal : ",non_coastal.shape)

coastal.to_csv('coastal.csv', index=True)
non_coastal.to_csv('non_coastal.csv', index=True)

#---------------------------------------------#

magCEf = pd.DataFrame()
magCEf['effectif'] = coastal['mag'].value_counts()
magCEf['mag'] = magCEf.index.tolist()
magCEf = magCEf[magCEf.index >= 0]
magCEf = magCEf.sort_index()
magCEf['Pays_Cotier'] = 'oui'
magCEf.to_csv('magCEf.csv', index=True)

#division de magC en 2 dataframes
magCEf1 = pd.DataFrame()
magCEf1['mag'] = magCEf['mag']
magCEf1 = magCEf[magCEf1['mag'] <= 3.5]
magCEf1.to_csv('magCEf1.csv', index=True)

magCEf2 = pd.DataFrame()
magCEf2['mag'] = magCEf['mag']
magCEf2 = magCEf[magCEf2['mag'] > 3.5]
magCEf2.to_csv('magCEf2.csv', index=True)



#---------------------------------------------#

magC = pd.DataFrame()
magC['mag'] = coastal['mag']
magC = magC[magC['mag'] >= 0]
# print("magC : ",magC)
magC.to_csv('magC.csv', index=True)

#division de magC en 2 dataframes
magC1 = pd.DataFrame()
magC1['mag'] = magC['mag']
magC1 = magC[magC1['mag'] <= 3.5]
magC1.to_csv('magC1.csv', index=True)

magC2 = pd.DataFrame()
magC2['mag'] = magC['mag']
magC2 = magC[magC2['mag'] > 3.5]
magC2.to_csv('magC2.csv', index=True)

#---------------------------------------------#

magNC = pd.DataFrame()
magNC['effectif'] = non_coastal['mag'].value_counts()
magNC = magNC[magNC.index >= 0]
magNC = magNC.sort_index()
magNC['Pays_Cotier'] = 'non'
magNC.to_csv('magNC.csv', index=True)
# print("magC : ",magC)
# print("magNC : ",magNC)

#---------------------------------------------#

mag = pd.concat([magC, magNC])

# print("mag : ",mag)


mag.to_csv('mag.csv', index=True)

#---------------------------------------------#

japanMag = pd.DataFrame()
japanMag['effectif'] = df[df['pays'] == 'Japan']['mag'].value_counts()
japanMag = japanMag.sort_index()

# print("japanMag : ",japanMag)

japanMag.to_csv('japanMag.csv', index=True)

#---------------------------------------------#
calMag = pd.DataFrame()
calMag['effectif'] = df[df['pays'] == 'California']['mag'].value_counts()
calMag = calMag.sort_index()

# print("calMag : ",calMag)

calMag.to_csv('calMag.csv', index=True)