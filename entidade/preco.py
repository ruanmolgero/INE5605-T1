from datetime import datetime

from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica


class Preco:
    def __init__(self, valor: float, cadastrante: PessoaFisica or PessoaJuridica) -> None:
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
