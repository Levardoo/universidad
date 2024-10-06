def es_subconjunto_dirigido(P, R, A):
    # Comprobamos si A es un subconjunto de P
    if not A.issubset(P):
        return False, "A no es un subconjunto de P"
    
    # Convertimos R en un diccionario para mejorar eficiencia en la búsqueda de sucesores
    sucesores = {p: set() for p in P}
    for (x, y) in R:
        sucesores[x].add(y)

    # Verificamos la propiedad de subconjunto dirigido
    for a in A:
        for b in A:
            if a != b:
                # Necesitamos encontrar un c en A tal que a R c y b R c
                existe_c = False
                for c in A:
                    if c in sucesores[a] and c in sucesores[b]:
                        existe_c = True
                        break
                if not existe_c:
                    return False, f"A no es un subconjunto dirigido, no hay c tal que {a} y {b} sean dirigidos hacia él"
    
    return True, "A es un subconjunto dirigido"
# Ejemplo de uso

P = {1, 2, 3, 4, 5}
R = [(1, 3), (2, 3), (3, 4), (4, 5)]  # Relación de orden (a R b significa a <= b)
A = {1, 2, 3}

resultado, mensaje = es_subconjunto_dirigido(P, R, A)
print(mensaje)
