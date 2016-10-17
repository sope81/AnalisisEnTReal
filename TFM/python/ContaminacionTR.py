import os
import csv
import sys
from pymongo import MongoClient
import datetime
from datetime import datetime
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

#valor fecha para la carga

ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
print ('Fecha carga datos contaminacion Madrid')
print (ahora)



#el fichero a cargar
path = 'http://www.mambiente.munimadrid.es/opendata/horario.txt'
#creo un fichero csv para bajar el fichero

print('Bajando fichero contaminación') 
name = 'C:\\TFM\\python\\ficheros\\contaminacion.csv'
file_csv = open(name,'w+')   # Recrea el fichero cada vez
#cabecera csv
cabecera='ESTACION,MAGNITUD,TECNICA,HORARIO,ANIO,MES,DIA,HORA1,HORA2,HORA3,HORA4,HORA5,HORA6,HORA7,HORA8,HORA9,HORA10,HORA11,HORA12,HORA13,HORA14,HORA15,HORA16,HORA17,HORA18,HORA19,HORA20,HORA21,HORA22,HORA23,HORA24'
file_csv.write(cabecera)
file_csv.write('\n')

#preparo el fichero

print('Preparo fichero')
data = urllib2.urlopen(path) # abro el fichero a cargar
for line in data: # inserto en el csv
    line_csv=str(line,'utf-8')
    line_csv=line_csv.replace(',N','')
    line_csv=line_csv.replace(',V','')
    line_csv=line_csv.replace(',','',2)
    file_csv.write(line_csv)
    #file.write('\n')


#cierro csv
file_csv.close()

print('cargo el fichero en mongo')
from subprocess import Popen
p = Popen("bulk_csv_cont.bat")#, cwd=r"c:\TFM")
#p = Popen("C:\TFM\python\ficheros\bulk_csv_cont.bat")
print('Volcado ficheros csv')
print('Fin carga contaminación Madrid')
print('*************************************')
print('*************************************')


