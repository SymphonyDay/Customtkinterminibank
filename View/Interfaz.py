import customtkinter
import sys
import os   
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Model.BancoModel import BancoModel
from .sidebar import Sidebar, SidebarSelection

class SelectionInterfaz:
    @staticmethod
    def Balance(interfaz, money):
        # Actualiza la vista mostrando el balance
        for widget in interfaz.content_frame.winfo_children():
            widget.destroy()
        interfaz.nuevo_label = customtkinter.CTkLabel(
            interfaz.content_frame, text=f"Balance ${money}", font=("Arial", 20)
        )
        interfaz.nuevo_label.pack(pady=10)
        interfaz.boton_volver = customtkinter.CTkButton(
            interfaz.content_frame, text="Volver", command=interfaz.crear_interfaz_inicial
        )
        interfaz.boton_volver.pack(pady=10)

    @staticmethod
    def Deposit(interfaz):
        # Muestra la interfaz para ingresar un depósito (solo vista)
        for widget in interfaz.content_frame.winfo_children():
            widget.destroy()
        deposit_label = customtkinter.CTkLabel(
            interfaz.content_frame, text="Enter deposit amount:", font=("Arial", 20)
        )
        deposit_label.pack(pady=10)
        vcmd = (interfaz.root.register(interfaz.only_numbers), '%P')
        interfaz.deposit_entry = customtkinter.CTkEntry(
            interfaz.content_frame, placeholder_text="Deposit amount",
            validate="key", validatecommand=vcmd
        )
        interfaz.deposit_entry.pack(pady=10)
        interfaz.deposit_button = customtkinter.CTkButton(
            interfaz.content_frame, text="Deposit", command=interfaz.process_deposit
        )
        interfaz.deposit_button.pack(pady=10)
        interfaz.boton_volver = customtkinter.CTkButton(
            interfaz.content_frame, text="Volver", command=interfaz.crear_interfaz_inicial
        )
        interfaz.boton_volver.pack(pady=10)

    @staticmethod
    def Withdraw(interfaz):
        # Muestra la interfaz para ingresar un retiro (solo vista)
        for widget in interfaz.content_frame.winfo_children():
            widget.destroy()
        withdraw_label = customtkinter.CTkLabel(
            interfaz.content_frame, text="Enter withdraw amount:", font=("Arial", 20)
        )
        withdraw_label.pack(pady=10)
        vcmd = (interfaz.root.register(interfaz.only_numbers), '%P')
        interfaz.withdraw_entry = customtkinter.CTkEntry(
            interfaz.content_frame, placeholder_text="Withdraw amount",
            validate="key", validatecommand=vcmd
        )
        interfaz.withdraw_entry.pack(pady=10)
        interfaz.withdraw_button = customtkinter.CTkButton(
            interfaz.content_frame, text="Withdraw", command=interfaz.process_withdraw
        )
        interfaz.withdraw_button.pack(pady=10)
        interfaz.boton_volver = customtkinter.CTkButton(
            interfaz.content_frame, text="Volver", command=interfaz.crear_interfaz_inicial
        )
        interfaz.boton_volver.pack(pady=10)

# ---------------------------
# Vista (View) - Interfaz principal
# ---------------------------
class Interfaz:
    def __init__(self, controller):
        self.controller = controller
        self.controller.set_interfaz(self)
        self.selected_option = None  # Guarda la opción seleccionada del sidebar

        # Configuración de la apariencia
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Crear ventana principal
        self.root = customtkinter.CTk()
        self.root.title("Ejemplo de Menú Lateral")
        self.root.geometry("800x500")
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Crear el sidebar (se asume que Sidebar y SidebarSelection están definidos)
        self.sidebar = Sidebar(self.root, update_selection_callback=self.update_selection)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Frame para el contenido principal
        self.content_frame = customtkinter.CTkFrame(self.root)
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # Label inicial para la selección
        self.selection_label = customtkinter.CTkLabel(
            self.content_frame, text="No selection", font=("Arial", 20)
        )
        self.selection_label.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Crear la interfaz inicial
        self.crear_interfaz_inicial()

    def update_selection(self, new_selection):
        self.selected_option = new_selection
        if new_selection == SidebarSelection.Balance:
            print("Balance pressed on Interfaz")
            SelectionInterfaz.Balance(self, self.controller.model.saldo())
        elif new_selection == SidebarSelection.Deposit:
            print("Deposit pressed on Interfaz")
            SelectionInterfaz.Deposit(self)
        elif new_selection == SidebarSelection.Withdraw:
            print("Withdraw pressed on Interfaz")
            SelectionInterfaz.Withdraw(self)
        else:
            print(f"{new_selection.name} pressed on Interfaz")

    def crear_interfaz_inicial(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        self.label_superior = customtkinter.CTkLabel(
            self.content_frame, text="Bienvenido al banco", font=("Arial", 18)
        )
        self.label_superior.pack(pady=10)
        self.entrada = customtkinter.CTkEntry(
            self.content_frame, placeholder_text="Escribe algo aquí y se muestra en consola"
        )
        self.entrada.pack(pady=10)
        self.boton_mostrar = customtkinter.CTkButton(
            self.content_frame, text="Mostrar en Consola", command=self.mostrar_texto
        )
        self.boton_mostrar.pack(pady=5)

    def mostrar_texto(self):
        texto = self.entrada.get()
        seleccion = self.selected_option.name if self.selected_option else "Ninguna"
        print(f"Texto ingresado: {texto}")
        print(f"Selección actual: {seleccion}")

    def only_numbers(self, value):
        if value == "":
            return True
        try:
            float(value)
            return True
        except ValueError:
            return False

    def process_deposit(self):
        amount_str = self.deposit_entry.get()
        if amount_str == "":
            return
        amount = float(amount_str)
        success, result = self.controller.deposit(amount)
        if success:
            SelectionInterfaz.Balance(self, result)
        else:
            self.show_error(result)

    def process_withdraw(self):
        amount_str = self.withdraw_entry.get()
        if amount_str == "":
            return
        amount = float(amount_str)
        success, result = self.controller.withdraw(amount)
        if success:
            SelectionInterfaz.Balance(self, result)
        else:
            self.show_error(result)

    def show_error(self, message):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        error_label = customtkinter.CTkLabel(
            self.content_frame, text=message, font=("Arial", 20), fg_color="red"
        )
        error_label.pack(pady=10)
        boton_volver = customtkinter.CTkButton(
            self.content_frame, text="Volver", command=self.crear_interfaz_inicial
        )
        boton_volver.pack(pady=10)

    def run(self):
        self.root.mainloop()
