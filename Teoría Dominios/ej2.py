import itertools

def es_reflexiva(relacion, conjunto):
    """Verifica si la relación es reflexiva."""
    for x in conjunto:
        if (x, x) not in relacion:
            return False
    return True

def es_antisimetrica(relacion):
    """Verifica si la relación es antisimétrica."""
    for (x, y) in relacion:
        if (x != y) and ((y, x) in relacion):
            return False
    return True

def es_transitiva(relacion):
    """Verifica si la relación es transitiva."""
    for (x, y) in relacion:
        for (y2, z) in relacion:
            if y == y2 and (x, z) not in relacion:
                return False
    return True

def es_orden_parcial(relacion, conjunto):
    """Verifica si la relación es un orden parcial."""
    return es_reflexiva(relacion, conjunto) and es_antisimetrica(relacion) and es_transitiva(relacion)

def obtener_ordenes_parciales(conjunto):
    """Genera todos los posibles órdenes parciales de un conjunto."""
    pares = list(itertools.product(conjunto, repeat=2))
    ordenes_parciales = []
    
    # Genera todos los subconjuntos posibles de pares
    for subrelacion in itertools.chain.from_iterable(itertools.combinations(pares, r) for r in range(len(pares)+1)):
        if es_orden_parcial(subrelacion, conjunto):
            ordenes_parciales.append(subrelacion)
    
    return ordenes_parciales

# Conjuntos con 3 y 4 elementos
conjunto_3 = {1, 2, 3}
conjunto_4 = {1, 2, 3, 4}

# Obtener todos los órdenes parciales
ordenes_parciales_3 = obtener_ordenes_parciales(conjunto_3)
ordenes_parciales_4 = obtener_ordenes_parciales(conjunto_4)

# Imprimir resultados
print(f"Órdenes parciales para el conjunto {conjunto_3}:")
for orden in ordenes_parciales_3:
    print(orden)

print(f"\nÓrdenes parciales para el conjunto {conjunto_4}:")
for orden in ordenes_parciales_4:
    print(orden)
