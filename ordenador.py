import csv

from ctypes import c_char, c_char_p
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from scipy.spatial import distance
 
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
    plt.text(float(Pos[i][1])+0.3, float(Pos[i][2])+0.3, Pos[i][0], fontsize=10, color='black')
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
        if(Pos[o][0] != Pos[i][0]):
            #Grafo.add_node(Pos[o][0])
            Grafo.add_edge(Pos[o][0],Pos[i][0])
            Grafo.nodes[Pos[o][0]][str(Pos[i][0])] = distance.euclidean(x,y)
        plt.plot(x,y,color='b',linewidth=0.05)
        print(x) 
        print(y)
        x=[]
        y=[]
print(str(Grafo.nodes(data=True)))
#print(Grafo.edges(data=True))

print(Grafo)


plt.show()