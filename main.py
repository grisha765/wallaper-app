# импортирование модулей
import os
import subprocess
try:
    import requests
    from bs4 import BeautifulSoup
    #print("[Debug] Modules import") # debug
except:
    print("Dependencies no found! Install dependencies? \nYes or No:")
    answer = input(">>")
    if answer == "Yes":
        os.system('pip install requests beautifulsoup4 lxml')
        print("Restart the utility.")
    if answer == "No":
        print("Good Bye!")
        exit()
from urllib.request import urlretrieve
import platform
import configparser
import re
import random
import ctypes

def add_config(): # создание конфига
    #print("[Debug] Detect OS: " + platform.system()) # debug
    global path_app
    if platform.system() == 'Linux':
        path_app = subprocess.getoutput("echo ~") + "/.config/wallapers-app/"
        if os.path.exists(f"{path_app}") == False:
            os.mkdir(f"{path_app}")
    if platform.system() == 'Windows':
        path_app = subprocess.getoutput("powershell.exe $HOME") + "\AppData\Local\wallapers-app\\" # путь для конфига
        if os.path.exists(f"{path_app}") == False:
            os.mkdir(f"{path_app}")
    if os.path.exists(f"{path_app}config_wallapers.ini") == False:
        config_text_size = "# Choose your size:\n# 240x320, 240x400, 320x240, 320x480, 360x640\n# 480x800, 480x854, 540x960, 720x1280, 800x600\n# 800x1280, 960x544, 1024x600, 1080x1920, 2160x3840\n# 1366x768, 1440x2560, 800x1200, 800x1420, 938x1668\n# 1280x1280, 1350x2400, 2780x2780, 3415x3415, 1024x768\n# 1152x864, 1280x960, 1400x1050, 1600x1200, 1280x1024\n# 1280x720, 1280x800, 1440x900, 1680x1050, 1920x1200\n# 2560x1600, 1600x900, 2560x1440, 1920x1080, 2048x1152\n# 2560x1024, 2560x1080"
        config_text_category = "# Choose your category:\n# 3d, abstraction, anime, art, vector, cities\n# food, animals, space, love, macro, cars\n# minimalism, motorcycles, music, holidays, nature, miscellaneous\n# words, smilies, sport, textures, dark, technology\n# fantasy, flowers, black"
        config_choose_size = input(f"{config_text_size}"+"\nChoose your size >> ")
        config_choose_category = input(f"{config_text_category}"+"\nChoose your category >> ")
        config_write = f"{config_text_size}\n\n{config_text_category}\n\n[Config]\nsize = {config_choose_size}\ncategory = {config_choose_category}"
        config = open(f"{path_app}config_wallapers.ini","w")
        config.write(config_write)
        print(f"The setup is completed on the path '{path_app}', restart the utility.")
        exit()
    config_parser = configparser.ConfigParser()
    config_parser.read(f"{path_app}config_wallapers.ini")
    global size
    size = config_parser["Config"]["size"]
    global category
    category = config_parser["Config"]["category"]

def html_get(category, page): # получение html документа
    url = f"https://wallpaperscraft.ru/catalog/{category}/page{page}"
    html = requests.get(url).text
    return html

def parsing_pages(html): # получение страниц сайта
    soup = BeautifulSoup(html, "lxml")
    pages_names = soup.find('li', class_='pager__item pager__item_last-page').find_all('a', class_='pager__link')
    for name in pages_names:
        href0 = name.get("href")
        href1 = re.sub(f"/catalog/{category}/page","",href0)
        #print(href1)
    site_number = random.randint(1, int(href1)) # рандом страниц от 1 до максимума
    #print(site_number)
    return site_number

def parsing_wallapers(html): # получение обоев
    #print(html)
    list0 = []
    soup = BeautifulSoup(html, "lxml")
    wallpapers_link = soup.find_all('a', class_='wallpapers__link')
    for name in wallpapers_link:
        href0 = name.get("href")
        href1 = re.sub("wallpaper/","",href0)
        href2 = "https://images.wallpaperscraft.ru/image/single" + href1 + f"_{size}.jpg"
        list0.append(href2) # вносим ссылки на обои в список
    #print(list0)
    link = random.choice(list0) # выбор обоев из списка
    return link

def set_wallaper(link, path): # скачивание и установка обоев
    set0 = f"{path}wallaper.png"
    urlretrieve(f"{link}", f"{path}wallaper.png") # скачивание обоев
    if platform.system() == 'Windows': # установка обоев windows с помощью ctypes
        cs = ctypes.c_buffer(set0.encode()) # местонахождение обоев
        SPI_SETDESKWALLPAPER = 0x14
        ctypes.windll.user32.SystemParametersInfoA(20, 0, cs, 3)
    if platform.system() == 'Linux': # установка обоев linux с помощью утилиты feh
        cs = f"{path}" # местонахождение обоев
        subprocess.call (f'feh --bg-scale {cs}/wallaper.png', shell=True)
if __name__ == '__main__':
    add_config()
    set_wallaper(parsing_wallapers(html_get(category, parsing_pages(html_get(category, 1)))), path_app) # запуск
