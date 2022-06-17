from limite.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self) -> None:
        super().__init__()

    def tela_opcoes_pessoa_fisica(self):
        print("Opções:")
        print("1 - Lançar Produto")
        print("2 - Buscar Produto")
        print("b - Voltar")
        print("q - Sair do Sistema")
        opcao = super().le_opcao(mensagem="Escolha a opção: ",
                                 entradas_validas=[1, 2, "b", "q"])
        return opcao

    def tela_opcoes_pessoa_juridica(self, supermercado_associado):
        print("Opções:")
        if supermercado_associado:
            print("1 - Lançar Produto")
            print("2 - Buscar Produto")
            print("3 - Listar Produtos")
            print("4 - Alterar Produto")
            print("b - Voltar")
            print("q - Sair do Sistema")
            opcao = super().le_opcao(mensagem="Escolha a opção: ",
                                     entradas_validas=[1, 2, 3, 4, "b", "q"])
        else:
            print("1 - Cadastrar Supermercado")
            print("b - Voltar")
            print("q - Sair do Sistema")
            opcao = super().le_opcao(mensagem="Escolha a opção: ",
                                     entradas_validas=[1, "b", "q"])
        return opcao
