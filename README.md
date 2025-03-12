# 💰 CustomTkinterMiniBank  

**Un mini banco con interfaz gráfica usando CustomTkinter y el patrón MVC.**  

---

## 📌 Descripción  

Este proyecto implementa el patrón **Modelo-Vista-Controlador (MVC)** utilizando **CustomTkinter** en Python.  
📁 La estructura principal está dividida en tres carpetas:  

- **`Controller/`** → Controla la lógica y la interacción con la interfaz.  
- **`Model/`** → Maneja los datos y las operaciones bancarias.  
- **`View/`** → Contiene la interfaz gráfica con **CustomTkinter**.  

📌 **`Interfaz.py`** es el punto de entrada y utiliza métodos del `Controller` para gestionar la UI y las operaciones del dinero.  

---

## 🏗️ Arquitectura del Proyecto  

```bash
CustomTkinterMiniBank/
│── Controller/
│   ├── controlador.py  # Maneja la lógica de negocio
│
│── Model/
│   ├── modelo.py  # Gestiona los datos y transacciones
│
│── View/
│   ├── interfaz.py  # Contiene la interfaz gráfica (CustomTkinter)
│
└── main.py  # Punto de entrada del programa
