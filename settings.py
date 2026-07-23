SETTING_FILE = "setting.json"

import os 
import json 


def load_settings():
    if not os.path.exists(SETTING_FILE):
        return {"promo" : 0}
    with open(SETTING_FILE, "r") as setfile:
         return json.load(setfile) 
    


def save_setting(setting):
  
  with open(SETTING_FILE, "w") as setfile:
        json.dump(setting, setfile, indent=4)






