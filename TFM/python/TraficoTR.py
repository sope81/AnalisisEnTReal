from pymongo import MongoClient
import datetime
import xml.etree.ElementTree as ET
from datetime import datetime

#valor fecha para la carga

ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
print ('Fecha carga datos tráfico Madrid')
print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#creo un cliente de mongo
client = MongoClient()
client = MongoClient('localhost', 27017)
print("***************************************************")
print(client)
#asigno bd
db = client['TFM']
print("***************************************************")
print(db)


from lxml import etree
from urllib.request import urlopen
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
    from urllib2 import urlopen

#conversor códigos a su tipo correcto
def num(s):
    try:
        return int(s)
    except ValueError:
        return s
    
print( 'Tratar fichero xml')
root = etree.parse(urlopen('http://informo.munimadrid.es/informo/tmadrid/pm.xml'))
###events = []



print("***************************************************")
print("inserción lineas")

result2 = db.trafico.remove()
for event in root.xpath('.//pm'):
    #gestiono campos nulos del xml
    
    cod=num(event.find('codigo').text)
    if event.find('descripcion') is not None:
        desc=event.find('descripcion').text
        AccA=event.find('accesoAsociado').text
        intsat=int(event.find('intensidadSat').text)
        suba=int(event.find( 'subarea' ).text)
    else:desc=''
    AccA=0
    intsat=0
    suba=0

    #obtengo datos asociados de los puntos de medición como Lat y Long
    query=db.puntos_medida.find({'identif' : cod}, {"_id" :0,"tipo_elem" : 1,"identif" : 1,"longitude" : 1,"latitude" : 1})
    if query is not None:
        for x in query:
            tipo_elem=(x["tipo_elem"])
            lng=(x["longitude"])
            lat=(x["latitude"])
            #print(x["tipo_elem"])
            
    else:
        tipo_elem=''
        lng=0
        lat=0
        #print('sin correspondencia')
    
    event = {'codigo' : cod ,
            'descripcion' : desc,
            'accesoAsociado' : AccA,
            'intensidad' : int(event.find( 'intensidad' ).text),
            'ocupacion' : int(event.find('ocupacion').text),
            'carga' : int(event.find('carga').text),
            'nivelServicio' : event.find('nivelServicio').text,
            'intensidadSat' : intsat,
            'error' : event.find( 'error' ).text,
            'subarea' : suba,
            'tipo_elem' :tipo_elem,
            'coordenadas':{'lng':lng,
                            'lat':lat},
            'loaddata' : ahora}
    result = db.trafico.insert(event)
   
   ### events.append(event)


print('fin carga trafico');
print('*************************************')
print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print('*************************************')
