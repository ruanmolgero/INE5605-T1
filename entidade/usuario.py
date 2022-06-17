from abc import ABC, abstractmethod


class Usuario(ABC):
    @abstractmethod
    def __init__(self, nome: str, email: str) -> None:
        super().__init__()
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(email, str):
            self.__email = email

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome) -> None:
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email) -> None:
        if isinstance(email, str):
            self.__email = email
