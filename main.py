debug = True # для разработчика
# импортирование модулей
import os
try:
    import requests
    from bs4 import BeautifulSoup
    if debug == True: print("[Debug] Modules import") # debug
except:
    print("Dependencies no found! Install dependencies? \nYes or No:")
    answer = input(">>")
    if answer == "Yes":
        os.system('pip install requests beautifulsoup4 lxml')
        print("Restart the utility.")
    if answer == "No":
        print("Good Bye!")
        exit()
import platform
import configparser
import re

def add_config(): # создание конфига
    print("[Debug] Detect OS: " + platform.system()) # debug
    if platform.system() == 'Linux':
        if debug == False: path_app = sp.getoutput("echo ~") + "/.config/nature-wallapers-app/"
        if debug == False: os.mkdir(f'{path_app}')
        if debug == True: path_app = "/home/grisha/Projects/python/wallapers_app2/" # debug
        if debug == True: print(f"[Debug] You path for app: {path_app}") # debug
    if os.path.exists(f"{path_app}config_wallapers.ini") == False:
        config_text_size = "#Choose your size:\n#240x320, 240x400, 320x240, 320x480, 360x640\n#480x800, 480x854, 540x960, 720x1280, 800x600\n#800x1280, 960x544, 1024x600, 1080x1920, 2160x3840\n#1366x768, 1440x2560, 800x1200, 800x1420, 938x1668\n#1280x1280, 1350x2400, 2780x2780, 3415x3415, 1024x768\n#1152x864, 1280x960, 1400x1050, 1600x1200, 1280x1024\n#1280x720, 1280x800, 1440x900, 1680x1050, 1920x1200\n#2560x1600, 1600x900, 2560x1440, 1920x1080, 2048x1152\n#2560x1024, 2560x1080"
        config_text_category = "#Choose your category:\n#3d, abstraction, anime, art, vector, cities\n#food, animals, space, love, macro, cars\n#minimalism, motorcycles, music, holidays, nature, miscellaneous\n#words, smilies, sport, textures, dark, technology\n#fantasy, flowers, black"
        config_choose_size = input(f"{config_text_size}"+"\n>>")
        config_choose_category = input(f"{config_text_category}"+"\n>>")
        config_write = f"{config_text_size}\n\n{config_text_category}\n\n[Config]\nsize = {config_choose_size}\ncategory = {config_choose_category}"
        if debug == True: print(f"[Debug] Config write:\n{config_write}") # debug
        if debug == False: config = open(f"{path_app}config_wallapers.ini","w")
        if debug == False: config.write(config_write)
    config_parser = configparser.ConfigParser()
    config_parser.read(f"{path_app}config_wallapers.ini")
    size = config_parser["Config"]["size"]
    global category
    category = config_parser["Config"]["category"]

def html_get(category, page): # получение html документа
    url = f"https://wallpaperscraft.ru/catalog/{category}/{page}"
    html = requests.get(url).text
    return html

def parsing_pages(html): # получение страниц сайта
    soup = BeautifulSoup(html, "lxml")
    pages_names = soup.find('li', class_='pager__item pager__item_last-page').find_all('a', class_='pager__link')
    for name in pages_names:
        href0 = name.get("href")
        href1 = re.sub(f"/catalog/{category}/page","",href0)
        if debug == True: print(f"[Debug] page in site: {href1}") # debug

def parsing_wallapers(html): # получение ссылок на обои
    pass

if __name__ == '__main__':
    add_config()
    parsing_pages(html_get(category, ""))
