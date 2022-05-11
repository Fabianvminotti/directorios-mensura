import os   
import csv
from datetime import datetime


ruta = os.getcwd()


f = open("csvprueba.csv", "r")


ruta = os.getcwd()

for fila in f:
    nombreCarpeta =  fila.replace('\n','')
    if os.path.exists(ruta + '/' + nombreCarpeta ):    
            print('La ruta '+ ruta + '/' + nombreCarpeta +' Ya existe')
    else:
            os.mkdir(ruta + '/' + nombreCarpeta )

