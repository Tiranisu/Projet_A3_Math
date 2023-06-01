#Lire un fichier csv et afficher les données avec pandas, pylab et seabornù


import pandas as pd
import pylab as plt
import seaborn as sns

#Lecture du fichier csv
df = pd.read_csv('seismes_2014(1).csv', sep=';')

#Affichage des données
print(df)

#Affichage des données avec pylab
plt.plot(df['x'], df['y'], 'ro')
plt.show()

#Affichage des données avec seaborn
sns.regplot(x='x', y='y', data=df)
plt.show()



