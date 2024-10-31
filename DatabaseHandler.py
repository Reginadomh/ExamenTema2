import requests
from tkinter import messagebox

class DatabaseHandler:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_records(self):
        """Obtiene todos los registros desde Mockapi."""
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error de conexión", f"No se pudo conectar: {e}")
            return []
