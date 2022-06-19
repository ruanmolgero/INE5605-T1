from entidade.qualificador import Qualificador
from limite.tela_qualificador import TelaQualificador


class ControladorQualificadores:
    def __init__(self, controlador_sistema) -> None:
        self.__qualificadores = []
        self.__tela_qualificador = TelaQualificador()
        self.__controlador_sistema = controlador_sistema
        self.__qualificadores_escolhidos = []

    @property
    def qualificadores(self):
        return self.__qualificadores

    @property
    def qualificadores_escolhidos(self):
        return self.__qualificadores_escolhidos

    def adicionar_qualificador_escolhido(self, qualificador_escolhido):
        if isinstance(qualificador_escolhido, Qualificador) and \
                qualificador_escolhido not in self.__qualificadores_escolhidos:
            self.__qualificadores_escolhidos.append(qualificador_escolhido)
