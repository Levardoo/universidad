import itertools
"""
Una funcion es monotona creciente si f(x) <= f(y) para todo x <= y
"""


#Escribir las funciones monótonas crecientes de P3 en sí mismo.

#Funciones monotonas Pn -> Pn
def funciones_monotonas_crecientes(n):
    Pn = list(range(1, n+1))
    funciones_monotonas = [f for f in itertools.product(Pn, repeat=n) if all(f[i] <= f[i+1] for i in range(n-1))]# Example usage
    return funciones_monotonas

def funciones_monotonas_crecientes_pn_pm(n, m):
    Pn = list(range(1, n + 1))  # CONJUNTO PN
    Pm = list(range(1, m + 1))  # CONJUNTO PM
    
    # Generar todas las tuplas donde f(1) <= f(2) <= ... <= f(n)
    funciones_monotonas = [f for f in itertools.product(Pm, repeat=n) if all(f[i] <= f[i+1] for i in range(n-1))]
    
    return len(funciones_monotonas)

def print_result(res):
    for f in res:
        print(f)

res = funciones_monotonas_crecientes(3)

print(f"Las cantidad de funciones monotonas crecientes para P3 -> P3 es: {len(res)}")
print_result(res)

n = 10
m = 10

res = funciones_monotonas_crecientes_pn_pm(n, m)
print("##########################################################################")
print(f"La cantidad de funciones monotonas crecientes para P{n} -> P{m} es: {res}")