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

    def adicionar_qualificador_escolhido(self, qualificador):
        if isinstance(qualificador, Qualificador) and \
                qualificador not in self.__qualificadores_selecionados:
            self.__qualificadores_selecionados.append(qualificador)

    def zerar_qualificadores_selecionados(self):
        self.__qualificadores_selecionados = []

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
            self.adicionar_qualificador_escolhido(qualificador)
            # if not dados:
            #     self.__controlador_sistema.controlador_produto_preco.abre_tela_produto()
        else:
            # qualificador jah existe, mas adiciona ainda assim na lista de escolhidos
            self.adicionar_qualificador_escolhido(qualificador)
            raise

    def voltar(self):
        self.zerar_qualificadores_selecionados()
        # self.__controlador_sistema.controlador_produto_preco.abre_tela_produto()

    def encerrar_sistema(self):
        exit(0)

    def abre_tela(self, qualificadores_selecionados: list = []):
        lista_opcoes = {}
        count = 1
        qualificadores = {}

        for qualificador in self.__qualificadores:
            if qualificador not in qualificadores_selecionados:
                lista_opcoes[count] = qualificador
                qualificadores[count] = (
                    qualificador.titulo, qualificador.descricao)
        lista_opcoes[len(lista_opcoes)+1] = self.criar_qualificador
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerra_sistema

        while True:
            opcao_escolhida = self.__tela_qualificador.tela_opcoes(
                qualificadores)
            if isinstance(opcao_escolhida, int) and opcao_escolhida in list(range(1, len(qualificadores) + 1)):
                self.adicionar_qualificador_escolhido(
                    lista_opcoes[opcao_escolhida])
                self.abre_tela(self.__qualificadores_selecionados)
            elif opcao_escolhida == "c":
                return
            else:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
