# wallaper-app
Python utility for downloading and setting wallpapers from wallpaperscraft.ru based on user-defined preferences such as size and category.
### Initial Setup
1. **Download Dependencies for os**: install FEH into your linux distribution.
2. **Clone the repository**: Clone this repository using `git clone`.
3. **Create Virtual Env**: Create a Python Virtual Env `venv` to download the required dependencies and libraries.
4. **Download Dependencies for python**: Download the required dependencies into the Virtual Env `venv` using `pip`.

```shell
git clone https://github.com/grisha765/wallaper-app.git
cd wallaper-app
python3 -m venv venv
venv/bin/pip3 install requests beautifulsoup4 lxml
```

### Run Utility

1. Configure Utility: Configure the utility by setting your preferred wallpaper size and category.
2. Start the Utility: Start the utility to download and set wallpapers based on your preferences.

```shell
venv/bin/python3 main.py
```

### Features

1. Downloads wallpapers from wallpaperscraft.ru based on user-defined preferences.
2. Supports customization of wallpaper size and category.
3. Sets wallpapers on both Windows and Linux systems.

### Configuration

1. The utility prompts the user to choose wallpaper size and category if the configuration file is not found.
2. Configuration options are stored in config_wallapers.ini.
3. Users can modify their preferences directly in the configuration file if needed.
