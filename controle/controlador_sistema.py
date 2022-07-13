from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica
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
        self.abrir_tela_usuario()

    def lancar_produto_pessoa_fisica(self):
        self.controlador_supermercado.abrir_tela()

    def lancar_produto_pessoa_juridica(self):
        self.controlador_categoria.abrir_tela()

    def abrir_tela_usuario(self):
        self.controlador_usuario.abrir_tela()

    def buscar_produto(self):
        pass

    # def listar_produtos(self):
    #     self.controlador_produto_preco.listar_produto()

    # def alterar_produto(self):
    #     self.controlador_produto_preco.abrir_tela_altera_produto()

    def criar_supermercado(self):
        self.controlador_supermercado.criar_supermercado()

    def voltar(self):
        self.controlador_usuario.usuario_logado = None  # desloga usuario
        if self.controlador_supermercado.supermercado_selecionado is not None:
            self.controlador_supermercado.supermercado_selecionado = None
        self.controlador_usuario.abrir_tela()

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        usuario_logado = self.controlador_usuario.usuario_logado
        if isinstance(usuario_logado, PessoaFisica):
            self.abrir_tela_pessoa_fisica()
        elif isinstance(usuario_logado, PessoaJuridica):
            supermercado_associado = self.controlador_supermercado.achar_supermercado_por_cnpj(
                self.controlador_usuario.usuario_logado.cnpj)
            self.controlador_supermercado.supermercado_selecionado = supermercado_associado
            self.abrir_tela_pessoa_juridica(supermercado_associado)

    def abrir_tela_pessoa_fisica(self):
        lista_opcoes = {1: self.lancar_produto_pessoa_fisica, 2: self.buscar_produto,
                        "b": self.voltar, "q": self.encerrar_sistema}

        while True:
            opcao_selecionada = self.__tela_sistema.tela_opcoes_pessoa_fisica()
            funcao_selecionada = lista_opcoes[opcao_selecionada]
            funcao_selecionada()

    def abrir_tela_pessoa_juridica(self, supermercado_associado: bool = False):
        if supermercado_associado:
            lista_opcoes = {1: self.lancar_produto_pessoa_juridica, 2: self.buscar_produto,
                            # 3: self.listar_produtos, 4: self.alterar_produto,
                            "b": self.voltar, "q": self.encerrar_sistema}
        else:
            lista_opcoes = {1: self.criar_supermercado,
                            "b": self.voltar, "q": self.encerrar_sistema}

        while True:
            opcao_selecionada = self.__tela_sistema.tela_opcoes_pessoa_juridica(
                supermercado_associado)
            funcao_selecionada = lista_opcoes[opcao_selecionada]
            funcao_selecionada()
