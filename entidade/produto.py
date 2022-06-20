from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica
from entidade.qualificador import Qualificador
from entidade.preco import Preco


class Produto:
    def __init__(self, nome: str, descricao: str,
                 qualificadores: list) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(qualificadores, list):
            self.__qualificadores = qualificadores
        self.__precos = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def qualificadores(self) -> Qualificador:
        return self.__qualificadores

    @property
    def precos(self) -> Preco:
        return self.__precos
