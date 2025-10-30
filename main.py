import os
import configparser

repo = "https://raw.githubusercontent.com/KrackF1/kaplin/refs/heads/main/"

def file():
    os.system(f"curl -o config.ini {repo}config.ini")
    config = configparser.ConfigParser()
    config.read('config.ini')
    section = "download"
    current_directory = os.getcwd()
    os.chdir(current_directory)
    for option in config.options(section):
        config.options('setup')
        file = config.get(section, option).replace('"', '')
        saveas = config.get("setup", option).replace('"', '').replace('/', '\\')
        directory = saveas
        if directory.rfind('\\') != -1:
            directory = saveas[:directory.rfind('\\')]
        os.system(f"mkdir {directory}")
        os.system(f"curl -o {saveas} {repo}{file}")


if __name__ == '__main__':
    file()
