import itertools

def es_dirigido(conjunto, relacion, D):
    # Implement the logic to check if D is directed
    for x in D:
        for y in D:
            if x != y:
                if not any((x, z) in relacion and (y, z) in relacion for z in conjunto):
                    return False
    return True

def es_supremo(conjunto, relacion, z, D):
    # Implement the logic to check if z is a supremum for D
    for x in D:
        if not (x == z or (x, z) in relacion):
            return False
    return True

def es_dcpo(conjunto, relacion):
    # Generate all possible subsets of P and check if they are directed
    for r in range(1, len(conjunto)+1):
        subconjuntos = itertools.combinations(conjunto, r)
        for D in subconjuntos:
            if es_dirigido(conjunto, relacion, D):
                # Check if there is a supremum
                supremo_encontrado = False
                for z in conjunto:
                    if es_supremo(conjunto, relacion, z, D):
                        supremo_encontrado = True
                        break
                if not supremo_encontrado:
                    return False
    return True

# Request the set of elements
P = input("Introduce el conjunto de elementos separados por comas: ").split(",")
P = [int(x.strip()) for x in P]  # Convert to integers or leave as characters if necessary

# Request the relations in pairs
R = []
print("Introduce las relaciones en forma de pares (por ejemplo: 1,2). Introduce 'fin' para terminar:")
while True:
    par = input("Introduce un par (o 'fin' para terminar): ")
    if par.lower() == 'fin':
        break
    x, y = par.split(",")
    R.append((int(x.strip()), int(y.strip())))

# Verify if P is a dcpo
if es_dcpo(P, R):
    print("El conjunto P con la relación R es un DCPO.")
else:
    print("El conjunto P con la relación R NO es un DCPO.")
