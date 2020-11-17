import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

data = pd.read_csv( 'SPX_exemples.csv', sep=';', index_col=0, parse_dates=True )
print(data)
spx = data['SPX'].sort_index()

#Ici on met spx.plot car on utilise panda. C'est une focntion pandas. On met 'dataframe.plot ='
#spx est la série (ou autrement dit, la colonne), et dans pandas, chaque série a une fonction plot
#Puis ax=ax signifie qu'on veut la fig ax
spx.plot(ax=ax, style='k-')

crisis_data = [
               (datetime(2007, 10, 11), 'Peak of bull market'),
               (datetime(2008, 3, 12), 'Bear Stearns Fails'),
               (datetime(2008, 9, 15), 'Lehman Bankruptcy')
]

for date, label in crisis_data:
  ax.annotate(label, xy=(date, spx.asof(date) + 75),
              xytext=(date, spx.asof(date) + 255),
              arrowprops=dict(facecolor='black', headwidth=4, width=2, headlength=4, rotation=45),
              horizontalalignment='left', verticalalignment='top')

ax.set_xlim(['1/1/2007', '1/1/2011'])
ax.set_ylim([600, 1800])

ax.set_title('Important dates in the 2008-2009 financial crisis')

plt.show()