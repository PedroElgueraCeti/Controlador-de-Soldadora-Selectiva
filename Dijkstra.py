
#Grado
grafo = {'a':{'b':2,'f':3}, 'b':{'c':2,'d':2,'e':4}, 'c':{'e':3,'z':1}, 'd':{'e':4}, 'e':{'g':7}, 'f':{'d':3,'g':5}, 'g':{'z':6}, 'z':{}}

def dijkstra(graph,inicio,fin):
    distacia_mascorta = {} # Guarda la distancia para el nodo. 
    predecesor = {}  #Guarda el camino seguido.
    nodosRestantes = graph #Itera el grafo.
    infinito = 9999999 #Numero grande comparado con los pesos.
    path = [] #Camino al nodo de inicio
    for nodo in nodosRestantes:
        distacia_mascorta[nodo] = infinito
    distacia_mascorta[inicio] = 0
    while nodosRestantes:
        minNodo = None
        for nodo in nodosRestantes:
            if minNodo is None:
                minNodo = nodo
            elif distacia_mascorta[nodo] < distacia_mascorta[minNodo]:
                minNodo = nodo
        """"Distancia ya terminada. 
        Eleccion de caminos"""
        for siguiente, weight in graph[minNodo].items():
            if weight + distacia_mascorta[minNodo] < distacia_mascorta[siguiente]:
                distacia_mascorta[siguiente] = weight + distacia_mascorta[minNodo]
                predecesor[siguiente] = minNodo #Guarda el camino que se ha tomado hasta el nodo actual
        nodosRestantes.pop(minNodo)
    nodoActual = fin
    while nodoActual != inicio:
        try:
            path.insert(0,nodoActual)
            nodoActual = predecesor[nodoActual]
        except KeyError:
            print('Camino no alcanzable')
            break
    path.insert(0,inicio)
    if distacia_mascorta[fin] != infinito:
        #print('El camino mas corto es ' + str(path))
        for indice in range(len(path)-1):
            caracterI=path[indice]
            caracterD=path[indice+1]
            print("[",caracterI,",",caracterD,"]")
        print('La distancia mas corta de [' + str.upper(inicio) + "] a [" + str.upper(fin) + "] es =" + str(distacia_mascorta[fin]))

dijkstra(grafo, 'a', 'z')