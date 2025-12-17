import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self._model.creaGrafo()
        num_nodi = self._model.get_nodes()
        num_archi = self._model.get_edges()
        peso_min, peso_max = self._model.get_edges_weight_min_max()
        self._view.lista_visualizzazione_1.controls.clear()

        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"Numero di vertici : {num_nodi}  Numero di archi: {num_archi}"))
        self._view.lista_visualizzazione_1.controls.append(ft.Text( f"Informazioni sui pesi degli archi - valore minimo: {peso_min} e valore massimo {peso_max}"))


        self._view.page.update()


    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        # TODO
        soglia = int(self._view.txt_name.value)

        if soglia<=7 and soglia>=3:
            minori, maggiori = self._model.conta_edges(soglia)
            self._view.lista_visualizzazione_2.controls.clear()

            self._view.lista_visualizzazione_2.controls.append(
                ft.Text(f"Numero archi con peso maggiore della soglia : {maggiori}"))
            self._view.lista_visualizzazione_2.controls.append(
                ft.Text(f"Numero archi con peso minore della soglia : {minori}"))
            self._view.page.update()

        else:
            self._view.alert.show_alert("Inserire numero tra 3 e 7")


    def handle_ricerca(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        # TODO