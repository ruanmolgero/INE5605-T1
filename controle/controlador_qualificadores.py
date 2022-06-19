from entidade import qualificador
from entidade.qualificador import Qualificador
from limite.tela_qualificador import TelaQualificador


class ControladorQualificadores:
    def __init__(self, controlador_sistema) -> None:
        self.__qualificadores = []
        self.__tela_qualificador = TelaQualificador()
        self.__controlador_sistema = controlador_sistema
        self.__qualificadores_escolhidos = None

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def qualificadores_escolhidos(self):
        return self.__qualificadores_escolhidos

    def adicionar_qualificador_escolhido(self, qualificador_escolhido):
        if isinstance(qualificador_escolhido, Qualificador) and \
                qualificador_escolhido not in self.__qualificadores_escolhidos:
            self.__qualificadores_escolhidos.append(qualificador_escolhido)

    def zera_qualificadores_escolhidos(self):
        self.__qualificadores_escolhidos = None

    def criar_qualificador(self):
        dados_qualificador = self.__tela_qualificador.pega_dados_categoria()
        qualificador_valido = True
        count = 0
        while qualificador_valido and count < len(self.__qualificadores):
            if dados_qualificador["título"] == self.__qualificadores[count].titulo and \
                    dados_qualificador["descrição"] == self.__qualificadores[count].descricao:
                self.__tela_qualificador.mostra_mensagem(
                    "Qualificador já cadastrada")
                qualificador_valido = False
            count = count + 1
        if qualificador_valido:
            qualificador = Qualificador(titulo=dados_qualificador['título'],
                                     descricao=dados_qualificador['descrição'])
            self.__qualificadores.append(qualificador)
            self.adicionar_qualificador_escolhido(qualificador)
            self.__controlador_sistema.controlador_qualificadores.abre_tela(self.__qualificadores_escolhidos)

    def abre_tela(self, qualificadores_escolhidos: list = None):
        # print(f"usuario: {self.__controlador_sistema.controlador_usuarios.usuario_logado} |",
        #       f"supermercado: {self.__controlador_sistema.controlador_supermercados.supermercado_escolhido} |",
        #       f"categoria: {self.__controlador_sistema.controlador_categorias.categoria_escolhida} |")
        lista_opcoes = {}
        count = 1
        qualificadores = {}

        if not qualificadores_escolhidos:
            for qualificador in self.__qualificadores:
                lista_opcoes[count] = qualificador
                qualificadores[count] = (
                    qualificador.nome, qualificador.descricao)
        else:
            for qualificador in self.__qualificadores:
                if qualificador not in qualificadores_escolhidos:
                    lista_opcoes[count] = qualificador
                    qualificadores[count] = (
                        qualificador.nome, qualificador.descricao)
        lista_opcoes[len(lista_opcoes)+1] = self.criar_qualificador
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerra_sistema

        while True:
            opcao_escolhida = self.__tela_categoria.tela_opcoes(qualificadores)
            if isinstance(opcao_escolhida, int) and opcao_escolhida in list(range(1, len(qualificadores) + 1)):
                # self.__qualificadores_escolhidos = lista_opcoes[opcao_escolhida]
                self.adicionar_qualificador_escolhido(
                    lista_opcoes[opcao_escolhida])
                self.abre_tela(self.__qualificadores_escolhidos)
            else:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
