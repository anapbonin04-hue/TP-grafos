class Conexion:
    def __init__(self, destino, peso):
        self.destino = destino
        self.peso = peso


class Nodo:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.conexiones = []

        # Datos utilizados por Dijkstra
        self.distancia = float("inf")
        self.anterior = None
        self.visitado = False


class Grafo:
    def __init__(self):
        self.nodos = []

    # -----------------------------------------
    # Buscar un nodo
    # -----------------------------------------
    def buscar_nodo(self, nombre):
        for nodo in self.nodos:
            if nodo.nombre == nombre:
                return nodo

        return None

    # -----------------------------------------
    # Agregar nodo
    # -----------------------------------------
    def agregar_nodo(self, nombre, tipo):
        nodo = Nodo(nombre, tipo)
        self.nodos.append(nodo)

    # -----------------------------------------
    # Agregar conexión
    # GRAFO NO DIRIGIDO
    # -----------------------------------------
    def agregar_conexion(self, nombre1, nombre2, peso):

        nodo1 = self.buscar_nodo(nombre1)
        nodo2 = self.buscar_nodo(nombre2)

        if nodo1 is not None and nodo2 is not None:

            # conexión de ida
            nodo1.conexiones.append(Conexion(nodo2, peso))

            # conexión de vuelta
            nodo2.conexiones.append(Conexion(nodo1, peso))

    # -----------------------------------------
    # Mostrar nodos
    # -----------------------------------------
    def mostrar_nodos(self):

        for nodo in self.nodos:
            print(nodo.nombre, "-", nodo.tipo)

    # -----------------------------------------
    # BARRIDO EN PROFUNDIDAD - DFS
    # -----------------------------------------
    def profundidad(self, nombre_inicio):

        inicio = self.buscar_nodo(nombre_inicio)

        if inicio is None:
            return

        visitados = []

        self._profundidad_recursiva(inicio, visitados)

        for nodo in visitados:
            print(nodo.nombre, end=" -> ")

        print("FIN")

    def _profundidad_recursiva(self, nodo, visitados):

        visitados.append(nodo)

        for conexion in nodo.conexiones:

            if conexion.destino not in visitados:
                self._profundidad_recursiva(
                    conexion.destino,
                    visitados
                )

    # -----------------------------------------
    # BARRIDO EN AMPLITUD - BFS
    # -----------------------------------------
    def amplitud(self, nombre_inicio):

        inicio = self.buscar_nodo(nombre_inicio)

        if inicio is None:
            return

        cola = []
        visitados = []

        cola.append(inicio)
        visitados.append(inicio)

        while len(cola) > 0:

            nodo = cola.pop(0)

            print(nodo.nombre, end=" -> ")

            for conexion in nodo.conexiones:

                if conexion.destino not in visitados:

                    visitados.append(conexion.destino)
                    cola.append(conexion.destino)

        print("FIN")

    # -----------------------------------------
    # DIJKSTRA
    # -----------------------------------------
    def camino_minimo(self, nombre_inicio, nombre_fin):

        inicio = self.buscar_nodo(nombre_inicio)
        fin = self.buscar_nodo(nombre_fin)

        if inicio is None or fin is None:
            return

        # Reiniciar datos
        for nodo in self.nodos:
            nodo.distancia = float("inf")
            nodo.anterior = None
            nodo.visitado = False

        inicio.distancia = 0

        while True:

            actual = None

            # Buscar nodo no visitado con menor distancia
            for nodo in self.nodos:

                if not nodo.visitado:

                    if actual is None or nodo.distancia < actual.distancia:
                        actual = nodo

            # No quedan nodos
            if actual is None:
                break

            # Llegamos al destino
            if actual == fin:
                break

            actual.visitado = True

            # Revisar conexiones
            for conexion in actual.conexiones:

                vecino = conexion.destino

                nueva_distancia = (
                    actual.distancia + conexion.peso
                )

                if nueva_distancia < vecino.distancia:

                    vecino.distancia = nueva_distancia
                    vecino.anterior = actual

        # Mostrar camino
        camino = []

        actual = fin

        while actual is not None:

            camino.insert(0, actual)
            actual = actual.anterior

        print("Camino:", end=" ")

        for nodo in camino:
            print(nodo.nombre, end=" -> ")

        print("FIN")
        print("Costo total:", fin.distancia)

    # -----------------------------------------
    # ÁRBOL DE EXPANSIÓN MÍNIMA - PRIM
    # -----------------------------------------
    def prim(self, nombre_inicio):

        inicio = self.buscar_nodo(nombre_inicio)

        if inicio is None:
            return

        visitados = []
        arbol = []
        costo_total = 0

        visitados.append(inicio)

        while len(visitados) < len(self.nodos):

            mejor_conexion = None
            nodo_origen = None

            # Buscar la conexión más barata
            # que salga de un visitado hacia uno no visitado
            for nodo in visitados:

                for conexion in nodo.conexiones:

                    if conexion.destino not in visitados:

                        if (
                            mejor_conexion is None
                            or conexion.peso < mejor_conexion.peso
                        ):

                            mejor_conexion = conexion
                            nodo_origen = nodo

            if mejor_conexion is None:
                break

            arbol.append(
                (
                    nodo_origen,
                    mejor_conexion.destino,
                    mejor_conexion.peso
                )
            )

            costo_total += mejor_conexion.peso

            visitados.append(mejor_conexion.destino)

        print("ÁRBOL DE EXPANSIÓN MÍNIMA")

        for conexion in arbol:

            print(
                conexion[0].nombre,
                "-",
                conexion[1].nombre,
                "peso:",
                conexion[2]
            )

        print("Costo total:", costo_total)

    # -----------------------------------------
    # Cambiar conexión de la impresora
    # -----------------------------------------
    def cambiar_impresora(self):

        switch1 = self.buscar_nodo("Switch 1")
        router2 = self.buscar_nodo("Router 2")
        impresora = self.buscar_nodo("Impresora")

        # Eliminar conexión Switch 1 - Impresora
        for conexion in switch1.conexiones:

            if conexion.destino == impresora:
                switch1.conexiones.remove(conexion)
                break

        for conexion in impresora.conexiones:

            if conexion.destino == switch1:
                impresora.conexiones.remove(conexion)
                break

        # Agregar nueva conexión Router 2 - Impresora
        router2.conexiones.append(
            Conexion(impresora, 22)
        )

        impresora.conexiones.append(
            Conexion(router2, 22)
        )

        print("La impresora ahora está conectada al Router 2.")