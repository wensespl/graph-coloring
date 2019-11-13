from Horario_util import *
from Horario_color import *
from os import system

#Obtenemos la informacion del usuario
E = getEvents()
T = getTimeIntervals()
S = getStudents()
R = getRooms()
F = getCaracteristics()
#Preguntamos por las restricciones y generamos P1 P2 P3 P4
P1 = genP1(S,E)
P2 = genP2(R,F)
P3 = genP3(E,F)
P4 = genP4(E,T)
system('cls')     #limpiando la pantalla
#generamos r y c
r = genR(P1,P2,P3)
c = genC(P1,P4,r)         #finalmente c sera la matriz de adyacencia
print("")      #salto de linea
print("Matriz de Adyacencia")
print("")      #salto de linea
Print(c,len(E),len(E))    #La imprimimos para visualizarla
#Procedemos con la coloracion de los vertices del grafo
Vertex = colorG(c)        #Obtenemos los vertices coloreados
print("")      #salto de linea
print("Vertices coloreados")
print("")      #salto de linea
for i in range(len(Vertex)):
    print(Vertex[i], end=" ")
print("")      #salto de linea
print("Con los vertices ya coloreados procedemos a generar el horario")
print("")      #salto de linea
l = input("Enter para continuar")
system('cls')
#Procedemos a imprimir el Horario
PrintHorario(Vertex,P4)
