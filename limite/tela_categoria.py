from limite.abstract_tela import AbstractTela


class TelaCategoria(AbstractTela):
    def __init__(self) -> None:
        super().__init__()

    def tela_opcoes(self, categorias):
        print("-------- CATEGORIAS ---------")
        print("Categorias existentes:")
        if categorias != {}:
            for c in categorias:
                print(f"{c} - {categorias[c][0]}: {categorias[c][1]}")
        else:
            print("Nenhuma")
            print("-----------------------------")
        print("Outras opções:")
        print(f"{len(categorias) + 1} - Adicionar Categoria")
        print("b - Voltar")
        print("q - Sair do Sistema")
        opcao = super().le_opcao(mensagem="Escolha a opcao: ",
                                 entradas_validas=(list(range(1, len(categorias) + 1)) + [len(categorias) + 1, "b", "q"]))
        return opcao

    def pega_dados_categoria(self):
        dados_categoria = {}
        print("-------- DADOS CATEGORIA ----------")
        dados_categoria["nome"] = input("Nome: ")
        dados_categoria["descricao"] = input("Descrição: ")
        return dados_categoria
