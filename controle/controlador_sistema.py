from entidade.supermercado import Supermercado
from limite.tela_sistema import TelaSistema
from controle.controlador_categorias import ControladorCategorias
from controle.controlador_usuarios import ControladorUsuarios
from controle.controlador_precos import ControladorPrecos
from controle.controlador_produtos import ControladorProdutos
from controle.controlador_qualificadores import ControladorQualificadores
from controle.controlador_supermercados import ControladorSupermercados


class ControladorSistema:
    def __init__(self) -> None:
        self.__controlador_categorias = ControladorCategorias(self)
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__controlador_precos = ControladorPrecos()
        self.__controlador_produtos = ControladorProdutos()
        self.__controlador_qualificadores = ControladorQualificadores()
        self.__controlador_supermercados = ControladorSupermercados(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_categorias(self) -> ControladorCategorias:
        return self.__controlador_categorias

    @property
    def controlador_usuarios(self) -> ControladorUsuarios:
        return self.__controlador_usuarios

    @property
    def controlador_precos(self) -> ControladorPrecos:
        return self.__controlador_precos

    @property
    def controlador_produtos(self) -> ControladorProdutos:
        return self.__controlador_produtos

    @property
    def controlador_qualificadores(self) -> ControladorQualificadores:
        return self.__controlador_qualificadores

    @property
    def controlador_supermercados(self) -> ControladorSupermercados:
        return self.__controlador_supermercados

    def inicializa_sistema(self):
        self.abre_tela_usuario()

    def lancar_produto(self):
        self.abre_tela_supermercado()

    def abre_tela_usuario(self):
        self.__controlador_usuarios.abre_tela()

    def abre_tela_supermercado(self):
        self.__controlador_supermercados.abre_tela()

    def abre_tela_categoria(self):
        self.__controlador_categorias.abre_tela()

    def abre_tela_produto(self):
        # self.__controlador_produtos.abre_tela()
        print("self.__controlador_produtos.abre_tela()")

    def buscar_produto(self):
        pass

    def listar_produtos(self):
        self.__controlador_produtos.lista_produto()

    def alterar_produto(self):
        self.__controlador_produtos.abre_tela_altera_produto()

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
        print(f"{self.controlador_usuarios.usuario_logado} |",
              f"{self.controlador_supermercados.supermercado_escolhido} |",
              f"{self.controlador_categorias.categoria_escolhida} |")
        tipo_pessoa_logada = self.__controlador_usuarios.tipo_pessoa_logada()
        if tipo_pessoa_logada == "PessoaFisica":
            self.abre_tela_pessoa_fisica()
        elif tipo_pessoa_logada == "PessoaJuridica":
            supermercado_associado = self.controlador_supermercados.acha_supermercado_por_cnpj(
                self.__controlador_usuarios.usuario_logado.cnpj)
            self.__controlador_supermercados.supermercado_escolhido = supermercado_associado
            self.abre_tela_pessoa_juridica(supermercado_associado)

    def abre_tela_pessoa_fisica(self):
        lista_opcoes = {1: self.lancar_produto, 2: self.buscar_produto,
                        "b": self.voltar, "q": self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_pessoa_fisica()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_pessoa_juridica(self, supermercado_associado: bool = False):
        if supermercado_associado:
            lista_opcoes = {1: self.lancar_produto, 2: self.buscar_produto,
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
