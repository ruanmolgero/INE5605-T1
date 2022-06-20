from entidade import usuario
from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica
from limite.tela_usuario import TelaUsuario


class ControladorUsuarios:
    def __init__(self, controlador_sistema) -> None:
        self.__usuarios = {"pessoas_fisicas": [], "pessoas_juridicas": []}
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
        self.__usuario_logado = None

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, usuario_logado):
        if isinstance(usuario_logado, PessoaFisica) or isinstance(usuario_logado, PessoaJuridica) or usuario_logado is None:
            self.__usuario_logado = usuario_logado

    def tipo_pessoa_logada(self):
        tipo_pessoa_logada = None
        if isinstance(self.__usuario_logado, PessoaFisica):
            tipo_pessoa_logada = "PessoaFisica"
        elif isinstance(self.__usuario_logado, PessoaJuridica):
            tipo_pessoa_logada = "PessoaJuridica"

        return tipo_pessoa_logada

    def acha_usuario_por_cpf(self, cpf: str = ""):
        usuario = None
        count = 0
        while not usuario and count < len(self.__usuarios['pessoas_fisicas']):
            if cpf == self.__usuarios['pessoas_fisicas'][count].cpf:
                usuario = self.__usuarios['pessoas_fisicas'][count]
            count = count + 1

        return usuario

    def acha_usuario_por_cnpj(self, cnpj: str = ""):
        usuario = None
        count = 0
        while not usuario and count < len(self.__usuarios['pessoas_juridicas']):
            if cnpj == self.__usuarios['pessoas_juridicas'][count].cnpj:
                usuario = self.__usuarios['pessoas_juridicas'][count]
            count = count + 1

        return usuario

    def realiza_login(self):
        dados_login = self.__tela_usuario.pega_dados_login()
        if "cpf" in dados_login:
            usuario = self.acha_usuario_por_cpf(dados_login['cpf'])
            if usuario:
                if usuario.email == dados_login["email"]:
                    self.__tela_usuario.mostra_mensagem(
                        f"Seja Bem-Vindo {usuario.nome}")
                    self.__usuario_logado = usuario
                    self.__controlador_sistema.abre_tela()
                else:
                    self.__tela_usuario.mostra_mensagem(
                        "Informações de login incorretas!")
            else:
                self.__tela_usuario.mostra_mensagem(
                    "Informações de login incorretas!")
        if "cnpj" in dados_login:

            usuario = self.acha_usuario_por_cnpj(dados_login['cnpj'])
            if usuario:
                if usuario.email == dados_login["email"]:
                    self.__tela_usuario.mostra_mensagem(
                        f"Seja Bem-Vindo {usuario.nome}")
                    self.__usuario_logado = usuario
                    self.__controlador_sistema.abre_tela()
                else:
                    self.__tela_usuario.mostra_mensagem(
                        "Informações de login incorretas!")
            else:
                self.__tela_usuario.mostra_mensagem(
                    "Informações de login incorretas!")

    def incluir_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        if "cpf" in dados_usuario:
            usuario = PessoaFisica(nome=dados_usuario["nome"],
                                   email=dados_usuario["email"],
                                   cpf=dados_usuario["cpf"])

            count = 0
            usuario_valido = True
            while usuario_valido and count < len(self.__usuarios['pessoas_fisicas']):
                if dados_usuario["email"] == self.__usuarios['pessoas_fisicas'][count].email or \
                        dados_usuario["cpf"] == self.__usuarios['pessoas_fisicas'][count].cpf:
                    usuario_valido = False
                count = count + 1

            if usuario_valido:
                self.__usuarios["pessoas_fisicas"].append(usuario)
                print(self.__usuarios)
            else:
                self.__tela_usuario.mostra_mensagem("Usuário já cadastrado!")
        elif "cnpj" in dados_usuario:
            usuario = PessoaJuridica(nome=dados_usuario["nome"],
                                     email=dados_usuario["email"],
                                     cnpj=dados_usuario["cnpj"])

            count = 0
            usuario_valido = True
            while usuario_valido and count < len(self.__usuarios['pessoas_juridicas']):
                if dados_usuario["email"] == self.__usuarios['pessoas_juridicas'][count].email or \
                        dados_usuario["cnpj"] == self.__usuarios['pessoas_juridicas'][count].cnpj:
                    usuario_valido = False
                count = count + 1

            if usuario_valido:
                self.__usuarios["pessoas_juridicas"].append(usuario)
                print(self.__usuarios)
            else:
                self.__tela_usuario.mostra_mensagem("Usuário já cadastrado!")

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.realiza_login, 2: self.incluir_usuario,
                        "q": self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_usuario.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
