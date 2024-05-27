import requests
import cv2

bot_token = '6850830632:AAFEkl7styQbto0lDxhQ6BhQ-MMUjvajhM0'

chat_id = '1015604262'

def send_photo_TG(numpy_array, list_cls:list=None):
    # Преобразование массива NumPy в изображение
    image = cv2.imencode('.jpg', numpy_array)[1].tobytes()
    converted_list_cls_to_str = ", ".join(str(element.item()) for element in list_cls)

    # Отправка фото через Telegram Bot API без сохранения на диск
    url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
    data = {'chat_id': chat_id}
    files = {'photo': ('photo.jpg', image)}

    data['caption'] = f"Обнаружен объект: {converted_list_cls_to_str}"
    response = requests.post(url, data=data, files=files)

    return response.json()