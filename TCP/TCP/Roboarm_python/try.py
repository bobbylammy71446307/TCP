import json

def load_error(errorid):
    with open('C:\\arm\\program\\Roboarm\\Roboarm\\en_alarmController.json',"r", encoding="utf-8") as file:
        data = json.load(file)
        for items in data:
            print(items)
            if items['id'] == errorid:
                if items['en']['description'] != "":
                    msg = "Description: " + items['en']['description'] + " "
                    break
    print(msg)
    return msg




load_error(132)