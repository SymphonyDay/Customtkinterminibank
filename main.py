from Controller.BancoController import Controller
from Model.BancoModel import BancoModel
from View.Interfaz import Interfaz
if __name__ == "__main__":
    model = BancoModel(1000)  # Balance inicial $1000
    controller = Controller(model)
    app = Interfaz(controller)
    app.run()