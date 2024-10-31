import tkinter as tk
from tkinter import messagebox, ttk, Toplevel
from DatabaseHandler import DatabaseHandler
from RecordTable import RecordTable

class App(tk.Tk):
    def __init__(self, base_url):
        super().__init__()
        self.title("Registro de Escuela de Baile")
        self.geometry("200x600")
        self.resizable(False, False)

        # Inicializar el manejador de base de datos y la tabla de IDs
        self.db_handler = DatabaseHandler(base_url)
        self.record_table = RecordTable(self)

        # Botón para cargar registros
        self.load_button = tk.Button(self, text="Cargar registros", command=self.load_records)
        self.load_button.pack(pady=5)

        # Botón para seleccionar registro
        self.select_button = tk.Button(self, text="Seleccionar registro", command=self.select_record)
        self.select_button.pack(pady=5)

        # Botón para actualizar la tabla principal
        self.refresh_button = tk.Button(self, text="Actualizar tabla", command=self.load_records)
        self.refresh_button.pack(pady=5)

    def load_records(self):
        """Carga todos los registros de la base de datos y los muestra en la tabla de IDs."""
        records = self.db_handler.get_records()
        self.record_table.populate_table(records)

    def select_record(self):
        """Abre una nueva ventana con la información completa del registro seleccionado."""
        selected_id = self.record_table.get_selected_record()
        if selected_id:
            # Obtener el registro completo usando el ID seleccionado
            records = self.db_handler.get_records()
            record = next((record for record in records if str(record["id"]) == str(selected_id)), None)

            if record:
                # Crear una nueva ventana para mostrar el registro seleccionado
                detail_window = Toplevel(self)
                detail_window.title("Detalles del Registro Seleccionado")
                detail_window.geometry("800x200")
                detail_window.resizable(False, False)

                # Configurar la tabla en la nueva ventana
                detail_table = ttk.Treeview(detail_window, columns=("ID", "Nombre", "Apellido", "Ciudad", "Calle", "Estilo"),
                                            show="headings", style="Custom.Treeview")
                detail_table.heading("ID", text="ID")
                detail_table.heading("Nombre", text="Nombre")
                detail_table.heading("Apellido", text="Apellido")
                detail_table.heading("Ciudad", text="Ciudad")
                detail_table.heading("Calle", text="Calle")
                detail_table.heading("Estilo", text="Estilo de Baile")

                # Centrar los datos en la tabla de detalles
                detail_table.column("ID", anchor="center", width=50)
                detail_table.column("Nombre", anchor="center", width=100)
                detail_table.column("Apellido", anchor="center", width=100)
                detail_table.column("Ciudad", anchor="center", width=100)
                detail_table.column("Calle", anchor="center", width=100)
                detail_table.column("Estilo", anchor="center", width=100)
                detail_table.pack(pady=20, fill=tk.BOTH, expand=True)

                # Insertar el registro en la tabla de detalles
                detail_table.insert("", "end", values=(
                    record["id"], record["nombre"], record["apellido"],
                    record["ciudad"], record["calle"], record["estilo"]
                ))
            else:
                messagebox.showinfo("Información", "No se encontró el registro.")
