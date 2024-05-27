import flet as ft
import re

from utils.training_utils import training_func

class TrainingModule(ft.UserControl):

    def __init__(self, page : ft.Page):
        super().__init__()
        self.page = page   # to add `SnackBar`

    def build(self):

        self.pick_files_dialog = ft.FilePicker(on_result=self.pick_files_result)
        self.choice_yaml = ft.CupertinoFilledButton(
                                "Выберите файл .yaml",
                                padding=0,
                                width=200,
                                icon=ft.icons.UPLOAD_FILE,
                                on_click=lambda _: self.pick_files_dialog.pick_files(
                                    allow_multiple=True
                                    )
                                )
        self.selected_files = ft.Text()


        self.model = ft.Dropdown(label="модель YOLOv8",
                                  width=200,
                                  value="YOLOv8n",
                                  options=[ft.dropdown.Option("YOLOv8n"),
                                           ft.dropdown.Option("YOLOv8s"),
                                           ft.dropdown.Option("YOLOv8m"),
                                           ft.dropdown.Option("YOLOv8l"),
                                           ft.dropdown.Option("YOLOv8x"),])

        self.epochs = ft.TextField(label="количество эпох", 
                               width=200,
                               on_change=self.remove_non_digit_characters, 
                               hint_text="введите количество эпох", 
                               value=1)
        
        self.imgsz = ft.TextField(label="размер изображения", 
                               width=200,
                               on_change=self.remove_non_digit_characters, 
                               hint_text="введите размер изображения", 
                               value=640)
        
        self.batch = ft.TextField(label="размер batch", 
                                  width=200,
                                  on_change=self.remove_non_digit_characters, 
                                  hint_text="введите размер batch", 
                                  value=16)
        
        self.device = ft.Dropdown(label="устройство для обучения",
                                  width=200,
                                  value="CPU",
                                  options=[ft.dropdown.Option("CPU"),
                                           ft.dropdown.Option("GPU")])
        
        
        
        self.start_train = ft.CupertinoFilledButton(
                                "начать обучение",
                                padding=0,
                                width=200,
                                on_click=self.start_train_f
                                )

        self.page.overlay.append(self.pick_files_dialog)

        return ft.Container(
                ft.Column([
                    ft.Row(
                        [
                            self.choice_yaml,
                            self.selected_files,
                        ]
                    ),
                    self.model,
                    self.epochs,
                    self.imgsz,
                    self.batch,
                    self.device,
                    self.start_train
                    ]
                )
            )
    
    def start_train_f(self, e):
        training_func(self.model.value,
                      int(self.epochs.value),
                      int(self.imgsz.value),
                      int(self.batch.value),
                      self.device.value)
         
    
    def pick_files_result(self, e: ft.FilePickerResultEvent):
            self.selected_files.value = (
                ", ".join(map(lambda f: f.path, e.files)) if e.files else "Cancelled!"
            )
            self.selected_files.update()
    
    
    def remove_non_digit_characters(self, e):
        # Удаляет все символы кроме чисел из frame_delay
        self.frame_delay.value = re.sub(r'\D', '', self.frame_delay.value)
        self.update()