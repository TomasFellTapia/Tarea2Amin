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

def prox_nodo(mfer,mheu,i,mmem,beta,q0,n,hormi):
    r1=np.random.rand()
    
    veop = np.ones(n,float)
    
    for j in range (n):
            veop[j] = mfer[i][j]*((mheu[i][j])**beta)*mmem[i][j]

    
    if r1<=q0:
     
        auxi=np.random.choice(np.where(veop ==veop.max())[0])
        return auxi
       
    else: 
        total = veop.sum() 
        if total !=0:
       
            veopa = np.cumsum(veop/total)
                
            r2=np.random.rand()
            
            for k in range (n):
                if r2 <= veopa[k]:
                    auxi = k
                    return auxi
        else:
            for w in range (n):
                if w not in hormi:
                    return w

       
            
    

        


        



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
    cosoli = calccost(matdist,soli)
    mejorhormi = cosoli.copy()
    mejsol = cosoli
    valfer=1/(n*cosoli)
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
        for j in range (1,n):
            for k in range (colonia):
                hormi[k][j] = prox_nodo(matfer,matheu,k,matmem,bet,q0,n,hormi[k])
                matmem[k][hormi[k][j]]=0
               
                matfer[hormi[k][j-1]][hormi[k][j]] = matfer[hormi[k][j]][hormi[k][j-1]] = (1-alf)*matfer[hormi[k][j-1]][hormi[k][j]] + valfer*alf
        
        vectcost = np.zeros(colonia,float)
        for z in range (colonia):
            vectcost[z]=calccost(matdist,hormi[z])
        minlocal = np.min(vectcost)
        if minlocal < mejsol:
            mejsol = minlocal
            posi= np.random.choice(np.where(vectcost ==vectcost.min())[0])
            mejorhormi== hormi[posi].copy()
            gen= rep + 1
            for u in range (n-1):
                for j in range(i+1,n):
                    matfer[i][j] = (1-alf)*matfer[i][j]
                    matfer[j][1] = matfer[i][j]
            


   
    
        

        
    
    
   
   
else :
    print("Error entrada de los parametros")
    print("Los parámetors son: semilla, Nombre del archivo, tamaño población iteraciones, alfa, beta")
    sys.exit(0)
