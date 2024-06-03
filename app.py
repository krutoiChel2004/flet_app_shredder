import flet as ft

from pages.pages import (page_home,
                         page_stat,
                         page_training,
                         page_sattings)

def main(page: ft.Page):
    page.title = "fletCam"
    def route_change(route):
        page.views.clear()
        page_home(page)

        if page.route == "/stat":
            page_stat(page)
        # elif page.route == "/training_module":
        #     training_module(page)
        elif page.route == "/settings":
            page_sattings(page)

        page.update()

    page.on_route_change = route_change
    page.go(page.route)

    page.update()

ft.app(target=main)