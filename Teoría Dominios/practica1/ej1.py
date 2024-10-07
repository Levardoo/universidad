def es_reflexiva(conjunto, relacion):
    """Verifica si la relación es reflexiva."""
    for x in conjunto:
        if (x, x) not in relacion:
            return False
    return True

def es_antisimetrica(relacion):
    """Verifica si la relación es antisimétrica."""
    for (x, y) in relacion:
        if x != y and (y, x) in relacion:
            return False
    return True

def es_transitiva(relacion):
    """Verifica si la relación es transitiva."""
    for (x, y) in relacion:
        for (y2, z) in relacion:
            if y == y2 and (x, z) not in relacion:
                return False
    return True

def es_orden_parcial(conjunto, relacion):
    """Verifica si la relación es un orden parcial."""
    return es_reflexiva(conjunto, relacion) and es_antisimetrica(relacion) and es_transitiva(relacion)







# Solicitar el conjunto de elementos
P = input("Introduce el conjunto de elementos separados por comas: ").split(",")

# Eliminar espacios innecesarios
P = [x.strip() for x in P]

# Solicitar las relaciones en forma de pares


R = []
print("Introduce las relaciones en forma de pares (por ejemplo: a,b). Introduce 'fin' para terminar:")
while True:
    par = input("Introduce un par (o 'fin' para terminar): ")
    if par.lower() == 'fin':
        break
    x, y = par.split(",")
    R.append((x.strip(), y.strip()))

# Verificar si la relación es un orden parcial
if es_orden_parcial(P, R):
    print("La relación es un orden parcial.")
else:
    print("La relación NO es un orden parcial.")
