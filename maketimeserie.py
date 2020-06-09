import pandas as pd
import datetime as dt

#UUID,DEPARTAMENTO,PROVINCIA,DISTRITO,METODODX,EDAD,SEXO,FECHA_RESULTADO

df = pd.read_csv("./positivos_covidutf.csv", encoding='latin-1')
states = pd.read_csv("./peru24.csv", encoding='latin-1')
df['FECHA']=pd.to_datetime(df['FECHA_RESULTADO'].astype(str), format='%d/%m/%Y')
df.sort_values(by='FECHA', inplace=True, ascending=True)

#start="2020-03-06"
start = dt.datetime(2020,3, 6)
end = dt.datetime(2020, 6, 7)
#Header
H=[]
H.append("Fecha")
for index,row in states.iterrows():
    dpto=row["Departamento"].upper().strip()
    H.append(dpto)
print(",".join(H))

while start< end:
  L=[]
  L.append("%s"%(start.strftime('%Y-%m-%d')))
  for index,row in states.iterrows():
    dpto=row["Departamento"].upper().strip()
    a=start.strftime('%Y-%m-%d')
    query=df.query('DEPARTAMENTO == "%s" and FECHA=="%s"'%(dpto,a))
    L.append( str( query["FECHA"].shape[0])  )
  print(",".join(L))
  start += dt.timedelta(days=1)
