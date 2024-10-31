import tkinter as tk
from tkinter import ttk, messagebox


class RecordTable:
    def __init__(self, parent):
        # Crear el estilo para centrar y cambiar la fuente
        style = ttk.Style()
        style.configure("Custom.Treeview.Heading", font=("Helvetica", 12, "bold"))
        style.configure("Custom.Treeview", font=("Helvetica", 10))
        style.configure("Treeview", rowheight=25)

        # Configurar la tabla con todas las columnas de datos
        self.table = ttk.Treeview(parent, columns=("ID", "Nombre", "Apellido", "Ciudad", "Calle", "Estilo"),
                                  show="headings", style="Custom.Treeview")
        self.table.heading("ID", text="ID")
        self.table.heading("Nombre", text="Nombre")
        self.table.heading("Apellido", text="Apellido")
        self.table.heading("Ciudad", text="Ciudad")
        self.table.heading("Calle", text="Calle")
        self.table.heading("Estilo", text="Estilo de Baile")

        # Centrar todas las columnas y ajustar ancho
        for column in ("ID", "Nombre", "Apellido", "Ciudad", "Calle", "Estilo"):
            self.table.column(column, anchor="center", width=100)

        self.table.pack(pady=20, fill=tk.BOTH, expand=True)

    def populate_table(self, records):
        """Llena la tabla con todos los datos de cada registro en la base de datos."""
        # Limpiar la tabla antes de agregar nuevos registros
        for row in self.table.get_children():
            self.table.delete(row)

        # Insertar todos los datos de cada registro en la tabla
        for record in records:
            self.table.insert("", "end", values=(
                record["id"], record["nombre"], record["apellido"], record["ciudad"], record["calle"], record["estilo"]
            ))

    def get_selected_record_id(self):
        """Obtiene el ID del registro seleccionado en la tabla."""
        selected_item = self.table.focus()
        if not selected_item:
            messagebox.showinfo("Información", "Por favor, seleccione un registro.")
            return None
        return self.table.item(selected_item)["values"][0]  # Devuelve solo el ID seleccionado
