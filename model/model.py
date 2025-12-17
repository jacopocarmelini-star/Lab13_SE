import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self._lista_cromosomi = []
        self._id_map = {}
        cromosomi = DAO.getCromosomi()
        for c in cromosomi:
            self._lista_cromosomi.append(c)
        for c in self._lista_cromosomi:
            self._id_map[c.cromosoma] = c



    def creaGrafo(self):
        self.G.clear()
        self.G.add_nodes_from(self._lista_cromosomi)

        interazioni = DAO.getInterazioni(self._id_map)
        # leggo le connessioni dal DAO
        for i in interazioni:
            self.G.add_edge(i.cromosoma1, i.cromosoma2, peso=i.peso)

    def get_nodes(self):
        return len(self.G.nodes())

    def get_edges(self):
        return len(self.G.edges())

    def get_edges_weight_min_max(self):
        pesi = []
        for archi in self.G.edges(data=True):
            pesi.append(archi[2]["peso"])
        return min(pesi), max(pesi)

    def conta_edges(self, soglia):
        minori = []
        maggiori = []

        for archi in self.G.edges(data=True):
            if archi[2]["peso"] < soglia:
                minori.append(archi)
            elif archi[2]["peso"] > soglia:
                maggiori.append(archi)

        return len(minori), len(maggiori)

    def getCamminoCorto(self, soglia):
        self.costoMax = 0
        self.best_percorso = []
        parziale = []

        grafo_temp = self.G.copy()
        edgesDaRimuovere = []
        for u, v, data in grafo_temp.edges(data=True):
            if data['peso'] <= soglia:
                edgesDaRimuovere.append((u, v))

        grafo_temp.remove_edges_from(edgesDaRimuovere)

        self._ricorsione(grafo_temp, self.costoMax, parziale)


    def _ricorsione(self,grafo_temp, costoMax, parziale):
        # parto da nodo[-1](ultimo)
        # calcolo vicini ammisssibili com funzione .out_edges()

        #guarda week13 artsmia


