#Autor: Wenses J. Penadillo Lazares
#python versión: v3.7.4

from random import randint
from os import system

def index(r,c,n):
    return (r * n) + c

def Print(M,r,c):
    for i in range(r):
        for j in range(c):
                print(M[index(i,j,c)], end="" )
        print("")

E = []

def getEvents():
    system('cls')
    print("")
    n = int(input("Ingrese numero de eventos: "))
    global E
    for i in range (n):
        E.append([])
    print("")
    for i in range (n):
        E[i] = str(input("Ingrese el evento " + str(i + 1) + ": "))
    return E

T = []

def getTimeIntervals():
    system('cls')
    print("")
    n = int(input("Ingrese numero de intervalos por día: "))
    global T
    for i in range (n * 5):
        T.append([])
    print("")
    for i in range(n):
        T[index(i,0,5)] = str(input("Ingrese el intervalo " + str(i + 1) +": "))
    for j in range(1,5):
        for i in range(n):
            T[index(i,j,5)] = T[index(i,0,5)]
    return T

S = []

def getStudents():
    system('cls')
    print("")
    n = int(input("Ingrese numero de estudiantes: "))
    global S
    for i in range (n):
        S.append([])
    s = 0
    f = 0
    print("")
    print("Ingrese numero de alumnos y tipo")
    print("")
    condition = (f != n)
    while condition:
        cant = int(input("Ingrese numero: "))
        tipo = str(input("Ingrese tipo: "))
        print("")
        f = f + cant
        for i in range(s,f):
            S[i] = tipo
        s = s + cant
        condition = (f != n)
    return S

C = []
R = []

def getRooms():
    system('cls')
    print("")
    n = int(input("Ingrese numero de aulas: "))
    global C, R
    for i in range(n):
        C.append([])
        R.append([])
    s = 0
    f = 0
    print("")
    print("Ingrese numero de aluas y capacidad")
    print("")
    condition = (f != n)
    while condition:
        num = int(input("Ingrese numero: "))
        tipo = str(input("Ingrese el tipo: "))
        cap = int(input("Ingrese capacidad: "))
        print("")
        f = f + num
        for i in range(s,f):
            C[i] = cap
            R[i] = tipo
        s = s + num
        condition = (f != n)
    return R

F = []

def getCaracteristics():
    system('cls')
    print("")
    n = int(input("Ingrese el numero de caracteristicas: "))
    print("")
    global F
    for i in range(n):
        F.append([])
    for i in range(len(F)):
        F[i] = str(input("Ingrese caracteristica: "))
    return F

def genP1(S,E):
    B = []
    for i in range(len(E)):
        B.append([])
        B[i] = 0
    P1 = []
    for i in range(len(E) * len(S)):
        P1.append([])
        P1[i] = 0
    selectedS = S[0]
    condition1 = True
    for i in range(len(S)):
        if (S[i] != selectedS):
            condition1 = True
            selectedS = S[i]
        while (condition1):
            system('cls')
            print("")
            print("Eventos:")
            for e in range(len(E)):
                print(str(e + 1)+") "+str(E[e]))
            print("")
            print("Ingrese restricciones")
            print("")
            print("A que evento(s) deben asistir los alumnos de " + str(selectedS) + "? ")
            condition2 = True
            while condition2:
                event = int(input("Elija evento (0 para terminar): "))
                if (event != 0):
                    B[event - 1] = 1
                condition2 = (event != 0)
            for I in range(len(S)):
                if (S[I] == selectedS):
                    for J in range(len(E)):
                        P1[index(I,J,len(E))] = B[J]
                else:
                    continue
            for i in range(len(E)):
                B[i] = 0
            condition1 = False
    return P1

def genP2(R,F):
    B = []
    for i in range(len(F)):
        B.append([])
        B[i] = 0
    P2 = []
    for i in range(len(R) * len(F)):
        P2.append([])
        P2[i] = 0
    selectedR = R[0]
    condition1 = True
    for i in range(len(R)):
        if (R[i] != selectedR):
            condition1 = True
            selectedR = R[i]
        while (condition1):
            system('cls')
            print("")
            print("caracteristicas:")
            for f in range(len(F)):
                print(str(f + 1)+") "+str(F[f]))
            print("")
            print("Ingrese restricciones")
            print("")
            print("Que caracteristica(s) tienen la(s) " + str(selectedR) + "? ")
            condition2 = True
            while condition2:
                caracteristic = int(input("Elija caracteristica (0 para terminar): "))
                if (caracteristic != 0):
                    B[caracteristic - 1] = 1
                condition2 = (caracteristic != 0)
            for I in range(len(R)):
                if (R[I] == selectedR):
                    for J in range(len(F)):
                        P2[index(I,J,len(F))] = B[J]
                else:
                    continue
            for i in range(len(F)):
                B[i] = 0
            condition1 = False
    return P2

def genP3(E,F):
    B = []
    for i in range(len(F)):
        B.append([])
        B[i] = 0
    P3 = []
    for i in range(len(E) * len(F)):
        P3.append([])
        P3[i] = 0
    for i in range(len(E)):
        system('cls')
        print("")
        print("caracteristicas:")
        for f in range(len(F)):
            print(str(f + 1)+") "+str(F[f]))
        print("")
        print("Ingrese restricciones")
        print("")
        print("Que caracteristica(s) requiere el evento " + str(E[i]) + "? ")
        condition = True
        while condition:
            caracteristic = int(input("Elija caracteristica (0 para terminar): "))
            if (caracteristic != 0):
                B[caracteristic - 1] = 1
            condition = (caracteristic != 0)
        for j in range(len(F)):
            P3[index(i,j,len(F))] = B[j]
        for i in range(len(F)):
            B[i] = 0
    return P3

def genP4(E,T):
    B = []
    for i in range(int(len(T)/5)):
        B.append([])
        B[i] = 0
    P4 = []
    for i in range(len(E) * int(len(T)/5)):
        P4.append([])
        P4[i] = 0
    for i in range(len(E)):
        system('cls')
        print("")
        print("Intervalos de tiempo:")
        for t in range(int(len(T)/5)):
            print(str(t + 1)+") "+str(T[index(t,0,5)]))
        print("")
        print("Ingrese restricciones")
        print("")
        print("En que intervalos se puede asignar el evento " + str(E[i]) + "? ")
        condition = True
        while condition:
            interval = int(input("Elija intervalo (0 para terminar): "))
            if (interval != 0):
                B[interval - 1] = 1
            condition = (interval != 0)
        for j in range(int(len(T)/5)):
            P4[index(i,j,int(len(T)/5))] = B[j]
        for I in range(int(len(T)/5)):
            B[I] = 0
    return P4

def genR(P1,P2,P3):
    r = []
    for i in range(len(E) * len(R)):
        r.append([])
        r[i] = 0
    sum = 0
    c1 = 0
    for i in range(len(E)):
        for j in range(len(R)):
            for l in range(len(S)):
                sum = sum + P1[index(l,i,len(E))]
            B1 = (sum <= C[j])
            sum = 0
            for l in range(len(F)):
                if(P3[index(i,l,len(F))] == 1 and P2[index(j,l,len(F))] == 0):
                    c1 = c1 + 1
            B2 = (c1 == 0)
            c1 = 0
            if (B1 and B2):
                r[index(i,j,len(R))] = 1
    return r

def genC(P1,P4,r):
    c = []
    for i in range(len(E) * len(E)):
        c.append([])
        c[i] = 0
    c1 = 0
    c2 = 0
    c3 = 0
    sum1 = 0
    sum2 = 0
    for i in range(len(E)):
        for j in range(len(E)):
            for l in range(len(S)):
                if((P1[index(l,i,len(E))] == 1) and (P1[index(l,j,len(E))] == 1)):
                    c1 = c1 + 1
            B1 = (c1 != 0)
            c1 = 0
            for l in range(len(R)):
                sum1 = sum1 + r[index(i,l,len(R))]
                sum2 = sum2 + r[index(j,l,len(R))]
            for l in range(len(R)):
                if(r[index(i,l,len(R))] == 1 and r[index(j,l,len(R))] == 1 and sum1 == 1 and sum2 == 1):
                    c2 = c2 + 1
            B2 = (c2 != 0)
            c2 = 0
            sum1 = 0
            sum2 = 0
            for l in range(int(len(T)/5)):
                if(P4[index(i,l,int(len(T)/5))] == 1 and P4[index(j,l,int(len(T)/5))] == 1):
                    c3 = c3 + 1
            B3 = (c3 == 0)
            c3 = 0
            if(B1 or B2 or B3):
                c[index(i,j,len(E))] = 1
    for i in range(len(E)):
        for j in range(len(E)):
            if(i == j):
                c[index(i,j,len(E))] = 0
    return c

def PrintHorario(Vertex,P4):
    print("")
    print("--------------------------------------------------------------------------------")
    print("|    H O R A    |         L      U      N      E      S          | M A R T E S |")
    print("|----------------------------------------------------------------|-------------|")
    print("| 08:00 - 10:00 | Cál Avan (P) |                 |               |  Inglés (T) |")
    print("| 10:00 - 12:00 |    POO (P)   | Aná Real II (P) | Física II (P) |             |")
    print("| 14:00 - 16:00 | Cál Avan (T) |                 |               |             |")
    print("| 16:00 - 18:00 |    POO (T)   | Aná Real II (T) | Física II (T) |             |")
    print("--------------------------------------------------------------------------------")
    print("")
    l = input("Enter para salir")
    system('cls')
