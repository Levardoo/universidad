import itertools

# Función para verificar si una función es monótona creciente
def es_monotona_creciente(funcion):
    for i in range(len(funcion) - 1):
        if funcion[i] > funcion[i + 1]:
            return False
    return True

# Función para generar todas las funciones monótonas crecientes de Pn a Pm
def funciones_monotonas_crecientes(n, m):
    P_m = list(range(1, m + 1))  # Genera P_m = {1, 2, ..., m}
    
    # Genera todas las funciones posibles de P_n a P_m (permutaciones con repetición)
    todas_funciones = itertools.product(P_m, repeat=n)
    
    # Filtra solo las funciones que son monótonas crecientes
    funciones_crecientes = [funcion for funcion in todas_funciones if es_monotona_creciente(funcion)]
    
    return funciones_crecientes

# Función para contar el número de funciones monótonas crecientes
def contar_funciones_monotonas_crecientes(n, m):
    funciones_crecientes = funciones_monotonas_crecientes(n, m)
    return len(funciones_crecientes)

# Ejemplo para P3 -> P3
n = 3
m = 3

# Lista de funciones monótonas crecientes de P3 a P3
funciones = funciones_monotonas_crecientes(n, m)

print(f"Funciones monótonas crecientes de P{n} a P{m}:")
for f in funciones:
    print(f)

# Contar el número de funciones monótonas crecientes
num_funciones = contar_funciones_monotonas_crecientes(n, m)
print(f"Número de funciones monótonas crecientes de P{n} a P{m}: {num_funciones}")
