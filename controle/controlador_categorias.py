from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria

class ControladorCategorias:
    def __init__(self, controlador_sistema) -> None:
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema
        self.__categoria_escolhida = None

    @property
    def categorias(self):
        return self.__categorias

    @property
    def categoria_escolhida(self):
        return self.__categoria_escolhida

    @categoria_escolhida.setter
    def categoria_escolhida(self, categoria_escolhida):
        if isinstance(categoria_escolhida, Categoria):
            self.__categoria_escolhida = categoria_escolhida

    def voltar(self):
        self.__supermercado_escolhido = None
        self.__controlador_sistema.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {}
        count = 1
        supermercados = {}

        for categoria in self.__categorias:
            lista_opcoes[count] = categoria
            supermercados[count] = (categoria.nome, categoria.descricao)
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerra_sistema

        while True:
            opcao_escolhida = self.__tela_supermercado.tela_opcoes(
                supermercados)
            if isinstance(opcao_escolhida, int):
                self.__supermercado_escolhido = lista_opcoes[opcao_escolhida]
            else:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()