from reloj_24h import Reloj24h

class RelojBuilder:
    def __init__(self):
        self._hora = 0
        self._minutos = 0
        self._segundos = 0

    def con_hora(self, hora):
        self._hora = hora
        return self

    def con_minutos(self, minutos):
        self._minutos = minutos
        return self

    def con_segundos(self, segundos):
        self._segundos = segundos
        return self

    def construir(self):
        return Reloj24h(self._hora, self._minutos, self._segundos)
