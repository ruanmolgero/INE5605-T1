from limite.abstract_tela import AbstractTela


class TelaProduto(AbstractTela):
    def __init__(self) -> None:
        super().__init__()

    #TODO: colocar qualificadores
    def tela_opcoes(self, produtos):
        print("-------- PRODUTOS ---------")
        print("Produtos existentes:")
        if produtos != {}:
            for p in produtos:
                print(f"{p} - {produtos[p][0]}: {produtos[p][1]}")
            # for q in
        else:
            print("Nenhum")
            print("-----------------------------")
        print("Outras opções:")
        print(f"{len(produtos) + 1} - Adicionar Produto")
        print("b - Voltar")
        print("q - Sair do Sistema")
        opcao = super().le_opcao(mensagem="Escolha a opcao: ",
                                 entradas_validas=(list(range(1, len(produtos) + 1)) + [len(produtos) + 1, "b", "q"]))
        return opcao

    def pega_dados_produto(self):
        dados_produto = {}
        print("-------- DADOS PRODUTO ----------")
        dados_produto["nome"] = input("Nome: ")
        dados_produto["descricao"] = input("Descrição: ")
        return dados_produto

    #TODO: tratamento float
    def pega_valor_produto(self):
        print("-------- PREÇO ----------")
        while True:
            try:
                valor = float(input("Preco: "))
                return valor
            except ValueError:
                print("Valor inválido, favor digitar um valor no formato: xx.xx.")
