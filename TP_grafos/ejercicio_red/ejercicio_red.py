from red import Grafo

# CREAR GRAFO


red = Grafo()



# a) AGREGAR NODOS Y TIPOS

# Notebooks
red.agregar_nodo("Red Hat", "notebook")
red.agregar_nodo("Debian", "notebook")
red.agregar_nodo("Arch", "notebook")

# PC
red.agregar_nodo("Manjaro", "pc")
red.agregar_nodo("Parrot", "pc")
red.agregar_nodo("Fedora", "pc")
red.agregar_nodo("Mint", "pc")
red.agregar_nodo("Ubuntu", "pc")

# Servidores
red.agregar_nodo("Guarani", "servidor")
red.agregar_nodo("MongoDB", "servidor")

# Routers
red.agregar_nodo("Router 1", "router")
red.agregar_nodo("Router 2", "router")
red.agregar_nodo("Router 3", "router")

# Switches
red.agregar_nodo("Switch 1", "switch")
red.agregar_nodo("Switch 2", "switch")

# Impresora
red.agregar_nodo("Impresora", "impresora")


# CARGAR CONEXIONES


# Router 2
red.agregar_conexion("Red Hat", "Router 2", 25)
red.agregar_conexion("Guarani", "Router 2", 9)
red.agregar_conexion("Router 2", "Router 3", 50)
red.agregar_conexion("Router 2", "Router 1", 37)

# Routers
red.agregar_conexion("Router 3", "Router 1", 43)
red.agregar_conexion("Router 3", "Switch 2", 61)

# Switch 1
red.agregar_conexion("Switch 1", "Router 1", 29)
red.agregar_conexion("Switch 1", "Debian", 17)
red.agregar_conexion("Switch 1", "Ubuntu", 18)
red.agregar_conexion("Switch 1", "Impresora", 22)
red.agregar_conexion("Switch 1", "Mint", 80)

# Switch 2
red.agregar_conexion("Switch 2", "Manjaro", 40)
red.agregar_conexion("Switch 2", "Parrot", 12)
red.agregar_conexion("Switch 2", "MongoDB", 5)
red.agregar_conexion("Switch 2", "Fedora", 3)
red.agregar_conexion("Switch 2", "Arch", 56)

# a) MOSTRAR NODOS

print("\n========== PUNTO A ==========")

red.mostrar_nodos()

# b) BARRIDO EN PROFUNDIDAD
# Y AMPLITUD

print("\n========== PUNTO B ==========")

print("\nDFS desde Red Hat:")
red.profundidad("Red Hat")

print("\nBFS desde Red Hat:")
red.amplitud("Red Hat")


print("\nDFS desde Debian:")
red.profundidad("Debian")

print("\nBFS desde Debian:")
red.amplitud("Debian")


print("\nDFS desde Arch:")
red.profundidad("Arch")

print("\nBFS desde Arch:")
red.amplitud("Arch")

# c) CAMINO MÁS CORTO A LA IMPRESORA


print("\n========== PUNTO C ==========")

print("\nDesde Manjaro:")
red.camino_minimo("Manjaro", "Impresora")

print("\nDesde Red Hat:")
red.camino_minimo("Red Hat", "Impresora")

print("\nDesde Fedora:")
red.camino_minimo("Fedora", "Impresora")


# d) ÁRBOL DE EXPANSIÓN MÍNIMA


print("\n========== PUNTO D ==========")

red.prim("Red Hat")



# e) PC MÁS CERCANA A GUARANI

print("\n========== PUNTO E ==========")

print("\nDesde Manjaro:")
red.camino_minimo("Manjaro", "Guarani")

print("\nDesde Parrot:")
red.camino_minimo("Parrot", "Guarani")

print("\nDesde Fedora:")
red.camino_minimo("Fedora", "Guarani")

print("\nDesde Mint:")
red.camino_minimo("Mint", "Guarani")

print("\nDesde Ubuntu:")
red.camino_minimo("Ubuntu", "Guarani")



# f) PC DEL SWITCH 1 MÁS CERCANA A MongoDB

print("\n========== PUNTO F ==========")

print("\nDesde Debian:")
red.camino_minimo("Debian", "MongoDB")

print("\nDesde Ubuntu:")
red.camino_minimo("Ubuntu", "MongoDB")

print("\nDesde Mint:")
red.camino_minimo("Mint", "MongoDB")

# g) CAMBIAR IMPRESORA AL ROUTER 2
# Y VOLVER A HACER B


print("\n========== PUNTO G ==========")

red.cambiar_impresora()


print("\nDFS desde Red Hat:")
red.profundidad("Red Hat")

print("\nBFS desde Red Hat:")
red.amplitud("Red Hat")


print("\nDFS desde Debian:")
red.profundidad("Debian")

print("\nBFS desde Debian:")
red.amplitud("Debian")


print("\nDFS desde Arch:")
red.profundidad("Arch")

print("\nBFS desde Arch:")
red.amplitud("Arch")

# h) GRAFO NO DIRIGIDO

print("\n========== PUNTO H ==========")

print("""
El grafo es NO DIRIGIDO porque cada conexión se
agrega en los dos sentidos.

Por ejemplo:

Router 2 ---- Router 3

permite ir:

Router 2 -> Router 3

y también:

Router 3 -> Router 2""")