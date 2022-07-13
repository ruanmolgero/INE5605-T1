from datetime import datetime

from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica
from entidade.produto import Produto
from entidade.preco import Preco
from limite.tela_produto import TelaProduto


class ControladorProdutoPreco:
    def __init__(self, controlador_sistema) -> None:
        self.__produtos = []
        self.__tela_produto = TelaProduto()
        self.__controlador_sistema = controlador_sistema
        self.__produto_selecionado = None

    @property
    def produtos(self):
        return self.__produtos

    @property
    def produto_selecionado(self):
        return self.__produto_selecionado

    @produto_selecionado.setter
    def produto_selecionado(self, produto_selecionado):
        if isinstance(produto_selecionado, Produto) or produto_selecionado is None:
            self.__produto_selecionado = produto_selecionado

    def achar_preco_com_valor_e_data_atual(self, produto: Produto, valor: float) -> Preco:
        data_atual = datetime.now().date()
        preco = None
        for p in produto.precos:
            if valor == p.valor and data_atual == p.data:
                preco = p
        return preco

    def achar_preco_com_cadastrante_e_data_atual(self,
                                                 produto: Produto,
                                                 cadastrante: PessoaFisica or PessoaJuridica) -> Preco:
        data_atual = datetime.now().date()
        preco = None
        for p in produto.precos:
            if cadastrante in p.cadastrantes and data_atual == p.data:
                preco = p
        return preco

    def achar_produto_igual(self, produto_procurado: Produto) -> Produto:
        produto = None
        count = 0
        while not produto and count < len(self.produtos):
            if produto_procurado.nome == self.produtos[count].nome and \
                    produto_procurado.descricao == self.produtos[count].descricao and \
                    produto_procurado.qualificadores.sort() == self.produtos[count].qualificadores.sort():
                produto = self.produtos[count]
            count = count + 1

        return produto

    def adicionar_preco_a_produto_novo(self, produto: Produto, preco: Preco, cadastrante: PessoaFisica or PessoaJuridica):
        preco.cadastrantes.append(cadastrante)
        produto.precos.append(preco)

    def adicionar_preco_a_produto(self, produto: Produto, preco: Preco):
        produto.precos.append(preco)

    def adicionar_cadastrante_a_preco(self, preco: Preco, cadastrante: PessoaFisica or PessoaJuridica):
        preco.cadastrantes.append(cadastrante)

    def criar_produto(self, dados: dict = None):
        if not dados:
            dados_produto = self.__tela_produto.pega_dados_produto()
            self.__controlador_sistema.controlador_qualificador.abrir_tela()
            dados_produto['valor'] = self.__tela_produto.pega_valor_produto()
        else:
            dados_produto = dados

        # Pega dados do sistema
        qualificadores_produto = self.__controlador_sistema.controlador_qualificador.qualificadores_selecionados
        cadastrante_produto = self.__controlador_sistema.controlador_usuario.usuario_logado

        produto = Produto(nome=dados_produto['nome'],
                          descricao=dados_produto['descricao'],
                          qualificadores=qualificadores_produto)

        produto_existente = self.achar_produto_igual(produto)

        if produto_existente:
            # produto nao é novo
            preco = self.achar_preco_com_cadastrante_e_data_atual(
                produto=produto_existente,
                cadastrante=cadastrante_produto)

            if not preco:
                # usuario nao cadastrou nenhum produto hoje ainda
                preco = self.achar_preco_com_valor_e_data_atual(
                    produto=produto_existente,
                    valor=dados_produto['valor'])
                if not preco:
                    # preco is None
                    preco = Preco(valor=dados_produto['valor'], cadastrante=cadastrante_produto)
                    self.adicionar_preco_a_produto(produto=produto_existente, preco=preco)
                else:
                    # preco is not None, mas cadastrante é novo
                    self.adicionar_cadastrante_a_preco(preco=preco, cadastrante=cadastrante_produto)
            else:
                # raise exceção ja cadastrou produto hoje
                raise
        else:
            # produto é novo
            preco = Preco(valor=dados_produto['valor'])
            self.adicionar_preco_a_produto_novo(produto=produto, preco=preco, cadastrante=cadastrante_produto)

            self.produtos.append(produto)

        if not dados:
            self.abrir_tela_produto()

    def adiciona_cadastrante_a_preco(self, preco, cadastrante):
        if cadastrante not in preco.cadastrantes:
            preco.cadastrantes.append(cadastrante)

    def voltar(self):
        self.__controlador_sistema.controlador_categoria.categoria_selecionada = None
        self.__controlador_sistema.controlador_qualificador.zerar_qualificadores_selecionados()
        self.__controlador_sistema.controlador_categoria.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela_produto(self):
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
        lista_opcoes["q"] = self.encerrar_sistema

        while True:
            opcao_selecionada = self.__tela_produto.tela_opcoes(
                produtos)
            if isinstance(opcao_selecionada, int) and opcao_selecionada in list(range(1, len(produtos) + 1)):
                self.__produto_selecionado = lista_opcoes[opcao_selecionada]
                if self.__controlador_sistema.controlador_qualificador.qualificadores_selecionados == []:
                    self.__controlador_sistema.controlador_qualificador.abrir_tela()
            else:
                funcao_selecionada = lista_opcoes[opcao_selecionada]
                funcao_selecionada()
