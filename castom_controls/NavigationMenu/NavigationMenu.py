import flet as ft

class NavigationMenu(ft.UserControl):
    def __init__(self, page : ft.Page):
        super().__init__()
        self.page = page 

    def build(self):
        return ft.Container(ft.Row([
            ft.ElevatedButton("главная", on_click=lambda _: self.page.go("/")),
            ft.ElevatedButton("статистика", on_click=lambda _: self.page.go("/stat")),
            ft.ElevatedButton("настройки", on_click=lambda _: self.page.go("/settings")),
        ]))