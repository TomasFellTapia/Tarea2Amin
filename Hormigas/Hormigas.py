import sys
import numpy as np # type: ignore
import pandas as pd # type: ignore
import gc
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
    np.fill_diagonal(mat,1)
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

def prox_nodo(mfer,mheu,i,mmem,beta,q0,n):
    r1=np.random.rand()
    veop = np.zeros(n,float)
    if r1<=q0:
        for j in range (n):
            veop[j] = mfer[i][j]*((mheu[i][j])**beta)*mmem[i][j]
        print(veop)
        auxi= veop.argmax()
       
    else: 
        for j in range (n):
            veop[j] = mfer[i][j]*((mheu[i][j])**beta)*mmem[i][j]
      
       
        veopa = np.cumsum(veop/veop.sum())
        
        r2=np.random.rand()
        for k in range (n):
            auxi = 0
            if r2<veopa[k]:
                auxi = k
                break
        
    return auxi

        


        



if len(sys.argv)== 8:
    sem = int(sys.argv[1])
    nom = str(sys.argv[2])
    colonia = int(sys.argv[3])
    q0 = float(sys.argv[4])
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
    
    soli = np.arange(0,n)
    np.random.shuffle(soli)
    valfer=1/(n*calccost(matdist,soli))
    matfer = np.full((n,n),fill_value=valfer)
    np.fill_diagonal(matfer,0)
  
    soloptd =pd.read_table(optdas, header=None, sep='\\s+', skiprows=4, skipfooter=2, engine='python').transpose().to_numpy() -1
    solot = np.ravel(soloptd,order='F')
    delta=1/calccost(matdist,solot)

    for rep in range (ite) :
        hormi = np.full((colonia,n),fill_value=-1)
        matmem= np.ones((colonia,n),int)
        
        for i in range (colonia):
            hormi[i][0]= np.random.randint(n)
            matmem[i][hormi[i][0]]=0
        for i in range (colonia):
            for j in range (1,n):
                
                hormi[i][j] = prox_nodo(matfer,matheu,hormi[i][j-1],matmem,bet,q0,n)
                matmem[i][hormi[i][j]]=0
            

        

        
    print(hormi)
    
   
   
else :
    print("Error entrada de los parametros")
    print("Los parámetors son: semilla, Nombre del archivo, tamaño población iteraciones, alfa, beta")
    sys.exit(0)
