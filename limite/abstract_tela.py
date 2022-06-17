from abc import ABC, abstractmethod


class AbstractTela(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()

    def __checa_inteiro(self, entrada_lida: str):
        try:
            entrada_lida = int(entrada_lida)
            return entrada_lida
        except ValueError:
            return entrada_lida

    def le_opcao(self, mensagem: str = "", entradas_validas: list = None):
        while True:
            entrada_lida = self.__checa_inteiro(input(mensagem))
            try:
                if entrada_lida not in entradas_validas:
                    raise ValueError
                return entrada_lida
            except ValueError:
                print("Valor inválido, favor digitar novamente.")
                if entradas_validas:
                    print(f"Entradas válidas: {entradas_validas}")

    def mostra_mensagem(self, mensagem: str = ""):
        print(mensagem)
