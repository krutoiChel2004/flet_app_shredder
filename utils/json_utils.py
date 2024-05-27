import json

def json_read():
    with open('flet_app_shredder\\settings\\settings.json', "r", encoding='utf-8') as json_file:
        return json.load(json_file)
    
def json_write(data):
    with open('flet_app_shredder\\settings\\settings.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

