import tkinter as tk
from tkinter import ttk, messagebox

class RecordTable:
    def __init__(self, parent):
        # Crear el estilo para centrar y cambiar la fuente
        style = ttk.Style()
        style.configure("Custom.Treeview.Heading", font=("Helvetica", 12, "bold"))  # Fuente para encabezado
        style.configure("Custom.Treeview", font=("Helvetica", 10))  # Fuente para los registros
        style.configure("Treeview", rowheight=25)  # Altura de las filas

        # Crear el Treeview con el estilo personalizado
        self.table = ttk.Treeview(parent, columns=("ID"), show="headings", style="Custom.Treeview")
        self.table.heading("ID", text="ID", anchor="center")  # Centrar el encabezado de la columna
        self.table.column("ID", anchor="center", width=100)  # Centrar los valores de la columna y ajustar el ancho
        self.table.pack(pady=20, fill=tk.BOTH, expand=True)

    def populate_table(self, records):
        """Llena la tabla con los IDs de los registros obtenidos de la base de datos."""
        # Limpiar la tabla antes de agregar nuevos registros
        for row in self.table.get_children():
            self.table.delete(row)

        # Insertar solo el ID en la tabla y centrarlo
        for record in records:
            self.table.insert("", "end", values=(record["id"],))

    def get_selected_record(self):
        """Obtiene el registro seleccionado en la tabla."""
        selected_item = self.table.focus()
        if not selected_item:
            messagebox.showinfo("Información", "Por favor, seleccione un registro.")
            return None
        return self.table.item(selected_item)["values"][0]  # Devuelve solo el ID
