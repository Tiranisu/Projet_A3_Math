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

#Affichage des données
#print(df)

print("Nombre de séisme en 2014 : %d" %len(df))
print(df['pays'].value_counts()[:20])

instant = np.array(df['lat'])
pays = np.array(df['lon'])

#Affichage des données avec pylab
plt.plot(instant, pays, 'ro')
plt.show()

#Affichage des données avec seaborn
# sns.regplot(x='lat', y='lon', data=df)
# plt.show()