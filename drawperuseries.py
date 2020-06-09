from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from csv import DictReader
import sys


def process(querydate,filename):
  df = pd.read_csv("./peru24.csv")
  dfs = pd.read_csv("./peru24series.csv")

  fig, ax = plt.subplots(figsize=(15,15))
#ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
# ^
# | Lat
#
# --> Long
#Basemap(fromlong,fromlat,tolong,tolat)

  m = Basemap(llcrnrlon=-84.131577,llcrnrlat=-19.768780,urcrnrlon=-65.870140,urcrnrlat=0.677325,\
            rsphere=(6378137.00,6356752.3142),            resolution='l',ax=ax)

  m.drawcoastlines()

  m.drawcountries(color='black')
  m.drawstates()


  info=dfs.query('Fecha<="%s"'%(querydate))

  S=[]

  for index,row  in df.iterrows():
      dpto=row["Departamento"].strip().upper()
      value=sum(info[dpto])
      S.append(int(value*0.2))

  ax.scatter(df['Lon'], df['Lat'], S, c='red',alpha=0.5)
  for d,la,lo in zip(df['Departamento'],df['Lat'],df['Lon']):
    
    ax.text(lo,la,d,horizontalalignment='center',color='orange')

  ST=sum(S)
  ax.text(-83,-18,"Total :%s"%(ST),color='black')

  ax.set_title(querydate)
  plt.suptitle('Perú',fontsize=18, y=1)
  #plt.show() #enable for debug
  plt.savefig(filename,bbox_inches='tight')
if __name__=="__main__":
  if( len(sys.argv)<3 ):
     print("Usage: python app.py date filename.png")
     exit(0)
  process(sys.argv[1],sys.argv[2])

