import os
import csv
import sys
from urllib.request import urlopen
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    from urllib2 import urlopen
import datetime
from datetime import datetime


ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
print ('Fecha carga datos precipitaciones Madrid')
print (ahora)

print('Importando precipitaciones desde AEMET')
urlfile = "http://www.aemet.es/es/eltiempo/observacion/ultimosdatos_comunidad-de-madrid_datos-horarios.csv?k=mad&datos=det&w=0&f=temperatura&x=h24"
urllib2.urlretrieve(urlfile,"ficheros\precipitaciones.csv")


name = 'C:\\TFM\\python\\ficheros\\precipitaciones.csv'
file_csv = open(name,'r')   # abre en modo lectura
file_csv2 = 'C:\\TFM\\python\\ficheros\\precipitaciones2.csv'

with file_csv as f:
    with open(file_csv2,'w+') as f1:
        f.__next__()# salta 1 linea
        f.__next__() # salta 1 linea
        f.__next__() # salta 1 linea
        f.__next__()# salta 1 linea
        f.__next__()# salta 1 linea
        #cambio la cabecera del csv
        cabecera='Estacion,Provincia,Temp_C,VelViento_km_h,DireccionViento,Racha_km_h,DireccionRacha,Precipitacion_mm,Presion_hPa,Tendencia_hPa,Humedad_perc'
        f1.write(cabecera)
        f1.write('\n')
        for line in f:
            f1.write(line)
#cierro csv
file_csv.close()
#cierro csv
#file_csv2.close()
print('')
print('Fin importación csv precipitaciones')
print('*************************************')
print('*************************************')





