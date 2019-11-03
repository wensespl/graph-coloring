from sudoku_color import *
from sys import setrecursionlimit

print("")
print("Continuemos con la solucion")
print("")
print("Pegar aqui!!   (enter para continuar)")
print("")
setrecursionlimit(100)
read_puzzle()
print("")
print("Resolviendo....")
print("")
for soln in color_puzzle(None, False):
    print_solution(soln)
    print("")
