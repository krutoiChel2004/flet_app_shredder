import flet as ft
import shutil
import os

from utils.json_utils import(json_read,
                             json_write)

class SattingsModule(ft.UserControl):
    def __init__(self, page : ft.Page):
        super().__init__()
        self.page = page
        self.settings_data = json_read()

    def build(self):
        data_json_settings = json_read()
        
        self.pick_files_pt = ft.FilePicker(on_result=self.pick_files_pt_result)
        self.choice_pt = ft.CupertinoFilledButton(
                                "Выберите файл .pt",
                                padding=0,
                                width=200,
                                icon=ft.icons.UPLOAD_FILE,
                                on_click=lambda _: self.pick_files_pt.pick_files(
                                    allowed_extensions=["pt"],
                                    allow_multiple=False
                                    )
                                )
        self.pt_selected_files = ft.Text()

        self.list_nn_models_dropdown = ft.Dropdown(label="модель",
                                          width=200,
                                          value=data_json_settings["selected_nn_models"],
                                          options=self.list_nn_models())
        
        self.pick_directory_dialog = ft.FilePicker(on_result=self.pick_directory_result)
        self.choice_frame_save_directory = ft.CupertinoFilledButton(
                                "путь сохранения кадров",
                                padding=0,
                                width=200,
                                icon=ft.icons.UPLOAD_FILE,
                                on_click=lambda _: self.pick_directory_dialog.get_directory_path()
                                )
        self.frame_save_directory = ft.Text(value=self.settings_data["frame_save_directory"])
        
        self.button_save_settings = ft.CupertinoFilledButton(content=ft.Text("сохранить"),
                                                             opacity_on_click=0.3,
                                                             on_click=self.save_settings)

        self.page.overlay.append(self.pick_files_pt)
        self.page.overlay.append(self.pick_directory_dialog)

        return ft.Container(
                    ft.Column([
                        ft.Column([
                                self.choice_pt,
                                self.pt_selected_files,
                                self.list_nn_models_dropdown
                            ]),
                        ft.Column([
                                self.choice_frame_save_directory,
                                self.frame_save_directory
                            ]),
                        self.button_save_settings
                        ])
                    )   
    
    def save_settings(self, e):
        data = json_read()
        
        data["selected_nn_models"] = self.list_nn_models_dropdown.value
        data["frame_save_directory"] = self.frame_save_directory.value

        json_write(data)

    def list_nn_models(self):
        nn_models = os.listdir(os.path.abspath("flet_app_shredder\\nn_models"))
        return [ft.dropdown.Option(nn_model) for nn_model in nn_models]
    
    def append_nn_model(self, file: ft.FilePickerResultEvent):
         shutil.copy(file.files[0].path, os.path.abspath("flet_app_shredder\\nn_models"))

    def pick_files_pt_result(self, e: ft.FilePickerResultEvent):
        if e.files:   
            if e.files[0].name.split(".")[-1] == "pt":
                self.pt_selected_files.value = e.files[0].name
                print(e.files[0].name)
                self.append_nn_model(e)
        
                self.list_nn_models_dropdown.options.append(ft.dropdown.Option(e.files[0].name))
                self.list_nn_models_dropdown.update()
            else:
                self.pt_selected_files.value = "Выберите файл с разрешением .pt"
        else:
            self.pt_selected_files.value = "Cancelled!"

        self.pt_selected_files.update()

    def pick_directory_result(self, e: ft.FilePickerResultEvent):
        self.frame_save_directory.value = e.path

        self.frame_save_directory.update()