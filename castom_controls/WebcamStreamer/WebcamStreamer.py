import time
import cv2
import re
import flet as ft

from utils.json_utils import (json_read,
                              json_write)

from utils.webcam_streamer_utils import (process_frame)

class WebcamStreamer(ft.UserControl):

    def __init__(self, page : ft.Page):
        super().__init__()
        self.page = page
        self.data_json_settings = json_read()


    def build(self):
        self.image_box = ft.Image(src="D:\\SHD\\flet_app_shredder\\gg.png")
        self.video_container = ft.Container(self.image_box)

        self.frame_delay = ft.TextField(label="задержка", 
                               width=200,
                               on_change=self.remove_non_digit_characters, 
                               hint_text="введите длительность задержки", 
                               value=self.data_json_settings["frame_delay"])
        
        self.operating_mode_dropdown = ft.Dropdown(label="Режим работы",
                                               width=200,
                                               value=self.data_json_settings["operating_mode"],
                                               options=[ft.dropdown.Option("детекция"),
                                                        ft.dropdown.Option("сбор данных")])
        
        self.button_save_settings = ft.CupertinoFilledButton(content=ft.Text("сохранить"),
                                                             opacity_on_click=0.3,
                                                             on_click=self.save_settings)

        self.button_start = ft.CupertinoFilledButton(content=ft.Text("start"),
                                                     opacity_on_click=0.3,
                                                     on_click=self.start_stream)
        
        self.button_stop = ft.CupertinoFilledButton(content=ft.Text("stop"),
                                                    opacity_on_click=0.3,
                                                    on_click=self.stop_stream,
                                                    disabled=True)

        return ft.Container(
            ft.Row(
                [
                    ft.Column(
                        [
                            self.frame_delay,
                            self.operating_mode_dropdown,
                            self.button_save_settings
                        ],
                        alignment=ft.MainAxisAlignment.START
                        ),
                    ft.Column(
                        [
                            self.video_container,
                            ft.Row(
                                [
                                    self.button_start,
                                    self.button_stop
                                ],
                                alignment=ft.MainAxisAlignment.END
                            )
                        ]
                    )
                ]
            )
        )
    

    def save_settings(self, e):
        data = json_read()
        
        data["frame_delay"] = int(self.frame_delay.value)
        data["operating_mode"] = self.operating_mode_dropdown.value

        json_write(data)

    def remove_non_digit_characters(self, e):
        # Удаляет все символы кроме чисел из frame_delay
        self.frame_delay.value = re.sub(r'\D', '', self.frame_delay.value)
        self.update()
        
    def start_stream(self, e):
        # Запуск стрима
        self.button_start.disabled = True
        
        self.update()
        self.cap = cv2.VideoCapture(1)
        self.button_stop.disabled = False
        
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            result = process_frame(self.operating_mode_dropdown.value ,frame)
            if ret:                
                self.image_box.src_base64 = result["img_b64_string"]
                self.update()
            else:
                break
            if self.frame_delay.value == '':
                time.sleep(0)
            else:
                time.sleep(int(self.frame_delay.value))

    def stop_stream(self, e):
        # Остановка стрима
        self.cap.release()
        self.button_start.disabled = False
        self.button_stop.disabled = True
        self.update()
    