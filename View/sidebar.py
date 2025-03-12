import customtkinter
from PIL import Image
from enum import Enum

# Definimos un enum para los posibles estados del sidebar
class SidebarSelection(Enum):
    Balance = 1
    Withdraw = 2
    Deposit = 3
    EXIT = 4

class Sidebar(customtkinter.CTkFrame):
    def __init__(self, parent, update_selection_callback=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Callback para actualizar el estado en main
        self.update_selection_callback = update_selection_callback
        # Estado actual (enum)
        self.current_selection = None

        # Atributo para saber si el menú está expandido
        self.expanded = True

        # Ajusta el ancho inicial
        self.sidebar_width_expanded = 200
        self.sidebar_width_collapsed = 60
        self.configure(width=self.sidebar_width_expanded)

        # -----------------------------
        # 1) Definir tamaños de botones
        # -----------------------------
        self.button_width_expanded = 180
        self.button_height_expanded = 40
        self.button_width_collapsed = 40
        self.button_height_collapsed = 40

        # ------------------------------------------
        # 2) Definir dos tamaños de íconos (opcional)
        # ------------------------------------------
        self.icon_size_expanded = (20, 20)
        self.icon_size_collapsed = (15, 15)

        # Carga de íconos en dos tamaños (ajusta rutas e imágenes)
        self.icon_balance_expanded = customtkinter.CTkImage(
            dark_image=Image.open("icons/balance.jpg"), size=self.icon_size_expanded
        )
        self.icon_balance_collapsed = customtkinter.CTkImage(
            dark_image=Image.open("icons/balance.jpg"), size=self.icon_size_collapsed
        )

        self.icon_withdraw_expanded = customtkinter.CTkImage(
            dark_image=Image.open("icons/withdraw.jpg"), size=self.icon_size_expanded
        )
        self.icon_withdraw_collapsed = customtkinter.CTkImage(
            dark_image=Image.open("icons/withdraw.jpg"), size=self.icon_size_collapsed
        )

        self.icon_deposit_expanded = customtkinter.CTkImage(
            dark_image=Image.open("icons/deposit.jpg"), size=self.icon_size_expanded
        )
        self.icon_deposit_collapsed = customtkinter.CTkImage(
            dark_image=Image.open("icons/deposit.jpg"), size=self.icon_size_collapsed
        )

        self.icon_exit_expanded = customtkinter.CTkImage(
            dark_image=Image.open("icons/exit.jpg"), size=self.icon_size_expanded
        )
        self.icon_exit_collapsed = customtkinter.CTkImage(
            dark_image=Image.open("icons/exit.jpg"), size=self.icon_size_collapsed
        )

        # Botón para colapsar/expandir
        self.toggle_button = customtkinter.CTkButton(
            self, 
            text="<<", 
            width=self.button_width_expanded, 
            height=self.button_height_expanded,
            anchor="w",
            border_spacing=10,
            command=self.toggle_sidebar
        )
        self.toggle_button.pack(pady=5, padx=10, fill="x")

        # Crear los botones en modo "expandido"
        self.btn_balance = customtkinter.CTkButton(
            self, 
            text="Balance", 
            image=self.icon_balance_expanded, 
            compound="left",
            width=self.button_width_expanded, 
            height=self.button_height_expanded,
            anchor="w",
            border_spacing=10,
            command=self.balance_action
        )
        self.btn_balance.pack(pady=5, padx=10, fill="x")

        self.btn_withdraw = customtkinter.CTkButton(
            self, 
            text="Withdraw", 
            image=self.icon_withdraw_expanded, 
            compound="left",
            width=self.button_width_expanded, 
            height=self.button_height_expanded,
            anchor="w",
            border_spacing=10,
            command=self.withdraw_action
        )
        self.btn_withdraw.pack(pady=5, padx=10, fill="x")

        self.btn_deposit = customtkinter.CTkButton(
            self, 
            text="Deposit", 
            image=self.icon_deposit_expanded, 
            compound="left",
            width=self.button_width_expanded, 
            height=self.button_height_expanded,
            anchor="w",
            border_spacing=10,
            command=self.deposit_action
        )
        self.btn_deposit.pack(pady=5, padx=10, fill="x")

        self.btn_exit = customtkinter.CTkButton(
            self, 
            text="Exit", 
            image=self.icon_exit_expanded, 
            compound="left",
            width=self.button_width_expanded, 
            height=self.button_height_expanded,
            anchor="w",
            border_spacing=10,
            command=self.exit_action
        )
        self.btn_exit.pack(pady=5, padx=10, fill="x")

    def toggle_sidebar(self):
        """Expande o colapsa el menú lateral."""
        if self.expanded:
            # Colapsar
            self.configure(width=self.sidebar_width_collapsed)
            self.toggle_button.configure(text=">>")

            # Quitar texto y reducir botones
            self.btn_balance.configure(
                text="", 
                width=self.button_width_collapsed, 
                height=self.button_height_collapsed,
                image=self.icon_balance_collapsed
            )
            self.btn_withdraw.configure(
                text="", 
                width=self.button_width_collapsed, 
                height=self.button_height_collapsed,
                image=self.icon_withdraw_collapsed
            )
            self.btn_deposit.configure(
                text="", 
                width=self.button_width_collapsed, 
                height=self.button_height_collapsed,
                image=self.icon_deposit_collapsed
            )
            self.btn_exit.configure(
                text="", 
                width=self.button_width_collapsed, 
                height=self.button_height_collapsed,
                image=self.icon_exit_collapsed
            )
            self.toggle_button.configure(
                text=">>",
                width=self.button_width_collapsed, 
                height=self.button_height_collapsed
            )

            self.expanded = False
        else:
            # Expandir
            self.configure(width=self.sidebar_width_expanded)
            self.toggle_button.configure(text="<<")

            # Restaurar texto y tamaño de botones
            self.btn_balance.configure(
                text="Balance", 
                width=self.button_width_expanded, 
                height=self.button_height_expanded,
                image=self.icon_balance_expanded
            )
            self.btn_withdraw.configure(
                text="Withdraw", 
                width=self.button_width_expanded, 
                height=self.button_height_expanded,
                image=self.icon_withdraw_expanded
            )
            self.btn_deposit.configure(
                text="Deposit", 
                width=self.button_width_expanded, 
                height=self.button_height_expanded,
                image=self.icon_deposit_expanded
            )
            self.btn_exit.configure(
                text="Exit", 
                width=self.button_width_expanded, 
                height=self.button_height_expanded,
                image=self.icon_exit_expanded
            )
            self.toggle_button.configure(
                text="<<",
                width=self.button_width_expanded, 
                height=self.button_height_expanded
            )

            self.expanded = True

    # Métodos de acción que actualizan el estado (enum)
    def balance_action(self):
        self.current_selection = SidebarSelection.Balance
        if self.update_selection_callback and callable(self.update_selection_callback):
            self.update_selection_callback(self.current_selection)
        print("Balance pressed, selection =", self.current_selection)

    def withdraw_action(self):
        self.current_selection = SidebarSelection.Withdraw
        if self.update_selection_callback and callable(self.update_selection_callback):
            self.update_selection_callback(self.current_selection)
        print("Withdraw pressed, selection =", self.current_selection)

    def deposit_action(self):
        self.current_selection = SidebarSelection.Deposit
        if self.update_selection_callback and callable(self.update_selection_callback):
            self.update_selection_callback(self.current_selection)
        print("Deposit pressed, selection =", self.current_selection)

    def exit_action(self):
        self.current_selection = SidebarSelection.EXIT
        if self.update_selection_callback and callable(self.update_selection_callback):
            self.update_selection_callback(self.current_selection)
        print("Exit pressed, selection =", self.current_selection)
