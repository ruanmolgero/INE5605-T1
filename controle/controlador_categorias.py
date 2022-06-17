from entidade import categoria
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

    def criar_categoria(self):
        dados_categoria = self.__tela_categoria.pega_dados_categoria()
        for c in self.__categorias:
            if dados_categoria["nome"] == c.nome and dados_categoria["descrição"] == c.descricao:
                self.__tela_categoria.mostra_mensagem(
                    "Categoria já cadastrada")
            else:
                categoria = Categoria(nome=dados_categoria['nome'],
                                      descricao=dados_categoria['descrição'])
                self.__categorias.append(categoria)
                self.__categoria_escolhida = categoria
                self.__controlador_sistema.abre_tela_produto()

    def voltar(self):
        self.__controlador_sistema.controlador_supermercados.supermercado_escolhido = None
        self.__controlador_sistema.controlador_supermercados.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        print(f"usuario: {self.__controlador_sistema.controlador_usuarios.usuario_logado} |",
              f"supermercado: {self.__controlador_sistema.controlador_supermercados.supermercado_escolhido} |",
              f"categoria: {self.__controlador_sistema.controlador_categorias.categoria_escolhida} |")
        lista_opcoes = {}
        count = 1
        categorias = {}

        for categoria in self.__categorias:
            lista_opcoes[count] = categoria
            categorias[count] = (categoria.nome, categoria.descricao)
        lista_opcoes[len(self.__categorias)+1] = self.criar_categoria
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerra_sistema

        while True:
            opcao_escolhida = self.__tela_categoria.tela_opcoes(
                categorias)
            if isinstance(opcao_escolhida, int) and opcao_escolhida in list(range(1, len(categorias) + 1)):
                self.__categoria_escolhida = lista_opcoes[opcao_escolhida]
                self.__controlador_sistema.abre_tela_produto()
            else:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
