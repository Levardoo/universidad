from itertools import product

conjunto_origen = ["a", "b", "c"]

conjunto_destino = ["a","b","c"]

def es_monotona_creciente1(asignacion):
      return (asignacion[0] <= asignacion[1] and  # f(a) <= f(b)
            asignacion[0] <= asignacion[2])     # f(a) <= f(c)


def es_monotona_creciente2(asignacion):
      return (asignacion[0] <= asignacion[1] and  # f(a) <= f(b)
            asignacion[0] <= asignacion[2] and  
            asignacion[1] <= asignacion[3] and
            asignacion[2] <= asignacion[3])      # f(a) <= f(c)

all_functions = list(product(conjunto_destino, repeat=len(conjunto_origen)))
monotonic_functions = [f for f in all_functions if es_monotona_creciente1(f)]

for funcion in monotonic_functions:
    print(f"f(a) = {funcion[0]}, f(b) = {funcion[1]}, f(c) = {funcion[2]}")

conjunto_origen = ["a", "b", "c", "d"]
conjunto_destino = ["a", "b", "c", "d"]
all_functions2 = list(product(conjunto_destino, repeat=len(conjunto_origen)))
monotonic_functions2 = [f for f in all_functions2 if es_monotona_creciente2(f)]

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for funcion in monotonic_functions2:
    print(f"f(a) = {funcion[0]}, f(b) = {funcion[1]}, f(c) = {funcion[2]}, f(d) = {funcion[3]}")
