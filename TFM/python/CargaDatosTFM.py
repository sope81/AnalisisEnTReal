#carga datos en tiempo real TFM
import sys
sys.path.insert(0, 'C:\TFM\python')
import pymongo
from pymongo import MongoClient
import datetime
from datetime import datetime
import webbrowser
#LLAMADA A LOS PAQUETES DE CARGA
import Precipitaciones
import TraficoTR
import ContaminacionTR





ahora = datetime.now().strftime("%Y-%m-%d %H:%M")
#como los datos de contaminación se actulizan cada hora entre los minutos 20 a 30,
#podremos un controlador si estamos a menos de 35 m, veo la hora anterior.

minutos=int(datetime.now().strftime("%M"))
if minutos<35:
    hora=str(int(datetime.now().strftime("%H"))-1)
else:
    hora=datetime.now().strftime("%H")
print ('Fecha carga datos contaminacion Madrid')
print (ahora)
print('Se mostrara la siguiente hora: '+hora)

#arranco mongodb

#creo un cliente de mongo
client = MongoClient()
client = MongoClient('localhost', 27017)
print("***************************************************")
print(client)
#asigno bd
db = client['TFM']
print("***************************************************")
print(db)



print("Carga datos bicis Madrid")
result = db.estacionesMad.remove()
webbrowser.open('http://localhost:3000/cargabicis')



from datetime import datetime
print("***************************************************")
print("ACTUALIZACIÓN DATOS CONTAMINACION MADRID")
result = db.contaminacion.update_many({'ESTACION':28079035},{'$set':{"EST_NAME":"Pza. del Carmen","Alt":657,"coordenadas":{"lat":40.41921,"lng":-3.70317}}})
db.contaminacion.save
result = db.contaminacion.update_many({'ESTACION':28079004},{'$set':{'EST_NAME':'Pza. de España  ','Alt':637,'coordenadas':{'lat':40.42399,'lng':-3.71233}}})
result = db.contaminacion.update_many({'ESTACION':28079039},{'$set':{'EST_NAME':'Barrio del Pilar','Alt':673,'coordenadas':{'lat':40.47823,'lng':-3.71154}}})
result = db.contaminacion.update_many({'ESTACION':28079008},{'$set':{'EST_NAME':'Escuelas Aguirre','Alt':672,'coordenadas':{'lat':40.42156,'lng':-3.68232}}})
result = db.contaminacion.update_many({'ESTACION':28079038},{'$set':{'EST_NAME':'Cuatro Caminos','Alt':699,'coordenadas':{'lat':40.44554,'lng':-3.70713}}})
result = db.contaminacion.update_many({'ESTACION':28079011},{'$set':{'EST_NAME':'Av. Ramón y Cajal ','Alt':708,'coordenadas':{'lat':40.45147,'lng':-3.67735}}})
result = db.contaminacion.update_many({'ESTACION':28079040},{'$set':{'EST_NAME':'Vallecas','Alt':677,'coordenadas':{'lat':40.38815,'lng':-3.65152}}})
result = db.contaminacion.update_many({'ESTACION':28079016},{'$set':{'EST_NAME':'Arturo Soria','Alt':698,'coordenadas':{'lat':40.44005,'lng':-3.63923}}})
result = db.contaminacion.update_many({'ESTACION':28079017},{'$set':{'EST_NAME':'Villaverde Alto','Alt':601,'coordenadas':{'lat':40.34710,'lng':-3.71333}}})
result = db.contaminacion.update_many({'ESTACION':28079018},{'$set':{'EST_NAME':'C/ Farolillo','Alt':581,'coordenadas':{'lat':40.39478,'lng':-3.73183}}})
result = db.contaminacion.update_many({'ESTACION':28079036},{'$set':{'EST_NAME':'Moratalaz','Alt':671,'coordenadas':{'lat':40.40796,'lng':-3.64529}}})
result = db.contaminacion.update_many({'ESTACION':28079024},{'$set':{'EST_NAME':'Casa de Campo  ','Alt':645,'coordenadas':{'lat':40.41936,'lng':-3.74734}}})
result = db.contaminacion.update_many({'ESTACION':28079027},{'$set':{'EST_NAME':'Barajas ','Alt':631,'coordenadas':{'lat':40.47693,'lng':-3.58003}}})
result = db.contaminacion.update_many({'ESTACION':28079047},{'$set':{'EST_NAME':'Méndez Álvaro','Alt':609,'coordenadas':{'lat':40.39806,'lng':-3.68667}}})
result = db.contaminacion.update_many({'ESTACION':28079048},{'$set':{'EST_NAME':'Pº. Castellana','Alt':676,'coordenadas':{'lat':40.43972,'lng':-3.69028}}})
result = db.contaminacion.update_many({'ESTACION':28079049},{'$set':{'EST_NAME':'Retiro','Alt':662,'coordenadas':{'lat':40.41444,'lng':-3.68250}}})
result = db.contaminacion.update_many({'ESTACION':28079050},{'$set':{'EST_NAME':'Pza. Castilla','Alt':728,'coordenadas':{'lat':40.46556,'lng':-3.68861}}})
result = db.contaminacion.update_many({'ESTACION':28079054},{'$set':{'EST_NAME':'Ensanche Vallecas','Alt':630,'coordenadas':{'lat':40.37278,'lng':-3.61194}}})
result = db.contaminacion.update_many({'ESTACION':28079055},{'$set':{'EST_NAME':'Urb. Embajada (Barajas)','Alt':619,'coordenadas':{'lat':40.46250,'lng':-3.58056}}})
result = db.contaminacion.update_many({'ESTACION':28079056},{'$set':{'EST_NAME':'Pza. Fdez. Ladreda','Alt':605,'coordenadas':{'lat':40.38472,'lng':-3.71861}}})
result = db.contaminacion.update_many({'ESTACION':28079057},{'$set':{'EST_NAME':'Sanchinarro','Alt':700,'coordenadas':{'lat':40.49419,'lng':-3.66050}}})
result = db.contaminacion.update_many({'ESTACION':28079058},{'$set':{'EST_NAME':'El Pardo','Alt':616,'coordenadas':{'lat':40.51806,'lng':-3.77461}}})
result = db.contaminacion.update_many({'ESTACION':28079059},{'$set':{'EST_NAME':'Parque Juan Carlos I','Alt':669,'coordenadas':{'lat':40.46500,'lng':-3.60889}}})
result = db.contaminacion.update_many({'ESTACION':28079060},{'$set':{'EST_NAME':'Tres Olivos','Alt':715,'coordenadas':{'lat':40.50056,'lng':-3.68972}}})
#Actualizo datos de magnitudes DE ANALISIS DE CONTAMINACION
result = db.contaminacion.update_many({'MAGNITUD':1},{'$set':{'MAGNITUD':'Dióxido de Azufre','MAG_ABV':'SO2'}})
result = db.contaminacion.update_many({'MAGNITUD':6},{'$set':{'MAGNITUD':'Monóxido de Carbono','MAG_ABV':'CO'}})
result = db.contaminacion.update_many({'MAGNITUD':7},{'$set':{'MAGNITUD':'Monóxido de Nitrógeno','MAG_ABV':'NO'}})
result = db.contaminacion.update_many({'MAGNITUD':8},{'$set':{'MAGNITUD':'Dióxido de Nitrógeno','MAG_ABV':'NO2'}})
result = db.contaminacion.update_many({'MAGNITUD':9},{'$set':{'MAGNITUD':'Partículas<2.5 µm','MAG_ABV':'PM2.5'}})
result = db.contaminacion.update_many({'MAGNITUD':10},{'$set':{'MAGNITUD':'Partículas < 10 µm','MAG_ABV':'PM10'}})
result = db.contaminacion.update_many({'MAGNITUD':12},{'$set':{'MAGNITUD':'Óxidos de Nitrógeno','MAG_ABV':'NOx'}})
result = db.contaminacion.update_many({'MAGNITUD':14},{'$set':{'MAGNITUD':'Ozono','MAG_ABV':'O3'}})
result = db.contaminacion.update_many({'MAGNITUD':20},{'$set':{'MAGNITUD':'Tolueno','MAG_ABV':'TOL'}})
result = db.contaminacion.update_many({'MAGNITUD':30},{'$set':{'MAGNITUD':'Benceno','MAG_ABV':'BEN'}})
result = db.contaminacion.update_many({'MAGNITUD':35},{'$set':{'MAGNITUD':'Etilbenceno','MAG_ABV':'EBE'}})
result = db.contaminacion.update_many({'MAGNITUD':37},{'$set':{'MAGNITUD':'Metaxileno','MAG_ABV':'MXY'}})
result = db.contaminacion.update_many({'MAGNITUD':38},{'$set':{'MAGNITUD':'Paraxileno','MAG_ABV':'PXY'}})
result = db.contaminacion.update_many({'MAGNITUD':39},{'$set':{'MAGNITUD':'Ortoxileno','MAG_ABV':'OXY'}})
result = db.contaminacion.update_many({'MAGNITUD':42},{'$set':{'MAGNITUD':'Hidrocarburos totales(hexano)','MAG_ABV':'TCH'}})
result = db.contaminacion.update_many({'MAGNITUD':44},{'$set':{'MAGNITUD':'Hidrocarburos no metánicos (hexano)','MAG_ABV':'NMHC'}})

#ACTUALIZO LAS TECNICAS DE ANALISIS DE CONTAMINACION
result = db.contaminacion.update_many({'TECNICA':38},{'$set':{'TECNICA':'Fluorescencia ultravioleta'}})
result = db.contaminacion.update_many({'TECNICA':48},{'$set':{'TECNICA':'Absorción infrarroja'}})
result = db.contaminacion.update_many({'TECNICA':8},{'$set':{'TECNICA':'Quimioluminiscencia'}})
result = db.contaminacion.update_many({'TECNICA':47},{'$set':{'TECNICA':'Microbalanza'}})
result = db.contaminacion.update_many({'TECNICA':47},{'$set':{'TECNICA':'Id.'}})
result = db.contaminacion.update_many({'TECNICA':8},{'$set':{'TECNICA':'Quimioluminiscencia'}})
result = db.contaminacion.update_many({'TECNICA':6},{'$set':{'TECNICA':'Absorción ultravioleta'}})
result = db.contaminacion.update_many({'TECNICA':59},{'$set':{'TECNICA':'Cromatografía de gases'}})
result = db.contaminacion.update_many({'TECNICA':2},{'$set':{'TECNICA':'Ionización de llama'}})
#actualizo el campo de la hora actual
result = db.contaminacion.update_many({},{'$rename': { 'HORA'+hora: 'HORA'}})
db.contaminacion.save


       
       
       
       
