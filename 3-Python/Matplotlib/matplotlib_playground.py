##matplotlib est un package, un package est un ensemble de classes. pyplot est une class. C'est la plus utilisée dans matplotlib
import matplotlib.pyplot as plt # ou 'from matplotlib import pyplot as plt'
# Numpy = numerical python, permet d'utiliser des fonctions numériques de manière plus rapide
import numpy as np

#arange ~ range de vanilla python,
# mais on utilise numpy car certaines fontions n'existent pas sur python, et le fonctions de python encombrent plus de mémroire
data = np.arange(10)

print(data)

print(type(data))

plt.plot(data)
#Pour accéder à l'aide, aller sur le terminal, taper
#ipython
#puis plt.plot?

#pour afficher le résultat
#plt.show()

#Pour subdiviser les graph
#POur l'aide sur les options plt.figure?
#On crée l'objet figure
fig = plt.figure(figsize=(12,10))

#Puis, au sein de cette fig, on créé pusieurs sous-tracés
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
# 2: nombre total de tracés verticalement,
# 2:nombre de tracés total horizontalement,
# 1: position ciblé pour le tracé en cours
plt.plot(np.random.randn(50).cumsum(),'k--') #random.randn(50) va créer 50 point random, cumsum() fait un cumul
plt.show()


