from reloj_base import RelojBase

class Reloj24h(RelojBase):
    def __init__(self, hora, minutos, segundos):
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def mostrar(self):
        return f"{self.__hora:02d}:{self.__minutos:02d}:{self.__segundos:02d}"

    def adelantar_minuto(self):
        self.__minutos += 1
        if self.__minutos >= 60:
            self.__minutos = 0
            self.__hora += 1
            if self.__hora >= 24:
                self.__hora = 0

    def actualizar_hora(self, h, m, s):
        self.__hora = h
        self.__minutos = m
        self.__segundos = s

    def es_igual(self, otro):
        return self.mostrar() == otro.mostrar()
