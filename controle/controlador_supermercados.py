from entidade.supermercado import Supermercado
from limite.tela_supermercado import TelaSupermercado


class ControladorSupermercados:
    def __init__(self, controlador_sistema) -> None:
        self.__supermercados = []
        self.__tela_supermercado = TelaSupermercado()
        self.__controlador_sistema = controlador_sistema
        self.__supermercado_escolhido = None

    @property
    def supermercados(self):
        return self.__supermercados

    @property
    def supermercado_escolhido(self):
        return self.__supermercado_escolhido

    @supermercado_escolhido.setter
    def supermercado_escolhido(self, supermercado_escolhido):
        if isinstance(supermercado_escolhido, Supermercado) or supermercado_escolhido is None:
            self.__supermercado_escolhido = supermercado_escolhido

    def acha_supermercado_por_cnpj(self, cnpj: str) -> Supermercado:
        supermercado = None
        for s in self.__supermercados:
            if cnpj == s.cadastrante.cnpj:
                supermercado = s

        return supermercado

    def criar_supermercado(self):
        dados_supermercado = self.__tela_supermercado.pega_dados_supermercado()
        supermercado = Supermercado(nome=dados_supermercado['nome'],
                                    endereco=dados_supermercado['endereço'],
                                    cadastrante=self.__controlador_sistema.controlador_usuarios.usuario_logado)
        self.__supermercados.append(supermercado)
        self.__supermercado_escolhido = supermercado
        self.__controlador_sistema.abre_tela()

    def incluir_categoria_ao_supermercado_escolhido(self, categoria):
        if categoria not in self.__supermercado_escolhido.categorias:
            self.__supermercado_escolhido.categorias.append(categoria)

    def voltar(self):
        if self.__supermercado_escolhido:  # True caso seja pessoa juridica
            self.__supermercado_escolhido = None
        self.__controlador_sistema.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {}
        count = 1
        supermercados = {}

        for supermercado in self.__supermercados:
            lista_opcoes[count] = supermercado
            supermercados[count] = (supermercado.nome, supermercado.endereco)
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerra_sistema

        while True:
            opcao_escolhida = self.__tela_supermercado.tela_opcoes(
                supermercados)
            if isinstance(opcao_escolhida, int):
                self.__supermercado_escolhido = lista_opcoes[opcao_escolhida]
                self.__controlador_sistema.controlador_categorias.abre_tela()
            else:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()
