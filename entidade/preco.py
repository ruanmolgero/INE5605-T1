from datetime import datetime


class Preco:
    def __init__(self, valor: float) -> None:
        if isinstance(valor, float):
            self.__valor = valor
        self.__data = datetime.now()
        self.__contador = 1

    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, data) -> None:
        if isinstance(data, datetime):
            self.__data = data

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor) -> None:
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def contador(self) -> int:
        return self.__contador

    @contador.setter
    def contador(self, contador) -> None:
        if isinstance(contador, int):
            self.__contador = contador
