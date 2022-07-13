from limite.tela_sistema import TelaSistema
from controle.controlador_categoria import ControladorCategoria
from controle.controlador_usuario import ControladorUsuario
from controle.controlador_produto_preco import ControladorProdutoPreco
from controle.controlador_qualificador import ControladorQualificador
from controle.controlador_supermercado import ControladorSupermercado


class ControladorSistema:
    def __init__(self) -> None:
        self.__controlador_categoria = ControladorCategoria(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_produto_preco = ControladorProdutoPreco(self)
        self.__controlador_qualificador = ControladorQualificador(self)
        self.__controlador_supermercado = ControladorSupermercado(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_categoria(self) -> ControladorCategoria:
        return self.__controlador_categoria

    @property
    def controlador_usuario(self) -> ControladorUsuario:
        return self.__controlador_usuario

    @property
    def controlador_produto_preco(self) -> ControladorProdutoPreco:
        return self.__controlador_produto_preco

    @property
    def controlador_qualificador(self) -> ControladorQualificador:
        return self.__controlador_qualificador

    @property
    def controlador_supermercado(self) -> ControladorSupermercado:
        return self.__controlador_supermercado

    def inicializa_sistema(self):
        self.abre_tela_usuario()

    def lancar_produto_pessoa_fisica(self):
        self.__controlador_supermercados.abre_tela()

    def lancar_produto_pessoa_juridica(self):
        self.__controlador_categorias.abre_tela()

    def abre_tela_usuario(self):
        self.__controlador_usuarios.abre_tela()

    def buscar_produto(self):
        pass

    def listar_produtos(self):
        self.__controlador_produtos_e_precos.lista_produto()

    def alterar_produto(self):
        self.__controlador_produtos_e_precos.abre_tela_altera_produto()

    def criar_supermercado(self):
        self.__controlador_supermercados.criar_supermercado()

    def voltar(self):
        self.__controlador_usuarios.usuario_logado = None  # desloga usuario
        if self.__controlador_supermercados.supermercado_escolhido is not None:
            self.__controlador_supermercados.supermercado_escolhido = None
        self.__controlador_usuarios.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        tipo_pessoa_logada = self.__controlador_usuarios.tipo_pessoa_logada()
        if tipo_pessoa_logada == "PessoaFisica":
            self.abre_tela_pessoa_fisica()
        elif tipo_pessoa_logada == "PessoaJuridica":
            supermercado_associado = self.controlador_supermercados.acha_supermercado_por_cnpj(
                self.__controlador_usuarios.usuario_logado.cnpj)
            self.__controlador_supermercados.supermercado_escolhido = supermercado_associado
            self.abre_tela_pessoa_juridica(supermercado_associado)

    def abre_tela_pessoa_fisica(self):
        lista_opcoes = {1: self.lancar_produto_pessoa_fisica, 2: self.buscar_produto,
                        "b": self.voltar, "q": self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_pessoa_fisica()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_pessoa_juridica(self, supermercado_associado: bool = False):
        if supermercado_associado:
            lista_opcoes = {1: self.lancar_produto_pessoa_juridica, 2: self.buscar_produto,
                            3: self.listar_produtos, 4: self.alterar_produto,
                            "b": self.voltar, "q": self.encerra_sistema}
        else:
            lista_opcoes = {1: self.criar_supermercado,
                            "b": self.voltar, "q": self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_pessoa_juridica(
                supermercado_associado)
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
