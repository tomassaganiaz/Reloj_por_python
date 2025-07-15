from abc import ABC, abstractmethod

class RelojBase(ABC):
    @abstractmethod
    def mostrar(self):
        """Devuelve la representación de la hora en formato string."""
        pass

    @abstractmethod
    def adelantar_minuto(self):
        """Adelanta el reloj un minuto."""
        pass

    @abstractmethod
    def actualizar_hora(self, h, m, s):
        """Actualiza la hora del reloj."""
        pass

    @abstractmethod
    def es_igual(self, otro):
        """Compara con otro reloj si las horas son iguales."""
        pass
