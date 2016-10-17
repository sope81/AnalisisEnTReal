import sys
import datetime
from datetime import datetime
import time
import sys
sys.path.insert(0, 'C:\TFM\python')

#Arrancamos servicios necesarios
from subprocess import Popen
    p = Popen("ArrancarServiciosMongo.bat", cwd=r"c:\TFM")
    p2 = Popen("ArrancarServiciosNode.bat", cwd=r"c:\TFM")

i=0
while True: #Infinite loop
    i=i+1
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('inicio bucle numero:')
    print(i)
    print(ahora) #imprime fecha
    #lanza la carga general
    import CargaDatosTFM
    time.sleep(600) #espera 10 minutos
