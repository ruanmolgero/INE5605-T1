from limite.abstract_tela import AbstractTela

class TelaQualificador(AbstractTela):
    def __init__(self) -> None:
        super().__init__()

    def tela_opcoes(self, qualificadores):
        print("-------- QUALIFICADORES ---------")
        print("Qualificadores existentes:")
        if qualificadores != {}:
            for q in qualificadores:
                print(f"{q} - {qualificadores[q][0]}: {qualificadores[q][1]}")
        else:
            print("Nenhum")
            print("-----------------------------")
        print("Outras opções:")
        print(f"{len(qualificadores) + 1} - Adicionar Qualificador")
        print("c - Continuar")
        print("b - Voltar")
        print("q - Sair do Sistema")
        opcao = super().le_opcao(mensagem="Escolha a opcao: ",
                                 entradas_validas=(list(range(1, len(qualificadores) + 1)) + [len(qualificadores) + 1, "c", "b", "q"]))
        return opcao

    def pega_dados_qualificador(self):
        dados_qualificador = {}
        print("-------- DADOS QUALIFICADOR ----------")
        dados_qualificador["título"] = input("Título: ")
        dados_qualificador["descrição"] = input("Descrição: ")
        return dados_qualificador