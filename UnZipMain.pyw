import zipfile
import os
import shutil
from time import sleep
import json
import ctypes

with open('config.json') as config_file:
    config = json.load(config_file)
pswdC = [ bytes(x, 'utf-8') for x in config["passwords"] ]
lisuzp = []
lisomov = []
cr = 1

while(True):
    for file in os.listdir(config["monipath"]):
        if file.endswith(".zip"):
            lisuzp.append(os.path.join(config["monipath"], file))
        elif file.endswith(".epub"):
            lisomov.append(file)
    if lisuzp != []:
        for zipfi in lisuzp:
            with zipfile.ZipFile(zipfi,"r") as zf:
                try:
                    zf.extractall(config["destpath"])
                except:
                    for tpwdc in pswdC:
                        try:
                            zf.extractall(config["destpath"],pwd=tpwdc)
                        except:
                            pass
                        else:
                            break
                    else:
                        if config["mispwdpop"]:
                            ctypes.windll.user32.MessageBoxW(0, f"The program didn't find a matching password for file:\n {zipfi}\nPlease add the password to the config.json file!", "Error: Password not found!", 0)
                        cr = 0
            if cr:
                os.remove(zipfi)
            cr = 1
    elif lisomov != []:
        for movfi in lisomov:
            try:
                shutil.move(os.path.join(config["monipath"], movfi),os.path.join(config["destpath"], movfi))
            except:
                pass
    lisomov = []
    lisuzp = []
    sleep(config["update-time"]*60)
