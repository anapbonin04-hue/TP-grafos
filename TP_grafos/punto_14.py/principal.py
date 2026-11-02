
from Grafos import Grafo


# CREAR EL GRAFO
g = Grafo()


# A. CARGAR LOS VERTICES

ambientes = [
    "Cocina",
    "Comedor",
    "Cochera",
    "Quincho",
    "Baño 1",
    "Baño 2",
    "Habitación 1",
    "Habitación 2",
    "Sala de estar",
    "Terraza",
    "Patio"
]

for ambiente in ambientes:
    g.agregar_vertice(ambiente)


# B. CARGAR LAS ARISTAS (DISTANCIAS EN METROS)

# COCINA: 5 ARISTAS
g.agregar_arista("Cocina", "Comedor", 3)
g.agregar_arista("Cocina", "Patio", 10)
g.agregar_arista("Cocina", "Cochera", 8)
g.agregar_arista("Cocina", "Baño 1", 5)
g.agregar_arista("Cocina", "Habitación 1", 9)

# COMEDOR: 5 ARISTAS
g.agregar_arista("Comedor", "Cochera", 7)
g.agregar_arista("Comedor", "Quincho", 6)
g.agregar_arista("Comedor", "Baño 2", 8)
g.agregar_arista("Comedor", "Habitación 2", 7)

# COCHERA
g.agregar_arista("Cochera", "Quincho", 4)
g.agregar_arista("Cochera", "Terraza", 9)

# QUINCHO
g.agregar_arista("Quincho", "Baño 1", 5)

# BAÑO 1
g.agregar_arista("Baño 1", "Baño 2", 3)

# BAÑO 2
g.agregar_arista("Baño 2", "Habitación 1", 4)

# HABITACIÓN 1
g.agregar_arista("Habitación 1", "Habitación 2", 3)

# HABITACIÓN 2
g.agregar_arista("Habitación 2", "Sala de estar", 6)

# SALA DE ESTAR
g.agregar_arista("Sala de estar", "Terraza", 5)
g.agregar_arista("Sala de estar", "Patio", 8)

# TERRAZA
g.agregar_arista("Terraza", "Patio", 4)


# MOSTRAR EL GRAFO
print("GRAFO DE LA CASA")
g.mostrar()


# C. ARBOL DE EXPANSION MINIMA

print()
print("ARBOL DE EXPANSION MINIMA")

arbol, total = g.kruskal()

for origen, destino, peso in arbol:

    print(origen, "-", destino, ":", peso, "metros")

print("Total de cable necesario:", total, "metros")


# D. CAMINO MAS CORTO

print()
print("CAMINO MAS CORTO")

camino, distancia = g.dijkstra(
    "Habitación 1",
    "Sala de estar"
)

if len(camino) > 0:

    print("Recorrido:", " -> ".join(camino))

    print("Distancia total:", distancia, "metros")

else:

    print("No existe un camino entre los ambientes")
