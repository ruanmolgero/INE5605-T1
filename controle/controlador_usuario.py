from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica
from limite.tela_usuario import TelaUsuario


class ControladorUsuario:
    def __init__(self, controlador_sistema) -> None:
        self.__usuarios = {"pessoas_fisicas": [], "pessoas_juridicas": []}
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
        self.__usuario_logado = None

    @property
    def usuarios(self):
        return self.__usuarios

    @property
    def usuario_logado(self):
        return self.__usuario_logado

    @usuario_logado.setter
    def usuario_logado(self, usuario_logado: PessoaFisica or PessoaJuridica):
        if isinstance(usuario_logado, PessoaFisica) or \
                isinstance(usuario_logado, PessoaJuridica) or \
                usuario_logado is None:
            self.__usuario_logado = usuario_logado

    # def __achar_usuario(self, cpf: str = None, cnpj: str = None):
    #     usuario = None
    #     count = 0
    #     if cpf:
    #         pessoas_fisicas = self.__usuarios['pessoas_fisicas']
    #         while not usuario and count < len(pessoas_fisicas):
    #             if cpf == pessoas_fisicas[count].cpf:
    #                 usuario = pessoas_fisicas[count]
    #             count = count + 1
    #     elif cnpj:
    #         pessoas_juridicas = self.__usuarios['pessoas_juridicas']
    #         while not usuario and count < len(pessoas_juridicas):
    #             if cpf == pessoas_juridicas[count].cpf:
    #                 usuario = pessoas_juridicas[count]
    #             count = count + 1

    def achar_usuario_por_cpf(self, cpf: str = ""):
        usuario = None
        count = 0
        while not usuario and count < len(self.__usuarios['pessoas_fisicas']):
            if cpf == self.__usuarios['pessoas_fisicas'][count].cpf:
                usuario = self.__usuarios['pessoas_fisicas'][count]
            count = count + 1

        return usuario

    def achar_usuario_por_cnpj(self, cnpj: str = ""):
        usuario = None
        count = 0
        while not usuario and count < len(self.__usuarios['pessoas_juridicas']):
            if cnpj == self.__usuarios['pessoas_juridicas'][count].cnpj:
                usuario = self.__usuarios['pessoas_juridicas'][count]
            count = count + 1

        return usuario

    # def __criar_usuario(self, usuario: PessoaFisica or PessoaJuridica):
    #     if isinstance(usuario, PessoaFisica):
    #         usuario_jah_existe = self.achar_usuario_por_cpf(cpf=usuario.cpf)
    #         if not usuario_jah_existe:
    #             self.usuarios["pessoas_fisicas"].append(usuario)
    #         else:
    #             # raise SupermercadoDuplicadoException
    #             pass
    #     else:
    #         usuario_jah_existe = self.achar_usuario_por_cnpj(cnpj=usuario.cnpj)
    #         if not usuario_jah_existe:
    #             self.usuarios["pessoas_juridicas"].append(usuario)
    #         else:
    #             # raise SupermercadoDuplicadoException
    #             pass

    def criar_usuario(self, dados: dict = None):
        if not dados:
            dados_usuario = self.__tela_usuario.pega_dados_usuario()
        else:
            dados_usuario = dados

        # ? ver com o professor se é melhor tratar assim ou com try/except
        if "nome" in dados_usuario and "email" in dados_usuario:
            if "cpf" in dados_usuario:
                usuario = PessoaFisica(nome=dados_usuario["nome"],
                                       email=dados_usuario["email"],
                                       cpf=dados_usuario["cpf"])

                count = 0
                usuario_jah_existe = self.achar_usuario_por_cpf(dados_usuario["cpf"])

                if not usuario_jah_existe:
                    self.__usuarios["pessoas_fisicas"].append(usuario)
                else:
                    self.__tela_usuario.mostra_mensagem("Usuário já cadastrado!")
            elif "cnpj" in dados_usuario:
                usuario = PessoaJuridica(nome=dados_usuario["nome"],
                                         email=dados_usuario["email"],
                                         cnpj=dados_usuario["cnpj"])

                count = 0
                usuario_jah_existe = self.achar_usuario_por_cnpj(dados_usuario["cnpj"])

                if not usuario_jah_existe:
                    self.__usuarios["pessoas_juridicas"].append(usuario)
                else:
                    self.__tela_usuario.mostra_mensagem("Usuário já cadastrado!")

    def realizar_login(self, dados: dict = None):
        if not dados:
            dados_login = self.__tela_usuario.pega_dados_login()
        else:
            dados_login = dados

        # ? ver com o professor se é melhor tratar assim ou com try/except
        if "email" in dados_login:
            if "cpf" in dados_login:
                usuario = self.achar_usuario_por_cpf(dados_login['cpf'])
                if usuario:
                    if usuario.email == dados_login['email']:
                        self.__tela_usuario.mostra_mensagem(f"Seja Bem-Vindo {usuario.nome}")
                        self.__usuario_logado = usuario
                        if not dados:
                            self.__controlador_sistema.abrir_tela()
                    else:
                        self.__tela_usuario.mostra_mensagem("Informações de login incorretas!")
                else:
                    self.__tela_usuario.mostra_mensagem("Informações de login incorretas!")
            if "cnpj" in dados_login:
                usuario = self.achar_usuario_por_cnpj(dados_login['cnpj'])
                if usuario:
                    if usuario.email == dados_login['email']:
                        self.__tela_usuario.mostra_mensagem(f"Seja Bem-Vindo {usuario.nome}")
                        self.__usuario_logado = usuario
                        if not dados:
                            self.__controlador_sistema.abrir_tela()
                    else:
                        self.__tela_usuario.mostra_mensagem("Informações de login incorretas!")
                else:
                    self.__tela_usuario.mostra_mensagem("Informações de login incorretas!")

    # FUNÇÕES PARA TESTE
    # def listar_usuarios_fisicos(self):
    #     usuarios_fisicos = self.usuarios['pessoas_fisicas']

    #     count = 0
    #     for u in usuarios_fisicos:
    #         print(usuarios_fisicos[count])
    #         count += 1

    # def listar_usuarios_juridicos(self):
    #     usuarios_juridicos = self.usuarios['pessoas_juridicas']

    #     count = 0
    #     for u in usuarios_juridicos:
    #         print(usuarios_juridicos[count])
    #         count += 1

    def encerrar_sistema(self):
        exit(0)

    def abrir_tela(self):
        lista_opcoes = {1: self.realizar_login, 2: self.criar_usuario,
                        "q": self.encerrar_sistema}

        while True:
            opcao_selecionada = self.__tela_usuario.tela_opcoes()
            funcao_selecionada = lista_opcoes[opcao_selecionada]
            funcao_selecionada()
