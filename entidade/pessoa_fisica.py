from entidade.usuario import Usuario


class PessoaFisica(Usuario):
    def __init__(self, nome: str, email: str, cpf: str) -> None:
        super().__init__(nome, email)
        if isinstance(cpf, str):
            self.__cpf = cpf

    @property
    def cpf(self) -> str:
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf) -> None:
        if isinstance(cpf, str):
            self.__cpf = cpf
