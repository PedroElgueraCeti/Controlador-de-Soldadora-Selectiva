import csv
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
 
Grafo = nx.Graph() # crear un grafo
Pos = [] # arreglo original con todas las coordenadas

with open('t1.csv') as csvfile:
    Posi = []
    reader = csv.DictReader(csvfile)
    for row in reader:
         #print(row['punto'],row['x'], row['y'])
         Posi=(row['punto'],row['x'], row['y'])
         Pos.append(Posi)

filas=len(Pos)
plt.title("Mapa de coordenadas",fontsize=15)
#trazar puntos
for i in range(len(Pos)):
    plt.plot(float(Pos[i][1]),float(Pos[i][2]),marker="*", color="red")
#Trazar rectas
x=[]
y=[]

#for o in range(len(Pos)):
    

for o in range(len(Pos)):
    for i in range(len(Pos)):
        x.append(float(Pos[o][1]))
        y.append(float(Pos[o][2]))
        x.append(float(Pos[i][1]))
        y.append(float(Pos[i][2]))
        Grafo.add_node(Pos[o][0])
        Grafo.add_edge(Pos[o][0],Pos[i][0])
        plt.plot(x,y,color='b',linewidth=0.05)
        print(x)
        print(y)
        x=[]
        y=[]
print(Grafo.nodes)
print(Grafo.edges)
#trazador de rectas
#for i in range(len(Pos)):
    

plt.show()