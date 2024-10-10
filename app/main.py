import flet as ft

def main(page: ft.Page):
    page.title = "My Flet App"
    page.add(ft.Text("Hello, World!", color="blue"))

# Executa a aplicação Flet
ft.app(target=main)
