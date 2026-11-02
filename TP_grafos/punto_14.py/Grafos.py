
class Grafo:

    # NODO VERTICE
    class NodoVertice:

        def __init__(self, nombre):
            self.nombre = nombre
            self.aristas = []


    # CONSTRUCTOR
    def __init__(self):
        self.vertices = []


    # BUSCAR VERTICE
    def buscar_vertice(self, nombre):

        for i in range(len(self.vertices)):

            if self.vertices[i].nombre == nombre:
                return i

        return None


    # AGREGAR VERTICE
    def agregar_vertice(self, nombre):

        if self.buscar_vertice(nombre) is None:

            nuevo = self.NodoVertice(nombre)
            self.vertices.append(nuevo)


    # AGREGAR ARISTA
    def agregar_arista(self, origen, destino, peso):

        pos_origen = self.buscar_vertice(origen)
        pos_destino = self.buscar_vertice(destino)

        if pos_origen is not None and pos_destino is not None:

            self.vertices[pos_origen].aristas.append(
                (destino, peso)
            )

            self.vertices[pos_destino].aristas.append(
                (origen, peso)
            )


    # MOSTRAR GRAFO
    def mostrar(self):

        for vertice in self.vertices:

            print(vertice.nombre)

            for destino, peso in vertice.aristas:

                print("   ->", destino, "-", peso, "metros")


    # KRUSKAL: ARBOL DE EXPANSION MINIMA
    def kruskal(self):

        aristas = []

        # CARGAR LAS ARISTAS EN UNA LISTA
        for i in range(len(self.vertices)):

            for destino, peso in self.vertices[i].aristas:

                pos_destino = self.buscar_vertice(destino)

                # EVITAR CARGAR DOS VECES LA MISMA ARISTA
                if i < pos_destino:

                    aristas.append(
                        (peso, i, pos_destino)
                    )

        # ORDENAR LAS ARISTAS POR PESO
        aristas.sort()

        # CREAR LA LISTA DE PADRES
        padre = []

        for i in range(len(self.vertices)):
            padre.append(i)


        # BUSCAR EL REPRESENTANTE DEL CONJUNTO
        def buscar(posicion):

            if padre[posicion] != posicion:

                padre[posicion] = buscar(padre[posicion])

            return padre[posicion]


        # UNIR DOS CONJUNTOS
        def unir(origen, destino):

            raiz_origen = buscar(origen)
            raiz_destino = buscar(destino)

            if raiz_origen != raiz_destino:

                padre[raiz_origen] = raiz_destino

                return True

            return False


        arbol = []
        total = 0

        # SELECCIONAR LAS ARISTAS
        for peso, origen, destino in aristas:

            if unir(origen, destino):

                nombre_origen = self.vertices[origen].nombre
                nombre_destino = self.vertices[destino].nombre

                arbol.append(
                    (nombre_origen, nombre_destino, peso)
                )

                total += peso

        return arbol, total


    # DIJKSTRA: CAMINO MAS CORTO
    def dijkstra(self, origen, destino):

        pos_origen = self.buscar_vertice(origen)
        pos_destino = self.buscar_vertice(destino)

        if pos_origen is None or pos_destino is None:
            return [], float('inf')


        # INICIALIZAR LAS LISTAS
        distancias = []
        anteriores = []
        visitados = []

        for i in range(len(self.vertices)):

            distancias.append(float('inf'))
            anteriores.append(None)
            visitados.append(False)

        distancias[pos_origen] = 0


        # RECORRER LOS VERTICES
        for i in range(len(self.vertices)):

            menor = None
            distancia_menor = float('inf')

            # BUSCAR EL VERTICE NO VISITADO DE MENOR DISTANCIA
            for j in range(len(self.vertices)):

                if not visitados[j]:

                    if distancias[j] < distancia_menor:

                        menor = j
                        distancia_menor = distancias[j]


            if menor is None:
                break

            visitados[menor] = True

            if menor == pos_destino:
                break


            # RECORRER LAS ARISTAS DEL VERTICE
            for vecino, peso in self.vertices[menor].aristas:

                pos_vecino = self.buscar_vertice(vecino)

                if not visitados[pos_vecino]:

                    nueva_distancia = distancias[menor] + peso

                    if nueva_distancia < distancias[pos_vecino]:

                        distancias[pos_vecino] = nueva_distancia
                        anteriores[pos_vecino] = menor


        # RECONSTRUIR EL CAMINO
        if distancias[pos_destino] == float('inf'):
            return [], float('inf')

        camino = []
        actual = pos_destino

        while actual is not None:

            camino.append(self.vertices[actual].nombre)

            actual = anteriores[actual]

        camino.reverse()

        return camino, distancias[pos_destino]
