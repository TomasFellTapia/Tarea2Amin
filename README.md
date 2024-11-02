# Tarea 2 Amin
## Algoritmo Colonia de Hormigas 
### Tomás Alejandro Fell Tapia

### Descripcion:
El problema del vendedor viajero consiste en minimisar los costos para visitar una cierta cantidad de nodos, para este se utilizara algoritmos de la colonia de hormigas.
Para que este funcione se debe de ingresar la semilla, el nombre, en este caso solo se debe de ingresar berlin52 ya que el algoritmo concatena la dirección relativa donde se encuentra el archivo de texto y ".tsp.txt", el tamaño la colonia, el q0 que se usara para calculos que requieran probabilidades, el numero de iteraciones y los valores de alfa que representa el factor de evaporacion y beta.
### Funcionamiento: 
Lo primero que se hace es leer los datos contenidos en el txt "berlin50.tsp.txt" y asignar sus datos a una matriz de 52x3, luego de esta se elimina la primera columna, luego se calcula la distancia entre cada nodo (√((X1-X2)^2-(Y1-Y2)^2)) y se asigna a una matriz simetrica de 52X52, para luego calcular la matriz heuristica dividiendo 1 por los datos de la matriz distancia y asignandole 0 a la diagonal.
Se genera una matriz genera una solucion inicial aleatoria, se le calcula el costo y con este de genera una matriz feremona, se toman los datos de la solucion optima asignandolos a una matriz, convirtiendo esa matriz en un vector y se le calcula el costo y como ultimo paso previo se asigna a una variable Booleana el valor falso.
Al iniciar las iteraciones se lleca con el valor "-1" una matriz que representa la colonia de hormigas, se le procede a aignar un valor aleatorio entre 0 y 51 a la posicion inicial de cada hormiga y luego se calculan los nodos a seguir mediante 2 ciclos for aplicando las formulas de calculo de proximo nodo, en el caso de las iteraciones finales se le asigna el menor valor no visitado.
Una vez todas las "hormigas" tienen una ruta se le calcula a cada uno el costo y luego se compara el menor de este con la solucion inicial si este es menor se actualiza la mejor solucion y se actualiza la matriz feromona y si el costo de esta es igual al costo de la solucion optima se cambia el valor de la variable booleana a verdadero y se sale del ciclo for de las iteraciones.