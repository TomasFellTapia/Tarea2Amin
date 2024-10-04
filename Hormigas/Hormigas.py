import sys
import numpy as np # type: ignore
import pandas as pd # type: ignore
def leerdatos(archivo):
    df = pd.read_table(archivo, header=None, sep='\\s+', skiprows=6, skipfooter=1, engine='python')
    ndf= df.drop(columns=0, axis=1).to_numpy()
    return ndf
def calcdist(datos):
    mat = np.zeros((len(datos),len(datos)),float)
    for i in range(len(datos)):
        for j in range(i+1,len(datos)):
            mat[i][j] = mat[j][i] = np.sqrt((datos[i][0] - datos[j][0])**2 + (datos[i][1] - datos[j][1])**2)
    return mat


if len(sys.argv)== 8:
    sem = int(sys.argv[1])
    nom = str(sys.argv[2])
    colonia = int(sys.argv[3])
    q0 = int(sys.argv[4])
    ite = int(sys.argv[5])
    alf = float(sys.argv[6])
    bet = float(sys.argv[7])
    print(sem, nom,colonia,q0,ite,alf,bet)
    nom="./Datos/"+nom+".tsp.txt"
    
    cordenadas=leerdatos(nom)
    matdist = calcdist(cordenadas)
    print(matdist)

   
else :
    print("Error entrada de los parametros")
    print("Los parámetors son: semilla, Nombre del archivo, tamaño población iteraciones, alfa, beta")
    sys.exit(0)
