#Autor: Wenses J. Penadillo Lazares
#python versión: v3.7.4

from Horario_util import *

def colorG(Edges):
    EdgeColor = []
    Colors = []
    Color = []
    for i in range(len(E)):
        Colors.append([])
        Colors[i] = i + 1
        Color.append([])
        Color[i] = 0
    Vertex = []
    for i in range(len(E)):
        Vertex.append([])
        Vertex[i] = 0
    for i in range(len(Edges)):
        EdgeColor.append([])
        EdgeColor[i] = 0
    for i in range(len(E)):
        if (Vertex[i] == 0):
            for j in range(len(E)):
                if (Edges[index(i,j,len(E))] == 1):
                    if (EdgeColor[index(i,j,len(E))] != 0):
                        Color[EdgeColor[index(i,j,len(E))] - 1] = 1
            for I in range(len(E)):
                if (Color[I] == 0):
                    Vertex[i] = Colors[I]
                    break
            for z in range(len(E)):
                Color[z] = 0
            for j in range(len(E)):
                if (Edges[index(i,j,len(E))] == 1):
                    if (EdgeColor[index(i,j,len(E))] == 0):
                        EdgeColor[index(i,j,len(E))] = Vertex[i]
                        EdgeColor[index(j,i,len(E))] = Vertex[i]
    return Vertex
