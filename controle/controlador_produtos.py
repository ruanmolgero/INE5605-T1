from entidade.produto import Produto
from limite.tela_produto import TelaProduto


class ControladorProdutos:
    def __init__(self, controlador_sistema) -> None:
        self.__produtos = []
        self.__tela_produto = TelaProduto()
        self.__controlador_sistema = controlador_sistema
        self.__produto_escolhido = None

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def produto_escolhido(self):
        return self.__produto_escolhido

    @produto_escolhido.setter
    def produto_escolhido(self, produto_escolhido):
        if isinstance(produto_escolhido, Produto) or produto_escolhido is None:
            self.__produto_escolhido = produto_escolhido

    def criar_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        produto_valido = True
        count = 0
        while produto_valido and count < len(self.__produtos):
            if dados_produto["nome"] == self.__produtos[count].nome and \
                    dados_produto["descrição"] == self.__produtos[count].descricao:
                self.__tela_produto.mostra_mensagem(
                    "Produto já cadastrada")
                produto_valido = False
            count = count + 1
        if produto_valido:
            produto = Produto(nome=dados_produto['nome'],
                              descricao=dados_produto['descrição'],)
            self.__produtos.append(produto)
            self.__produto_escolhido = produto
            self.__controlador_sistema.controlador_qualificadores.abre_tela()

    def abre_tela(self):
        print(f"usuario: {self.__controlador_sistema.controlador_usuarios.usuario_logado} |",
              f"supermercado: {self.__controlador_sistema.controlador_supermercados.supermercado_escolhido} |",
              f"categoria: {self.__controlador_sistema.controlador_categorias.categoria_escolhida} |")
        lista_opcoes = {}
        count = 1
        produtos = {}

        for produto in self.__produtos:
            lista_opcoes[count] = produto
            produtos[count] = (produto.nome, produto.descricao)
        lista_opcoes[len(self.__produtos)+1] = self.criar_produto
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerra_sistema

        while True:
            opcao_escolhida = self.__tela_produto.tela_opcoes(
                produtos)
            if isinstance(opcao_escolhida, int) and opcao_escolhida in list(range(1, len(produtos) + 1)):
                self.__produto_escolhido = lista_opcoes[opcao_escolhida]
                self.__controlador_sistema.controlador_qualificadores.abre_tela()
            else:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
