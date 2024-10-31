from Gui import App

# Inicialización de la aplicación
if __name__ == "__main__":
    # URL de la API de Mockapi para el recurso de la escuela de baile
    base_url = "https://6721384998bbb4d93ca7d492.mockapi.io/Usuarios"
    app = App(base_url)
    app.mainloop()
