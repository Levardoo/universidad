# Dado un conjunto de números P y una relación de orden R, comprobar si P es un dcpo
import itertools

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

def es_cota_superior(conjunto, relacion, z, D):
    """Verifica si z es una cota superior para el conjunto dirigido D."""
    for x in D:
        if (x, z) not in relacion and x != z:
            return False
    return True

def es_supremo(conjunto, relacion, z, D):
    """Verifica si z es el supremo de un conjunto dirigido D."""
    if not es_cota_superior(conjunto, relacion, z, D):
        return False
    for w in conjunto:
        if es_cota_superior(conjunto, relacion, w, D) and (w, z) in relacion and w != z:
            return False
    return True

def es_dirigido(conjunto, relacion, D):
    """Verifica si un subconjunto D es dirigido."""
    for x in D:
        for y in D:
            if x != y:
                tiene_cota_superior = False
                for z in conjunto:
                    if (x, z) in relacion and (y, z) in relacion:
                        tiene_cota_superior = True
                        break
                if not tiene_cota_superior:
                    return False
    return True

def es_dcpo(conjunto, relacion):
    """Verifica si el conjunto P es un DCPO."""
    # Comprobar que es un orden parcial
    if not es_orden_parcial(conjunto, relacion):
        return False
    
    # Generar todos los subconjuntos posibles de P y comprobar si son dirigidos
    for r in range(1, len(conjunto)+1):
        subconjuntos = itertools.combinations(conjunto, r)
        for D in subconjuntos:
            if es_dirigido(conjunto, relacion, D):
                # Verificar si existe un supremo
                supremo_encontrado = False
                for z in conjunto:
                    if es_supremo(conjunto, relacion, z, D):
                        supremo_encontrado = True
                        break
                if not supremo_encontrado:
                    return False
    return True

# Solicitar el conjunto de elementos
P = input("Introduce el conjunto de elementos separados por comas: ").split(",")
P = [int(x.strip()) for x in P]  # Convertir a enteros o dejar en forma de caracteres si es necesario

# Solicitar las relaciones en forma de pares
R = []
print("Introduce las relaciones en forma de pares (por ejemplo: 1,2). Introduce 'fin' para terminar:")
while True:
    par = input("Introduce un par (o 'fin' para terminar): ")
    if par.lower() == 'fin':
        break
    x, y = par.split(",")
    R.append((int(x.strip()), int(y.strip())))

# Verificar si P es un dcpo
if es_dcpo(P, R):
    print("El conjunto P con la relación R es un DCPO.")
else:
    print("El conjunto P con la relación R NO es un DCPO.")
