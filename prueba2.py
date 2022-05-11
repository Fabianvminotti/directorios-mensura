import os   
import csv
from datetime import datetime


#########FUNCIONES#######################
def CreacionCarpetas():
        conf= input('desea crear %i carpetas? (SI/NO)' %i)
        print(conf)
        if conf == 'SI':
                for fila in f:
                        if os.path.exists(ruta + '/' + fila.replace('\n','') ):    
                                print('La ruta '+ ruta + '/' + fila.replace('\n','') +' Ya existe')
                        else:
                                try:
                                        os.mkdir(ruta + '/' + fila.replace('\n','') )
                                except:
                                        print("Ocurrio un error en la creacion de la carpeta" + fila.replace('\n','') )
                                else:
                                        os.mkdir(ruta + '/' + fila.replace('\n','') )
        elif conf == 'NO':
                print('programa finalizado')
        else:
                print('Ingresar un SI o NO')
                CreacionCarpetas()

#######################CODIGO########################                

ruta = os.getcwd()
f = open("csvprueba.csv", "r")

#rutaUser = input('Insertar ruta del directorio donde crear las carpetas')

#########Contador de filas del csv##########
i=0
for entrada in f:
        i=i+1

CreacionCarpetas()
