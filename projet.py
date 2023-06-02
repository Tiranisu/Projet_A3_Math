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
    print(pays, mag)

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

# instant = np.array(df['lat'])
# pays = np.array(df['lon'])

#Affichage des données avec pylab
# plt.plot(instant, pays, 'ro')
# plt.show()

#Affichage des données avec seaborn
# sns.regplot(x='lat', y='lon', data=df)
# plt.show()