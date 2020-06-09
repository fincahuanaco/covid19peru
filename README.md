# Bubbles covid19 - Perú
Visualization of the growth of infected by covid-19 (Python with maps )

<!--![Demo](perujunio.gif|width=600)-->
<img src="perujunio.gif" alt="Demo" width="600px"/>


#How to execute
You need to get positivos_covidutf.csv from https://covid19.minsa.gob.pe/sala_situacional.asp

$python3 maketimeserie.py > peru24series.csv
$python3 drawperuseries.py 2020-03-20 out.png

or

$sh runperu.sh 

for create the complete images animation
