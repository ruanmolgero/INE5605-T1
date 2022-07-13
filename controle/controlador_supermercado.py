from entidade.categoria import Categoria
from entidade.supermercado import Supermercado
from limite.tela_supermercado import TelaSupermercado


class ControladorSupermercado:
    def __init__(self, controlador_sistema) -> None:
        self.__supermercados = []
        self.__tela_supermercado = TelaSupermercado()
        self.__controlador_sistema = controlador_sistema
        self.__supermercado_selecionado = None

    @property
    def supermercados(self):
        return self.__supermercados

    @property
    def supermercado_selecionado(self):
        return self.__supermercado_selecionado

    @supermercado_selecionado.setter
    def supermercado_selecionado(self, supermercado_selecionado):
        if isinstance(supermercado_selecionado, Supermercado) or supermercado_selecionado is None:
            self.__supermercado_selecionado = supermercado_selecionado

    def achar_supermercado_por_cnpj(self, cnpj: str):
        supermercado = None
        if isinstance(cnpj, str):
            for s in self.supermercados:
                if cnpj == s.cadastrante.cnpj:
                    supermercado = s

        return supermercado

    def adicionar_categoria_a_supermercado(self, supermercado: Supermercado, categoria: Categoria) -> None:
        if categoria not in supermercado.categorias:
            supermercado.categorias.append(categoria)

    def criar_supermercado(self, dados: dict = None):
        if not dados:
            dados_supermercado = self.__tela_supermercado.pega_dados_supermercado()
        else:
            dados_supermercado = dados

        supermercado = Supermercado(nome=dados_supermercado['nome'],
                                    endereco=dados_supermercado['endereço'],
                                    cadastrante=self.__controlador_sistema.controlador_usuario.usuario_logado)
        self.supermercados.append(supermercado)
        self.supermercado_selecionado = supermercado
        if not dados:
            self.__controlador_sistema.abrir_tela()

    # Métodos que apenas copiei do código antigo

    def voltar(self):
        if self.__supermercado_selecionado:  # True caso seja pessoa juridica
            self.__supermercado_selecionado = None
        self.__controlador_sistema.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        lista_opcoes = {}
        count = 1
        supermercados = {}

        for supermercado in self.__supermercados:
            lista_opcoes[count] = supermercado
            supermercados[count] = (supermercado.nome, supermercado.endereco)
        lista_opcoes["b"] = self.voltar
        lista_opcoes["q"] = self.encerrar_sistema

        while True:
            opcao_selecionada = self.__tela_supermercado.tela_opcoes(
                supermercados)
            if isinstance(opcao_selecionada, int):
                self.__supermercado_selecionado = lista_opcoes[opcao_selecionada]
                self.__controlador_sistema.controlador_categoria.abrir_tela()
            else:
                funcao_selecionada = lista_opcoes[opcao_selecionada]
                funcao_selecionada()
