import sys
import numpy as np # type: ignore
import pandas as pd # type: ignore
def leerdatos(archivo):
    df = pd.read_table(archivo, header=None, sep='\\s+', skiprows=6, skipfooter=1, engine='python')
    ndf= df.drop(columns=0, axis=1).to_numpy()
    return ndf
def calcdist(datos):
    n = len(datos)
    mat = np.zeros((n,n),float)
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j] = mat[j][i] = np.sqrt((datos[i][0] - datos[j][0])**2 + (datos[i][1] - datos[j][1])**2)
    return mat
def mathuristica(mat):
    heu = np.full_like(mat,fill_value=1/mat,dtype=float)
    np.fill_diagonal(heu,0)
    return heu
def calccost (dist,solin):
    sum=0
    v=len(solin)-1
    c=solin[v]
    d=solin[0]
    for i in range (v):
        a=solin[i]
        b=solin[i+1]
        sum=sum+dist[a][b]
    sum=sum+dist[c][d]
    return sum



        



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
    optdas="./Datos/berlin52.opt.tour.txt"
    np.random.seed(sem)
    cordenadas=leerdatos(nom)
    n=len(cordenadas)
    matdist = calcdist(cordenadas)
    matheu = mathuristica(matdist)
    rep=0
    hormi = np.full((colonia,n),fill_value=-1)
    soli = np.arange(0,n)
    np.random.shuffle(soli)
    while rep<ite:
        for i in range (colonia):
            hormi[i][0]= np.random.randint(n)
    
                

        rep +=1
    
    soloptd =pd.read_table(optdas, header=None, sep='\\s+', skiprows=4, skipfooter=2, engine='python').transpose().to_numpy() -1
    solot = np.ravel(soloptd,order='F')
    
    print(calccost(matdist,solot))
   
   
else :
    print("Error entrada de los parametros")
    print("Los parámetors son: semilla, Nombre del archivo, tamaño población iteraciones, alfa, beta")
    sys.exit(0)
