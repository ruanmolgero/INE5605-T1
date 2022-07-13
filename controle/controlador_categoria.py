from entidade.categoria import Categoria
from entidade.produto import Produto
from limite.tela_categoria import TelaCategoria


class ControladorCategoria:
    def __init__(self, controlador_sistema) -> None:
        self.__categorias = []
        self.__tela_categoria = TelaCategoria()
        self.__controlador_sistema = controlador_sistema
        self.__categoria_selecionada = None

    @property
    def categorias(self):
        return self.__categorias

    @property
    def categoria_selecionada(self):
        return self.__categoria_selecionada

    @categoria_selecionada.setter
    def categoria_selecionada(self, categoria_selecionada):
        if isinstance(categoria_selecionada, Categoria) or categoria_selecionada is None:
            self.__categoria_selecionada = categoria_selecionada

    def achar_categoria_igual(self, categoria_procurada: Categoria):
        categoria = None
        count = 0
        while not categoria and count < len(self.categorias):
            if categoria_procurada.nome == self.__categorias[count].nome and \
                    categoria_procurada.descricao == self.__categorias[count].descricao:
                # self.__tela_categoria.mostra_mensagem("Categoria já cadastrada")
                categoria = self.categorias[count]
            count = count + 1

        return categoria

    def adicionar_produto_a_categoria(self, categoria: Categoria, produto: Produto):
        if produto not in categoria.produtos:
            self.categoria_selecionada.produtos.append(produto)

    def criar_categoria(self, dados: dict = None):
        if not dados:
            dados_categoria = self.__tela_categoria.pega_dados_categoria()
        else:
            dados_categoria = dados

        categoria = Categoria(nome=dados_categoria['nome'],
                              descricao=dados_categoria['descricao'])

        categoria_jah_existe = self.achar_categoria_igual(categoria)
        if not categoria_jah_existe:
            self.__categorias.append(categoria)
            self.__categoria_selecionada = categoria
            self.__controlador_sistema.controlador_supermercado.adicionar_categoria_a_supermercado(
                supermercado=self.__controlador_sistema.controlador_supermercado.supermercado_selecionado,
                categoria=categoria)
            if not dados:
                self.__controlador_sistema.controlador_produto_preco.abrir_tela_produto()
        else:
            # categoria jah existe bla bla bla
            raise

    def incluir_produto_a_categoria_selecionada(self, produto):
        if produto not in self.__categoria_selecionada.produtos:
            self.__categoria_selecionada.produtos.append(produto)

    def voltar(self):
        self.__controlador_sistema.controlador_supermercado.supermercado_selecionado = None
        self.__controlador_sistema.controlador_supermercado.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        lista_opcoes = {}
        count = 1
        categorias = {}

        for categoria in self.__categorias:
            lista_opcoes[count] = categoria
            categorias[count] = (categoria.nome, categoria.descricao)
        lista_opcoes[len(self.__categorias)+1] = self.criar_categoria
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerrar_sistema

        while True:
            opcao_selecionada = self.__tela_categoria.tela_opcoes(
                categorias)
            if isinstance(opcao_selecionada, int) and opcao_selecionada in list(range(1, len(categorias) + 1)):
                self.__categoria_selecionada = lista_opcoes[opcao_selecionada]
                self.__controlador_sistema.controlador_produto_preco.abrir_tela_produto()
            else:
                funcao_selecionada = lista_opcoes[opcao_selecionada]
                funcao_selecionada()
