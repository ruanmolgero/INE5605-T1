from datetime import datetime
from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica
from entidade.produto import Produto
from entidade.preco import Preco
from limite.tela_produto import TelaProduto


class ControladorProdutosPrecos:
    def __init__(self, controlador_sistema) -> None:
        self.__produtos = []
        self.__tela_produto = TelaProduto()
        self.__controlador_sistema = controlador_sistema
        self.__produto_escolhido = None

    @property
    def produtos(self):
        return self.__produtos

    @property
    def produto_escolhido(self):
        return self.__produto_escolhido

    @produto_escolhido.setter
    def produto_escolhido(self, produto_escolhido):
        if isinstance(produto_escolhido, Produto) or produto_escolhido is None:
            self.__produto_escolhido = produto_escolhido

    # def acha_preco_com_cadastrante(self, produto: Produto, cadastrante: PessoaFisica or PessoaJuridica):
    #     preco = None
    #     for p in produto.precos:
    #         if cadastrante in p.cadastrantes:
    #             preco = p
    #     return preco

    # def acha_preco_com_valor(self, produto: Produto, valor: float):
    #     preco = None
    #     for p in produto.precos:
    #         if valor == p.valor:
    #             preco = p
    #     return preco

    def acha_preco_com_valor_e_data_atual(self, produto: Produto, valor: float):
        data_atua = datetime.now().date()
        preco = None
        for p in produto.precos:
            if valor == p.valor and data_atua == p.data:
                preco = p
        return preco

    def acha_preco_com_cadastrante_e_data_atual(self, produto: Produto, cadastrante: PessoaFisica or PessoaJuridica):
        data_atua = datetime.now().date()
        preco = None
        for p in produto.precos:
            if cadastrante in p.cadastrantes and data_atua == p.data:
                preco = p
        return preco

    def criar_produto(self):
        dados_produto = self.__tela_produto.pega_dados_produto()
        self.__controlador_sistema.controlador_qualificadores.abre_tela()
        qualificadores_produto = self.__controlador_sistema.controlador_qualificadores.qualificadores_escolhidos
        valor_produto = self.__tela_produto.pega_valor_produto()
        cadastrante = self.__controlador_sistema.controlador_usuarios.usuario_logado

        preco_com_valor_e_data_atual = None
        preco_com_cadastrante_e_data_atual = None

        produto_novo = True
        preco_novo = True
        cadastrante_novo = True
        count = 0
        while produto_novo and count < len(self.__produtos):
            if dados_produto["nome"] == self.__produtos[count].nome and \
                    dados_produto["descricao"] == self.__produtos[count].descricao and \
                    qualificadores_produto.sort() == self.__produtos[count].qualificadores.sort():
                preco_com_valor_e_data_atual = self.acha_preco_com_valor_e_data_atual(self.__produtos[count], valor_produto)
                preco_com_cadastrante_e_data_atual = self.acha_preco_com_cadastrante_e_data_atual(self.__produtos[count], cadastrante)
                if preco_com_valor_e_data_atual and preco_com_cadastrante_e_data_atual:
                    # usuario ja fez entrada para esse produto e preco na data atual
                    produto_novo = False
                    preco_novo = False
                    cadastrante_novo = False
                elif preco_com_valor_e_data_atual and not preco_com_cadastrante_e_data_atual:
                    # existe preco para essa data em produto, mas usuario nao fez entrada ainda
                    produto_novo = False
                    preco_novo = False
                elif not preco_com_valor_e_data_atual and preco_com_cadastrante_e_data_atual:
                    # usuario ja fez entrada para esse produto na data atual mas nao no mesmo preco
                    produto_novo = False
                    cadastrante_novo = False
            if produto_novo:
                count = count + 1

        if produto_novo:
            produto = Produto(nome=dados_produto['nome'],
                              descricao=dados_produto['descricao'],
                              qualificadores=qualificadores_produto)
            preco = Preco(valor=valor_produto, cadastrante=cadastrante)
            self.adiciona_preco_a_produto_novo(produto=produto, preco=preco)

            self.__produtos.append(produto)
        else:
            produto = self.__produtos[count]
            if cadastrante_novo:
                if preco_novo:
                    preco = Preco(valor=valor_produto, cadastrante=cadastrante)
                    self.adiciona_preco_a_produto_existente(produto=produto, preco=preco)
                else:
                    self.adiciona_cadastrante_a_preco(preco_com_valor_e_data_atual, cadastrante)
            else:
                self.__tela_produto.mostra_mensagem(
                    "Você já cadastrou um produto com mesmo preço no dia de hoje")

    def adiciona_preco_a_produto_novo(self, produto, preco):
        produto.precos.append(preco)

    def adiciona_preco_a_produto_existente(self, produto, preco):
        produto.precos.append(preco)

    def adiciona_cadastrante_a_preco(self, preco, cadastrante):
        if cadastrante not in preco.cadastrantes:
            preco.cadastrantes.append(cadastrante)

    def voltar(self):
        self.__controlador_sistema.controlador_categorias.categoria_escolhida = None
        self.__controlador_sistema.controlador_qualificadores.zera_qualificadores_escolhidos()
        self.__controlador_sistema.controlador_categorias.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela_produto(self):
        lista_opcoes = {}
        count = 1
        produtos = {}

        for produto in self.__produtos:
            lista_opcoes[count] = produto
            qualificadores = {}
            count_qualificadores = 0
            # while count_qualificadores < 3 and count_qualificadores < len(produto.qualificadores):
            #     qualificadores[count_qualificadores] = (qualificador.titulo, qualificador.descricao)
            produtos[count] = (produto.nome, produto.descricao)
        lista_opcoes[len(self.__produtos)+1] = self.criar_produto
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerra_sistema

        while True:
            opcao_escolhida = self.__tela_produto.tela_opcoes(
                produtos)
            if isinstance(opcao_escolhida, int) and opcao_escolhida in list(range(1, len(produtos) + 1)):
                self.__produto_escolhido = lista_opcoes[opcao_escolhida]
                if self.__controlador_sistema.controlador_qualificadores.qualificadores_escolhidos == []:
                    self.__controlador_sistema.controlador_qualificadores.abre_tela()
            else:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
