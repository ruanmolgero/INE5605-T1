from entidade.preco import Preco
from entidade.qualificador import Qualificador
from limite.tela_qualificador import TelaQualificador


class ControladorQualificador:
    def __init__(self, controlador_sistema) -> None:
        self.__qualificadores = []
        self.__tela_qualificador = TelaQualificador()
        self.__controlador_sistema = controlador_sistema
        self.__qualificadores_selecionados = []

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def qualificadores_selecionados(self):
        return self.__qualificadores_selecionados

    def adicionar_qualificador_selecionado(self, qualificador):
        if isinstance(qualificador, Qualificador) and \
                qualificador not in self.qualificadores_selecionados:
            self.qualificadores_selecionados.append(qualificador)

    def zerar_qualificadores_selecionados(self):
        self.qualificadores_selecionados = []

    def achar_qualificador_igual(self, qualificador_procurado: Qualificador):
        qualificador = None
        count = 0
        while not qualificador and count < len(self.qualificadores):
            if qualificador_procurado.titulo == self.qualificadores[count].titulo and \
                    qualificador_procurado.descricao == self.qualificadores[count].descricao:
                qualificador = self.qualificadores[count]
            count = count + 1

        return qualificador

    def criar_qualificador(self, dados: dict = None):
        if not dados:
            dados_qualificador = self.__tela_qualificador.pega_dados_qualificador()
        else:
            dados_qualificador = dados

        qualificador = Qualificador(titulo=dados_qualificador['titulo'],
                                    descricao=dados_qualificador['descricao'])

        qualificador_existente = self.achar_qualificador_igual(qualificador)
        if not qualificador_existente:
            self.qualificadores.append(qualificador)
            self.adicionar_qualificador_selecionado(qualificador)
            # if not dados:
            #     self.__controlador_sistema.controlador_produto_preco.abrir_tela_produto()
        else:
            # qualificador jah existe, mas adiciona ainda assim na lista de selecionados
            self.adicionar_qualificador_selecionado(qualificador)
            raise

    def voltar(self):
        self.zerar_qualificadores_selecionados()
        self.__controlador_sistema.controlador_produto_preco.abrir_tela_produto()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self, qualificadores_selecionados: list = []):
        lista_opcoes = {}
        count = 1
        qualificadores = {}
        # qualificadores_ja_selecionados = []

        for qualificador in self.__qualificadores:
            if qualificador not in qualificadores_selecionados:
                lista_opcoes[count] = qualificador
                qualificadores[count] = (qualificador.titulo, qualificador.descricao)
        # for qualificador in qualificadores_selecionados:
            # qualificadores_ja_selecionados.append((qualificador.titulo, qualificador.descricao))
        lista_opcoes[len(lista_opcoes)+1] = self.criar_qualificador
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerrar_sistema

        while True:
            opcao_selecionada = self.__tela_qualificador.tela_opcoes(qualificadores)
            if isinstance(opcao_selecionada, int) and opcao_selecionada in list(range(1, len(qualificadores) + 1)):
                self.adicionar_qualificador_selecionado(lista_opcoes[opcao_selecionada])
                self.abrir_tela(self.qualificadores_selecionados)
            # TODO: testa qualificadores selecionados e dependendo criar novo produto ou
            # TODO: chama metodo para adicionar valor a produto existente
            elif opcao_selecionada == "c":
                produto_selecionado = self.__controlador_sistema.controlador_produto_preco.produto_selecionado
                if produto_selecionado:
                    if (produto_selecionado.qualificadores.sort() == self.qualificadores_selecionados.sort()):
                        valor_produto = self.__controlador_sistema.controlador_produto_preco.tela_produto.pega_valor_produto()
                        # preco = Preco(valor=valor_produto)
                        self.__controlador_sistema.controlador_produto_preco.adicionar_valor_a_produto_selecionado(
                            valor=valor_produto)
                        pass
                        # self.__controlador_sistema.controlador_produto_preco.
                else:
                    return
            else:
                funcao_selecionada = lista_opcoes[opcao_selecionada]
                funcao_selecionada()
