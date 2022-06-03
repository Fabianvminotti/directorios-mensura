import os   
import csv
from datetime import datetime


#########FUNCIONES#######################
def CreacionCarpetas(dataSet):
        conf= input('desea crear %i carpetas? (SI/NO)' %i)
        if conf == 'SI':
                for fila in dataSet:
                        if os.path.exists(ruta + '/' + fila.replace('\n','') ):    
                                print('La ruta '+ ruta + '/' + fila.replace('\n','') +' Ya existe')
                        else:
                                try:
                                        os.mkdir(ruta + '/' + fila.replace('\n','') )
                                except:
                                        print("Ocurrio un error en la creacion de la carpeta" + fila.replace('\n','') )
                                else:
                                        print('La carpeta '+fila+' fue creada con exito')
        elif conf == 'NO':
                print('programa finalizado')
                return "no"
        else:
                print('Ingresar un SI o NO')
                CreacionCarpetas()


def LeerArchivos():
        with os.scandir(ruta) as ficheros:
                for fichero in ficheros:
                        print(fichero.name)

#######################CODIGO########################                

ruta = os.getcwd()
f = open("numPlanos.csv", "r")
leer = csv.reader(f)
#rutaUser = input('Insertar ruta del directorio donde crear las carpetas')

#########Contador de filas del csv##########
i=0
listaDePlanos = []
for entrada in leer:
        listaDePlanos.append(entrada[0]) 
        i=i+1



#LeerArchivos()
#CreacionCarpetas(listaDePlanos)

################ Leer archivos existentes dentro de una carpeta


