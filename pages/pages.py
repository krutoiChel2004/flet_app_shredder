import flet as ft

from castom_controls.NavigationMenu.NavigationMenu import NavigationMenu
from castom_controls.WebcamStreamer.WebcamStreamer import WebcamStreamer
from castom_controls.StatModul.StatModul import StatModul
from castom_controls.TrainingModule.TrainingModule import TrainingModule
from castom_controls.SattingsModule.SattingsModule import SattingsModule




def page_home(page: ft.Page):
    navigation_menu = NavigationMenu(page)
    w = WebcamStreamer(page)

    page.views.append(
            ft.View(
                "/",
                [
                    ft.Column([
                        navigation_menu,
                        w,
                    ]),
                    
                ],
            )
        )
    
def page_stat(page: ft.Page):
    navigation_menu = NavigationMenu(page)
    s = StatModul()

    page.views.append(
                ft.View(
                    "/stat",
                    [
                        ft.Column([
                            navigation_menu,
                            s,
                        ])
                        
                    ],
                )
            )
    
def page_training(page: ft.Page):
    navigation_menu = NavigationMenu(page)
    t = TrainingModule(page)

    page.views.append(ft.View(
                    "/page_training",
                    [
                        navigation_menu,
                        t,
                    ],
                ))
    
def page_sattings(page: ft.Page):
    navigation_menu = NavigationMenu(page)
    sattings_module = SattingsModule(page)

    page.views.append(ft.View(
                    "/page_sattings",
                    [
                        navigation_menu,
                        sattings_module,
                    ],
                ))