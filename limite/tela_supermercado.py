from limite.abstract_tela import AbstractTela


class TelaSupermercado(AbstractTela):
    def __init__(self) -> None:
        super().__init__()

    def tela_opcoes(self, supermercados):
        print("-------- SUPERMERCADOS ---------")
        print("Supermercados existentes:")
        if supermercados != {}:
            for s in supermercados:
                print(f"{s} - {supermercados[s][0]}: {supermercados[s][1]}")
        else:
            print("Nenhum")
            print("-----------------------------")
        print("Outras opções:")
        print("b - Voltar")
        print("q - Sair do Sistema")
        print("-----------------------------")
        opcao = super().le_opcao(mensagem="Escolha a opcao: ",
                                 entradas_validas=(list(range(1, len(supermercados) + 1)) + ["b", "q"]))
        return opcao

    def pega_dados_supermercado(self):
        dados_supermercado = {}
        print("-------- DADOS SUPERMERCADO ----------")
        dados_supermercado["nome"] = input("Nome: ")
        dados_supermercado["endereço"] = input("Endereço: ")
        return dados_supermercado