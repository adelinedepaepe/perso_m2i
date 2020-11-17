#Ecrire un script python afin de:
# Ajouter un sous tracé ax
#Dessiner un graphique à partir des valeurs aléatoires de 1000 valeurs cumulées(en utilisant numpy)
#Afficher la graduation par dafaut
#Changer la graduation en utilisant des pas de 5(0,5,10,15...)
#Appliquer des étiquettes de la forme xi où i est (0,5,10,15,...)

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()


ax1 = fig.add_subplot(2,2,1)
plt.plot(np.random.randn(50).cumsum())
ax2 = fig.add_subplot(2,2,2)
plt.plot(np.random.randn(50).cumsum())
ax2.set_xticks ( np.arange ( 0, 50, step=5 ) )
ax3 = fig.add_subplot(2,2,3)
plt.plot(np.random.randn(50).cumsum())
ax3.set_xticklabels('x' + str(i) for i in range(200,600,5))
ax4 = fig.add_subplot(2,2,4)
plt.plot(np.random.randn(50).cumsum())
ax4.set_xticklabels('x' + str(i) for i in ax4.get_xticks())



plt.show()