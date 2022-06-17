from entidade.pessoa_juridica import PessoaJuridica


class Supermercado:
    def __init__(self, nome: str, endereco: str, cadastrante) -> None:
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(endereco, str):
            self.__endereco = endereco
        if isinstance(cadastrante, PessoaJuridica):
            self.__cadastrante = cadastrante
        self.__categorias = []

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco) -> None:
        if isinstance(endereco, str):
            self.__endereco = endereco

    @property
    def cadastrante(self) -> str:
        return self.__cadastrante

    @cadastrante.setter
    def cadastrante(self, cadastrante) -> PessoaJuridica:
        if isinstance(cadastrante, str):
            self.__cadastrante = cadastrante

    @property
    def categorias(self) -> list:
        return self.__categorias
