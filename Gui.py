import tkinter as tk
from tkinter import messagebox, ttk
from DatabaseHandler import DatabaseHandler
from RecordTable import RecordTable

# Clase principal de la aplicación
class App(tk.Tk):
    def __init__(self, base_url):
        super().__init__()
        self.title("Registro de Escuela de Baile")
        self.geometry("700x500")
        self.resizable(False, False)

        # Inicializar el manejador de base de datos y la tabla
        self.db_handler = DatabaseHandler(base_url)
        self.record_table = RecordTable(self)
        self.select_window = None  # Variable para la ventana de selección

        # Botones de la interfaz
        self.load_button = tk.Button(self, text="Cargar registros", command=self.load_records)
        self.load_button.pack(pady=5)

        self.select_button = tk.Button(self, text="Seleccionar registro", command=self.show_selected_record)
        self.select_button.pack(pady=5)

        self.refresh_button = tk.Button(self, text="Actualizar Tabla", command=self.load_records)
        self.refresh_button.pack(pady=5)

    def load_records(self):
        """Carga todos los registros de la base de datos y los muestra en la tabla."""
        records = self.db_handler.get_records()
        self.record_table.populate_table(records)

    def show_selected_record(self):
        """Muestra el registro seleccionado en una ventana secundaria en formato de tabla."""
        # Obtener el ID seleccionado en la tabla principal
        selected_id = self.record_table.get_selected_record_id()
        if not selected_id:
            return  # Salir si no se seleccionó ningún ID

        # Cerrar la ventana secundaria anterior si existe
        if self.select_window is not None and self.select_window.winfo_exists():
            self.select_window.destroy()

        # Crear una nueva ventana secundaria
        self.select_window = tk.Toplevel(self)
        self.select_window.title("Detalle del Registro Seleccionado")
        self.select_window.geometry("400x200")

        # Obtener el registro completo utilizando el ID seleccionado
        records = self.db_handler.get_records()
        selected_record = next((record for record in records if record["id"] == str(selected_id)), None)

        # Si el registro existe, mostrarlo en la tabla de la ventana secundaria
        if selected_record:
            # Crear tabla para mostrar detalles del registro seleccionado
            detail_table = ttk.Treeview(self.select_window, columns=("Campo", "Valor"), show="headings", height=5)
            detail_table.heading("Campo", text="Campo")
            detail_table.heading("Valor", text="Valor")
            detail_table.column("Campo", anchor="center", width=100)
            detail_table.column("Valor", anchor="center", width=150)
            detail_table.pack(pady=20, fill=tk.BOTH, expand=True)

            # Insertar los detalles del registro en la tabla
            for key, value in selected_record.items():
                detail_table.insert("", "end", values=(key.capitalize(), value))

# Inicialización de la aplicación
if __name__ == "__main__":
    # URL de la API de Mockapi para el recurso de la escuela de baile
    base_url = "https://6721384998bbb4d93ca7d492.mockapi.io/Usuarios"
    app = App(base_url)
    app.mainloop()
