from entidade.pessoa_fisica import PessoaFisica
from entidade.pessoa_juridica import PessoaJuridica
from entidade.qualificador import Qualificador
from entidade.preco import Preco


class Produto:
    def __init__(self, nome: str, descricao: str,
                 qualificador: Qualificador, valor: float, cadastrante: PessoaFisica or PessoaJuridica) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(descricao, str):
            self.__descricao = descricao
        # if isinstance(qualificador, Qualificador):
        self.__qualificadores = []
        if isinstance(valor, float):
            self.__preco = Preco(valor=valor)
        if isinstance(cadastrante, PessoaFisica) or isinstance(cadastrante, PessoaJuridica):
            self.__cadastrante = cadastrante

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
    def qualificador(self) -> Qualificador:
        return self.__qualificador

    @qualificador.setter
    def qualificador(self, qualificador: Qualificador):
        if isinstance(qualificador, Qualificador):
            self.__qualificador = qualificador

    @property
    def preco(self) -> Preco:
        return self.__preco

    @preco.setter
    def preco(self, preco: Preco):
        if isinstance(preco, Preco):
            self.__preco = preco

    @property
    def cadastrante(self):
        return self.__cadastrante

    @cadastrante.setter
    def cadastrante(self, cadastrante):
        if isinstance(cadastrante, PessoaFisica) or isinstance(cadastrante, PessoaJuridica):
            self.__cadastrante = cadastrante
