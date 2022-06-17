from entidade.usuario import Usuario


class PessoaJuridica(Usuario):
    def __init__(self, nome: str, email: str, cnpj: str) -> None:
        super().__init__(nome, email)
        if isinstance(cnpj, str):
            self.__cnpj = cnpj

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj) -> None:
        if isinstance(cnpj, str):
            self.__cnpj = cnpj

