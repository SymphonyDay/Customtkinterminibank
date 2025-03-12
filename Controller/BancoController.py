import os
import sys

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Model.BancoModel import BancoModel
from View.Interfaz import Interfaz
class Controller:
    def __init__(self, model):
        self.model = model
        self.interfaz = None

    def set_interfaz(self, interfaz):
        self.interfaz = interfaz

    def deposit(self, amount):
        try:
            self.model.depositar(amount)
            return True, self.model.saldo()
        except Exception as e:
            return False, str(e)

    def withdraw(self, amount):
        try:
            self.model.retirar(amount)
            return True, self.model.saldo()
        except Exception as e:
            return False, str(e)
