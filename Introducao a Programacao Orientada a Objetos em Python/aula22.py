# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.

from abc import ABC, ABCMeta, abstractmethod

class Log(ABC): # Pode ser também class Log(ABCMeta):
    
    @abstractmethod
    def _log(self, msg): # Método abstrato
        ...
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogPrintMixin(Log):
    def _log(self, msg): # método log implementado e definido
        print(f'{msg} ({self.__class__.__name__})')

# l = Log() # class Log não pode ser instanciada, ser for teremos uma mensagem de error:
# Can't instantiate abstract class Log without an implementation for abstract method '_log'

l = LogPrintMixin()

l.log_error('Oi')