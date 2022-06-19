from limite.abstract_tela import AbstractTela


class TelaProduto(AbstractTela):
    def __init__(self) -> None:
        super().__init__()

    #TODO:
    def tela_opcoes(self, produtos):
        print("-------- Bem-vindo ao sistema de controle de preço interativo ---------")
        print("Opções:")
        for p in produtos:
            print(f"{p} - {produtos[p][0]}, {produtos[p][1]}")
        print(f"{len(produtos) + 1} - Adicionar Categoria")
        print("b - Voltar")
        print("q - Sair do Sistema")
        opcao = super().le_opcao(mensagem="Escolha a opcao: ",
                                 entradas_validas=(list(range(1, len(produtos) + 1)) + [len(produtos) + 1, "b", "q"]))
        return opcao

    def pega_dados_produto(self):
        dados_produto = {}
        print("-------- DADOS PRODUTO ----------")
        dados_produto["nome"] = input("Nome: ")
        dados_produto["descrição"] = input("Descrição: ")
        return dados_produto
