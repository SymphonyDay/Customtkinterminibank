class BancoModel:
    def __init__(self, plata):
        self.__plata = plata

    def retirar(self, retirarp):
        if (retirarp <= self.__plata and self.__plata >= 0 and retirarp >= 1):
            self.__plata -= retirarp
        else:
            raise Exception("No puedes retirar plata")

    def saldo(self):
        return self.__plata

    def depositar(self, dinero):
        if (dinero >= 1):
            self.__plata += dinero
        else:
            raise Exception("Error, no has podido depositar dinero")
