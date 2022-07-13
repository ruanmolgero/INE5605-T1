from datetime import datetime

from entidade.usuario import Usuario


class Preco:
    # def __init__(self, valor: float, cadastrante: Usuario) -> None:
    def __init__(self, valor: float) -> None:
        if isinstance(valor, float):
            self.__valor = valor
        self.__cadastrantes = []
        self.__data = datetime.now().date()

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor) -> None:
        if isinstance(valor, float):
            self.__valor = valor

    @property
    def cadastrantes(self):
        return self.__cadastrantes

    @property
    def data(self) -> datetime:
        return self.__data

    @data.setter
    def data(self, data) -> None:
        if isinstance(data, datetime):
            self.__data = data

    @property
    def contador(self) -> int:
        return len(self.__cadastrantes)
