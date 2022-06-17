from limite.abstract_tela import AbstractTela


class TelaUsuario(AbstractTela):
    def __init__(self) -> None:
        super().__init__()

    def tela_opcoes(self):
        print("-------- Bem-vindo ao sistema de controle de preço interativo ---------")
        print("Opções:")
        print("1 - Logar no sistema")
        print("2 - Criar Usuário")
        print("q - Sair do Sistema")
        opcao = super().le_opcao(mensagem="Escolha a opcao: ",
                                 entradas_validas=[1, 2, "q"])
        return opcao

    def pega_dados_usuario(self):
        dados_usuario = {}
        print("-------- DADOS USUARIO ----------")
        dados_usuario["nome"] = input("Nome: ")
        dados_usuario["email"] = input("Email: ")
        print("Pessoa Física ou Jurídica")
        print("1 - Pessoa Física")
        print("2 - Pessoa Jurídica")
        opcao = super().le_opcao(mensagem="Escolha a opção: ",
                                 entradas_validas=[1, 2])
        if opcao == 1:
            dados_usuario["cpf"] = input("CPF: ")
        elif opcao == 2:
            dados_usuario["cnpj"] = input("CNPJ: ")

        return dados_usuario

    def pega_dados_login(self):
        dados_login = {}
        print("-------- DADOS LOGIN ----------")
        dados_login["email"] = input("Email: ")
        print("Pessoa Física ou Jurídica")
        print("1 - Pessoa Física")
        print("2 - Pessoa Jurídica")
        opcao = super().le_opcao(mensagem="Escolha a opção: ",
                                 entradas_validas=[1, 2])
        if opcao == 1:
            dados_login["cpf"] = input("CPF: ")
        elif opcao == 2:
            dados_login["cnpj"] = input("CNPJ: ")

        return dados_login
