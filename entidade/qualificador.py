class Qualificador:
    def __init__(self, titulo: str, descricao: str) -> None:
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo) -> None:
        if isinstance(titulo, str):
            self.__titulo = titulo

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao) -> None:
        if isinstance(descricao, str):
            self.__descricao = descricao
